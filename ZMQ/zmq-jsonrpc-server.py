'''
install : jsonrpcserver
'''
import zmq
from jsonrpcserver import methods
from jsonrpcserver.response import NotificationResponse

socket = zmq.Context().socket(zmq.REP)

@methods.add
def ping(args):
    print(args)
    return args

@methods.add
def ping1():
    return 'pong1'

@methods.add
def ping2():
    return 'pong2'

if __name__ == '__main__':
    socket.bind('tcp://*:5000')
    while True:
        request = socket.recv().decode()
        response = methods.dispatch(request)
        socket.send_string(str(response))