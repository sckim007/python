import zmq

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://127.0.0.1:5555")

#for i in range(10):
i = 0
while True:
    i += 1
    msg = "msg %s" % i
    socket.send(msg.encode())
    recv_msg = socket.recv()
    print(recv_msg.decode())