import asyncore
import socket
import threading
import json

# Global byte counter
bytes = []
bytes.append(0)
connections = []
connections.append(0)

class ServerSocket(asyncore.dispatcher):
    def __init__(self, address=('localhost', 10000)):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        #self.bind(('localhost', port))
        self.bind(address)
        self.listen(5)
        self.remote_clients = []

    def handle_accept(self):
        newSocket, address = self.accept()
        print("Connected from", address)
        print("Type : ", type(address))
        #ConnectSocket(newSocket)
        self.remote_clients.append(ConnectSocket(self, newSocket, address))
        print("Remote clients = ", len(self.remote_clients))

class ConnectSocket(asyncore.dispatcher):
    def __init__(self, server, socket, address):
        asyncore.dispatcher.__init__(self, socket)
        self.server = server

    def handle_read(self):
        receivedData = self.recv(4096)
        if receivedData:
            bytes[0] += len(receivedData)
            self.send(receivedData)
            self.parse_data(receivedData)
        else:
            self.close()

    def handle_close(self):
        connections[0] -= 1
        print("Disconnected: ", self.addr)
        print("List length : ", len(self.server.remote_clients))
        i = 0
        for client in self.server.remote_clients:
            if client.addr == self.addr:
                print("\t client list : ", client.addr)
                print("\t client self : ", self.addr)
                break
            i += 1
        print("Index ===> ", i)
        del(self.server.remote_clients[i])
        print("List length : ", len(self.server.remote_clients))


    def parse_data(self, data):
        print('Received : ', json.loads(data))


class EventThread(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event
        self.report_interval = 5.0

    def run(self):
        while not self.stopped.isSet():
            last_conns = connections[0]
            last_bytes = bytes[0]
            self.stopped.wait(self.report_interval)
            this_conns = connections[0]
            this_bytes = bytes[0]
            self.report(this_bytes - last_bytes, this_conns - last_conns)

    def report(self, diff_bytes, diff_conns):
        print("%d connections/sec, %.2f KB/sec" % (
            diff_conns / 5.0,
            float(diff_bytes) / float(self.report_interval) / 1024.0)
        )

if __name__ == '__main__':
    try:
        # Running Server
        ServerSocket(('localhost', 10000))

        # Running Report Thread
        stopFlag = threading.Event()
        t = EventThread(stopFlag)

        # Enter Loop
        t.start()
        asyncore.loop()
    except:
        print("STOP")
        stopFlag.set()