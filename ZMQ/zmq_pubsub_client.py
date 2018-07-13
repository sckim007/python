import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:5000")
socket.setsockopt(zmq.SUBSCRIBE, b'portugal')
socket.setsockopt(zmq.SUBSCRIBE, b'brazil')

while True:
    msg = socket.recv()
    print("==>", msg.decode())