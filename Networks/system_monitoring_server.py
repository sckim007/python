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
import threading
import json
import inspect

clients = []

class SystemMonitoringServer(asyncio.Protocol):
    def __init__(self):
        print("Line : ", inspect.currentframe().f_lineno)
        self.recv_bytes = 0
        self.sent_bytes = 0

    def connection_made(self, transport):
        self.transport = transport
        clients.append(self)
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        print("Clients: ", len(clients))

    def data_received(self, data):
        data_length = len(data)
        # Increase receive bytes
        if data_length > 0:
            self.recv_bytes += data_length
        # Print received message
        self.print_system_message(data)
        # Send received bytes
        self.transport.write(data_length.to_bytes(4, byteorder='big'))
        if len(data) > 0:
            self.sent_bytes += len(data)

    def connection_lost(self, exc):
        print('Connection lost from{}'.format(self.transport.get_extra_info('peername')))
        clients.remove(self)
        print("Clients: ", len(clients))

    def print_system_message(self, data):
        try:
            message = json.loads(data)
        except TypeError:
            print("[Error] Unable to serialize the objects")
        '''
        else:
            print('HOSTNAME : ', message['hostname'])
            print('CPU      : ', message['cpu'])
            print('MEMORY   : ', message['memory'])
            print('SWAP     : ', message['swap'])
            print('DISK     : ', message['disks'])
            print('NETWORKS :')
            for n in message['networks']:
                print('\t', str(n))
        '''

class EventThread(threading.Thread):
    def __init__(self, event, interval):
        threading.Thread.__init__(self)
        self.stopped = event
        self.report_interval = interval

    def run(self):
        while not self.stopped.isSet():
            self.stopped.wait(self.report_interval)
            self.report()

    def report(self):
        if len(clients) == 0:
            print("Not exist client connection")
'''            
        for client in clients:
            print("client recv byte: ", client.recv_bytes)
'''
'''
        for client in self.server.remote_clients:
            print("Client: %s " % (str(client.addr)),
                  "Recv: %.2f KB/sec" % (client.receivedBytes / float(self.report_interval) / 1024.0),
            client.clear_bytes()
'''

def main():
    # Create asyncio loop
    loop = asyncio.get_event_loop()
    # Each client connection will create a new instance
    coro = loop.create_server(SystemMonitoringServer, '127.0.0.1', 8888)
    server = loop.run_until_complete(coro)

    # Running Report Thread
    stop_flag = threading.Event()
    t = EventThread(stop_flag, 5.0)

    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        t.start()               # Enter event thread loop
        loop.run_forever()      # Enter asyncio loop
    except KeyboardInterrupt:
        pass

    server.close()              # Close the server
    loop.run_until_complete(server.wait_closed())
    loop.close()                # Close  asyncio loop
    stop_flag.set()             # Stop event loop

if __name__ == "__main__":
    main()