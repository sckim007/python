'''
refer : https://github.com/mbr/tinyrpc/tree/master/examples

import tinyrpc
'''
import zmq
import json

from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
from tinyrpc.transports.zmq import ZmqClientTransport
from tinyrpc import RPCClient
import time


ctx = zmq.Context()

rpc_client = RPCClient(
    JSONRPCProtocol(),
    ZmqClientTransport.create(ctx, 'tcp://127.0.0.1:5001')
)

remote_server = rpc_client.get_proxy()

# call a method called 'reverse_string' with a single string argument
result = remote_server.reverse_string('Hello, World!')
print("Server answered:", result)

result = remote_server.double_string('Hello, World!')
print("Server answered:", result)

# JSON Data Structure send/receive
print(time.ctime())
for _ in range(1000000):
    req_str = json.dumps({"c": 0, "b": 0, "a": 0})
    rep_str = remote_server.echo_string(req_str)
    #print(rep_str)
print(time.ctime())


