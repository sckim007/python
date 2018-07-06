import socket
import sys
import json
import time

jsonFile = 'girlfriend.json'
def read_json_data():
    fp = open(jsonFile, 'r', encoding='utf-8')
    data = json.load(fp)
    fp.close()
    print(data)
    return data

def send_json_data(message):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print(sys.stderr, 'connecting to %s port %s' % server_address)
    sock.connect(server_address)

    try:
        for i in range(5):
            i += 1
            print(i, "th Message")
            # Convert dict to bytes and Send data
            print('Send Type :', type(message))             # type : dict
            print('Sending: ', message)
            sock.sendall(json.dumps(message).encode())      # type : bytes

            # Receive data
            recv_bytes_data = sock.recv(4096)               # type : bytes
            recv_dict_data = json.loads(recv_bytes_data)    # type : dict
            print('Received: ', recv_dict_data)

            time.sleep(1)
    finally:
        print(sys.stderr, 'closing socket')
        sock.close()

if __name__ == '__main__':
    data = read_json_data()
    send_json_data(data)