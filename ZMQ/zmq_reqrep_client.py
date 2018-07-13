import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5000")
#socket.connect("tcp://127.0.0.1:6000")

#for i in range(10):
i = 0
while True:
    i += 1
    msg = "msg %s" % i
    socket.send(msg.encode())
    print("Sending", msg)
    msg_in = socket.recv()
    print(msg_in.decode())