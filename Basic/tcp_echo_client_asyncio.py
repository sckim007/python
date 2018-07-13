
import asyncio
import time
import inspect

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop
        self.recv_count = 0
        self.send_count = 0
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        self.data_send()

    def data_send(self):
        self.transport.write(self.message.encode())
        self.send_count += 1
        if self.send_count % 10000 == 0:
            print('Data sent: {!r}, sent_count: {}'.format(self.message, self.send_count))

    def data_received(self, data):
        self.recv_count += 1
        if self.recv_count % 10000 == 0:
            print('Data received: {!r}'.format(data.decode(), self.recv_count))
        self.data_send()

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()

loop = asyncio.get_event_loop()
message = 'Hello World!'
coro = loop.create_connection(lambda: EchoClientProtocol(message, loop),
                              '127.0.0.1', 8889)
print("Line : ", inspect.currentframe().f_lineno)
loop.run_until_complete(coro)
print("Line : ", inspect.currentframe().f_lineno)
loop.run_forever()
print("Line : ", inspect.currentframe().f_lineno)
loop.close()
print("Line : ", inspect.currentframe().f_lineno)