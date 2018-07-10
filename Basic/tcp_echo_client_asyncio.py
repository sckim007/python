'''
http://asyncio.readthedocs.io/en/latest/tcp_echo.html
'''
import asyncio
import time

async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888,
                                                   loop=loop)

    print('Send: %r' % message)
    writer.write(message.encode())

    data = await reader.read(100)
    print('Received: %r' % data.decode())

    print('Close the socket')
    writer.close()

message = 'Hello World!'

loop = asyncio.get_event_loop()
count = 0
while True:
    loop.run_until_complete(tcp_echo_client(message, loop))
    count = count +1
    print('count : ', count)
    time.sleep(1)
loop.close()
