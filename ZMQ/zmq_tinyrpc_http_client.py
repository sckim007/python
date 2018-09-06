'''
refer : https://github.com/mbr/tinyrpc/tree/master/examples
import gevent
import tinyrpc
import gevent-websocket
'''

from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
from tinyrpc.transports.http import HttpPostClientTransport
from tinyrpc import RPCClient

rpc_client = RPCClient(
    JSONRPCProtocol(),
    HttpPostClientTransport('http://127.0.0.1:5000/')
)

remote_server = rpc_client.get_proxy()

# call a method called 'reverse_string' with a single string argument
result = remote_server.reverse_string('Hello, World!')

print("Server answered: ", result)