# create JSON-RPC client
from sckim import jsonrpc_diy as jrpc

server = jrpc.ServerProxy(jrpc.JsonRpc20(), jrpc.TransportTcpIp(addr=("127.0.0.1", 31415)))

# call a remote-procedure (with positional parameters)
#result = server.echo("hello world")

# call a remote-procedure (with named/keyword parameters)
found = server.search(last_name='Python')