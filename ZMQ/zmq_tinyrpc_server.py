'''
refer : https://github.com/mbr/tinyrpc/tree/master/examples
import tinyrpc
'''
import zmq

from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
from tinyrpc.transports.zmq import ZmqServerTransport
from tinyrpc.server import RPCServer
from tinyrpc.dispatch import RPCDispatcher

ctx = zmq.Context()
dispatcher = RPCDispatcher()
transport = ZmqServerTransport.create(ctx, 'tcp://127.0.0.1:5001')

rpc_server = RPCServer(
    transport,
    JSONRPCProtocol(),
    dispatcher
)

@dispatcher.public
def reverse_string(s):
    return s[::-1]

@dispatcher.public
def double_string(s):
    return s + s

@dispatcher.public
def echo_string(s):
    return s


rpc_server.serve_forever()