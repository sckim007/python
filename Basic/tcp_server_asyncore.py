import sys
import asyncore
import socket
import threading
import inspect
import json

class ServerSocket(asyncore.dispatcher):
    def __init__(self, address=('localhost', 10000)):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(address)
        self.listen(10)
        self.remote_clients = []

    def writable(self):
        return True

    def handle_expt(self):
        print("Close socket : ", inspect.currentframe().f_lineno)
        self.close()

    def handle_accept(self):
        socket, address = self.accept()
        print("Connected from", address)
        self.remote_clients.append(ConnectSocket(self, socket, address))
        print("Remote clients = ", len(self.remote_clients))

class ConnectSocket(asyncore.dispatcher):
    def __init__(self, server, socket, address):
        asyncore.dispatcher.__init__(self, socket)
        self.server = server
        self.receivedBytes = 0
        self.sentBytes = 0

    def handle_read(self):
        # First recv 4 bytes for message length
        recv_bytes_data = b''
        while len(recv_bytes_data) < 4:
            chunk = self.socket.recv(4 - len(recv_bytes_data))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            recv_bytes_data += chunk

        # Read message length
        msg_length = int.from_bytes(recv_bytes_data, byteorder='big')
        # Next recv message body
        recv_bytes_data = b''
        while len(recv_bytes_data) < msg_length:
            chunk = self.socket.recv(msg_length - len(recv_bytes_data))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            recv_bytes_data += chunk

        if recv_bytes_data:
            self.receivedBytes += len(recv_bytes_data)
            self.sentBytes += len(recv_bytes_data)

            # send_buffer : 4byte length + message body
            send_buff = bytes()
            send_buff += msg_length.to_bytes(4, byteorder='big')
            send_buff += recv_bytes_data
            total_sent = 0
            while total_sent < (msg_length + 4):
                sent = self.socket.send(send_buff[total_sent:])  # type : bytes
                if sent == 0:
                    raise RuntimeError("socket connection broken")
                total_sent = total_sent + sent

            # Parsing message : TBD
            self.parse_data(recv_bytes_data)
        else:
            print("Close socket : ", inspect.currentframe().f_lineno)
            self.close()

    def handle_close(self):
        try:
            # 삭제하기 위해 list의 index를 계산함
            index = 0
            for client in self.server.remote_clients:
                if client.addr == self.addr:
                    break
                index += 1
            # Closed client address and port 출력
            print("Closed from : ", self.server.remote_clients[index].addr)
            # Closed socket
            print("Close socket : ", inspect.currentframe().f_lineno)
            self.close()
            # 인덱스에 해당하는 Entry를 삭제
            del(self.server.remote_clients[index])
        except Exception as msg:
            print("Recv : %s\n terminating program" % msg)
            sys.exit(1)

    def clear_bytes(self):
        self.receivedBytes = 0
        self.sentBytes = 0

    def parse_data(self, data):
        #print('Received : ', json.loads(data))
        pass


class EventThread(threading.Thread):
    def __init__(self, event, server):
        threading.Thread.__init__(self)
        self.stopped = event
        self.report_interval = 5.0
        self.server = server

    def run(self):
        while not self.stopped.isSet():
            self.stopped.wait(self.report_interval)
            self.report()

    def report(self):
        if len(self.server.remote_clients) == 0:
            print("Not exist client connection")
'''
        for client in self.server.remote_clients:
            print("Client: %s " % (str(client.addr)),
                  "Recv: %.2f KB/sec" % (client.receivedBytes / float(self.report_interval) / 1024.0),
                  "Sent: %.2f KB/sec" % (client.sentBytes / float(self.report_interval) / 1024.0))
            client.clear_bytes()
'''
if __name__ == '__main__':
    try:
        # Running Server
        server = ServerSocket(('localhost', 10000))

        # Running Report Thread
        stopFlag = threading.Event()
        t = EventThread(stopFlag, server)

        # Enter Loop
        t.start()
        asyncore.loop()
    except:
        print("STOP")
        stopFlag.set()