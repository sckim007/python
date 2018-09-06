'''
refer : https://github.com/mbr/tinyrpc/tree/master/examples
import gevent
import tinyrpc
'''
import gevent
#import gevent.wsgi     # Linux
import gevent.pywsgi    # Windows
import gevent.queue
from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
from tinyrpc.transports.wsgi import WsgiServerTransport
from tinyrpc.server.gevent import RPCServerGreenlets
from tinyrpc.dispatch import RPCDispatcher

dispatcher = RPCDispatcher()
transport = WsgiServerTransport(queue_class=gevent.queue.Queue)

# start wsgi server as a background-greenlet
#wsgi_server = gevent.wsgi.WSGIServer(('127.0.0.1', 5000), transport.handle)
wsgi_server = gevent.pywsgi.WSGIServer(('127.0.0.1', 5000), transport.handle)
gevent.spawn(wsgi_server.serve_forever)

rpc_server = RPCServerGreenlets(
    transport,
    JSONRPCProtocol(),
    dispatcher
)


@dispatcher.public
def reverse_string(s):
    print("Recv : ", s)
    return s[::-1]

# in the main greenlet, run our rpc_server
rpc_server.serve_forever()