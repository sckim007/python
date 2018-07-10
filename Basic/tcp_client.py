import socket
import sys
import json
import time
import signal
import psutil

jsonFile = 'data/girlfriend.json'
def read_json_data():
    fp = open(jsonFile, 'r', encoding='utf-8')
    data = json.load(fp)
    fp.close()
    print(data)
    return data

class MonitorResource:
    def __init__(self, server):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        try:
            print("Connecting to ", server)
            self.sock.connect(server)
        except Exception as msg:
            print("Couldnt connect with the socket-server: %s\n terminating program" % msg)
            sys.exit(1)

    def signal_handler(self, signal, frame):
        print("Signal Handling, Signal = ", signal)
        print(sys.stderr, 'closing socket')
        self.sock.close()
        sys.exit(0)

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

        print("+++++++++++++++")
        for l in networks:
            print('\t', str(l))

        return networks

    def print_resources(self, resources):
        print('HOSTNAME : ', resources['hostname'])
        print('CPU      : ', resources['cpu'])
        print('MEMORY   : ', resources['memory'])
        print('SWAP     : ', resources['swap'])
        print('DISK     : ', str(resources['disk']))
        print('NETWORKS :')
        for l in resources['networks']:
            print('\t', str(l))
        print("end")

    '''
    +-------------------------------------------------------------------------+
    |                             Length(4 Bytes)                             |
    +-------------------------------------------------------------------------+
    |                            Message(any Bytes)                           |
    |                             Dictionary->Byte                            |
    +-------------------------------------------------------------------------+
    '''
    def send_data_dict_2_json(self, message):
        try:
            # Print dictionary data
            print('Send(dick) :', message)
            # Convert dictionary to bytes format
            send_byte_data = json.dumps(message).encode()
            # Send data
            msg_length = len(send_byte_data)
            print("msg_length : ", msg_length)
            # send_buffer
            send_buff = bytes()
            send_buff += msg_length.to_bytes(4, byteorder='big')
            send_buff += send_byte_data
            total_sent = 0
            while total_sent < (msg_length + 4):
                sent = self.sock.send(send_buff[total_sent:])      # type : bytes
                if sent == 0:
                    raise RuntimeError("socket connection broken")
                total_sent = total_sent + sent
        except Exception as msg:
            print("Send : %s\n terminating program" % msg)
            sys.exit(1)

        try:
            # Receive data
            recv_bytes_data = b''
            while len(recv_bytes_data) < 4:
                chunk = self.sock.recv(4 - len(recv_bytes_data))
                if chunk == b'':
                    raise RuntimeError("socket connection broken")
                recv_bytes_data += chunk

            # Read message length
            msg_length = int.from_bytes(recv_bytes_data, byteorder='big')
            print('next body length : ', msg_length)

            # Next recv message body
            recv_bytes_data = b''
            while len(recv_bytes_data) < msg_length:
                chunk = self.sock.recv(msg_length - len(recv_bytes_data))
                if chunk == b'':
                    raise RuntimeError("socket connection broken")
                recv_bytes_data += chunk

            # Convert bytes to dictionary format
            recv_dict_data = json.loads(recv_bytes_data)    # type : dict
            # Print dictionary data
            print('Recv(dic) :', recv_dict_data)

        except Exception as msg:
            print("Recv : %s\n terminating program" % msg)
            sys.exit(1)

    def run(self):
        while True:
            resources = dict()
            resources['hostname'] = socket.gethostname()
            resources['cpu'] = float(self.scan_cpuinfo())
            resources['memory'] = float(self.scan_meminfo())
            resources['swap'] = float(self.scan_swapinfo())
            resources['disk'] = self.scan_diskinfos()
            resources['networks'] = self.scan_netinfos()
            print(self.print_resources(resources))
            self.send_data_dict_2_json(resources)

        self.sock.close()

if __name__ == '__main__':
    #data = read_json_data()
    #send_json_data(data)

    mon = MonitorResource(('localhost', 10000))
    signal.signal(signal.SIGINT, mon.signal_handler)
    signal.signal(signal.SIGTERM, mon.signal_handler)
    mon.run()