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
        #server_address = ('localhost', 10000)
        #print(sys.stderr, 'connecting to %s' % server)
        try:
            print("Connecting to ", server)
            self.sock.connect(server)
        #except socket.error as msg:
        except Exception as msg:
            print("Couldnt connect with the socket-server: %s\n terminating program" % msg)
            sys.exit(1)

    def signal_handler(self, signal, frame):
        print("Signal Handling, Signal = ", signal)
        print(sys.stderr, 'closing socket')
        self.sock.close()
        sys.exit(0)

    def scan_resource(self):
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()[2]
        swap = psutil.swap_memory()[3]
        line = "CPU  : {}%, ".format(cpu)
        line += "MEM  : {}%, ".format(memory)
        line += "SWAP : {}%, ".format(swap)
        sys_dict = dict()
        sys_dict['cpu'] = float(cpu)
        sys_dict['memory'] = float(memory)
        sys_dict['swap'] = float(swap)
 #       print("dictionary : ", sys_dict)
        line += "DISK ["

        disks = psutil.disk_partitions()
        disk_dict = dict()
        for disk in disks:
            if disk.fstype is '':
                break
            disk_name = disk.mountpoint
            disk_usage = psutil.disk_usage(disk.mountpoint)[3]
            line += "{}:{}% ".format(disk_name, disk_usage)
            disk_dict[disk.mountpoint] = disk_usage
        line += "]"
        sys_dict['disk'] = disk_dict
#        print("dictionary : ", sys_dict)

        return sys_dict, line

    def send_data_dict_2_json(self, message):
        try:
            # Convert dict to bytes and Send data
            send_byte_data = json.dumps(message).encode()
            # Send data
            print('Send :', send_byte_data)
            self.sock.sendall(send_byte_data)      # type : bytes

            # Receive data
            recv_bytes_data = self.sock.recv(4096)          # type : bytes
            print('Recv :', recv_bytes_data)
            recv_dict_data = json.loads(recv_bytes_data)    # type : dict

        except Exception as msg:
            print("Send/Recv : %s\n terminating program" % msg)
            sys.exit(1)

    def run(self):
        while True:
            result_dict, result_str = self.scan_resource()
            #print(">> dictionary : ", result_dict)
            #print(">> string     : ", result_str)
            self.send_data_dict_2_json(result_dict)
            #time.sleep(1)

        self.sock.close()

if __name__ == '__main__':
    #data = read_json_data()
    #send_json_data(data)

    mon = MonitorResource(('localhost', 10000))
    signal.signal(signal.SIGINT, mon.signal_handler)
    signal.signal(signal.SIGTERM, mon.signal_handler)
    mon.run()