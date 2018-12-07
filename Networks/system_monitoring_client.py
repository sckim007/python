"""
system_monitoring_client.py - System monitoring client using asyncio
This will scan system resource and provide information to server.
System resource format is like this
{
    'hostname'  : 'host name',
    'cpu'       : 'cpu usage',
    'memory'    : 'memory usage(%)',
    'swap'      : 'swap usage(%),
    'disks'     : ['disk usage(%)',]
    'networks'  : [{
                        'ip'            : ['ip address',],
                        'iface'         : 'interface name',
                        'isup'          : 'status',
                        'sent'          : sent MB,
                        'recv'          : received MB,
                        'packets_sent'  : sent bytes,
                        'packets_recv'  : recv bytes,
                        'errin'         : incoming error,
                        'errout'        : outgoing error,
                        'dropin'        : drop of incoming packet,
                        'dropout'       : drop of outgoing packet
                    },]
}
"""
import asyncio
import json
import inspect
import socket
import threading
import sys
import signal
import psutil
import time

class SystemMonitoringClient(asyncio.Protocol):
    def __init__(self, loop):
        self.system_resources = {}
        self.loop = loop
        self.recv_count = 0
        self.send_count = 0
        self.send_bytes = 0
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))

    def data_send(self):
        self.scan_system_resources()
        try:
            message = json.dumps(self.system_resources)
        except TypeError:
            print("Unable to serialize the objects")
        else:
            self.send_bytes = len(message.encode())
            self.send_count += 1
            self.transport.write(message.encode())

            if self.send_count % 10 == 0:
                print('Data sent: sent_count: {}'.format(self.send_count))

    def data_received(self, data):
        self.recv_count += 1
        recv_length = int.from_bytes(data, byteorder='big')
        if self.send_bytes != recv_length:
            print("Error : not the same length of send/recv bytes")
            print("Sent: {0}, Recv: {1} ".format(self.send_bytes, recv_length))
            self.loop.stop()
        else:
            if self.recv_count % 10 == 0:
                print('Data recv: recv_count: {}'.format(self.recv_count))

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()

    def scan_cpuinfo(self):
        return float(psutil.cpu_percent(interval=1))

    def scan_meminfo(self):
        return float(psutil.virtual_memory()[2])

    def scan_swapinfo(self):
        return float(psutil.swap_memory()[3])

    def scan_diskinfos(self):   # return type is dictionary
        disk_dict = dict()
        disks = psutil.disk_partitions()
        for disk in disks:
            if disk.fstype is '':
                break
            disk_usage = psutil.disk_usage(disk.mountpoint)[3]
            disk_dict[disk.mountpoint] = float(disk_usage)
        return disk_dict

    def scan_netinfos(self):    # return type is list
        network = psutil.net_io_counters(pernic=True)
        ifaddrs = psutil.net_if_addrs()
        ifstats = psutil.net_if_stats()
        networks = list()
        for k, v in ifaddrs.items():
            iplist = list()
            for addr in v:
                iplist.append(addr.address)
            data = network[k]
            ifnet = dict()
            ifnet['ip'] = iplist
            ifnet['iface'] = k
            ifnet['isup'] = ifstats[k].isup
            ifnet['sent'] = '%.2fMB' % (data.bytes_sent / 1024 / 1024)
            ifnet['recv'] = '%.2fMB' % (data.bytes_recv / 1024 / 1024)
            ifnet['packets_sent'] = data.packets_sent
            ifnet['packets_recv'] = data.packets_recv
            ifnet['errin'] = data.errin
            ifnet['errout'] = data.errout
            ifnet['dropin'] = data.dropin
            ifnet['dropout'] = data.dropout
            networks.append(ifnet)
        return networks

    def print_system_resources(self):
        print('HOSTNAME : ', self.system_resources['hostname'])
        print('CPU      : ', self.system_resources['cpu'])
        print('MEMORY   : ', self.system_resources['memory'])
        print('SWAP     : ', self.system_resources['swap'])
        print('DISK     : ', str(self.system_resources['disks']))
        print('NETWORKS :')
        for l in self.system_resources['networks']:
            print('\t', str(l))

    def scan_system_resources(self):
        self.system_resources = dict()
        self.system_resources['hostname'] = socket.gethostname()
        self.system_resources['cpu'] = float(self.scan_cpuinfo())
        self.system_resources['memory'] = float(self.scan_meminfo())
        self.system_resources['swap'] = float(self.scan_swapinfo())
        self.system_resources['disks'] = self.scan_diskinfos()
        self.system_resources['networks'] = self.scan_netinfos()

        #self.print_system_resources()

class EventThread(threading.Thread):
    def __init__(self, event, interval, client):
        threading.Thread.__init__(self)
        self.stopped = event
        self.report_interval = interval
        self.client = client

    def run(self):
        while not self.stopped.isSet():
            self.stopped.wait(self.report_interval)
            self.report()

    def report(self):
        print("<<<<<<<<<<<< Report >>>>>>>>>>>>>>>")
        self.client.data_send()

def main():
    # Create asyncio loop
    loop = asyncio.get_event_loop()
    monitor_client = SystemMonitoringClient(loop)
    coro = loop.create_connection(lambda: monitor_client, '127.0.0.1', 8888)
    loop.run_until_complete(coro)

    # Running Report Thread
    stop_flag = threading.Event()
    t = EventThread(stop_flag, 1.0, monitor_client)

    try:
        t.start()               # Enter event thread loop
        loop.run_forever()      # Enter asyncio loop
    except KeyboardInterrupt:
        pass

    loop.close()                # Close  asyncio loop
    stop_flag.set()             # Stop event loop

if __name__ == "__main__":
    main()