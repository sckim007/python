# create a JSON-RPC-server
from sckim import jsonrpc_diy as jrpc

server = jrpc.Server(jrpc.JsonRpc20(),
                     jrpc.TransportTcpIp(addr=("127.0.0.1", 31415),
                                         logfunc=jrpc.log_file("myrpc.log")))

# define some example-procedures and register them (so they can be called via RPC)
def echo(s):
    return s

def search(number=None, last_name=None, first_name=None):
    """
    sql_where = []
    sql_vars  = []
    if number is not None:
        sql_where.append("number=%s")
        sql_vars.append(number)
    if last_name is not None:
        sql_where.append("last_name=%s")
        sql_vars.append(last_name)
    if first_name is not None:
        sql_where.append("first_name=%s")
        sql_vars.append(first_name)
    sql_query = "SELECT id, last_name, first_name, number FROM mytable"
    if sql_where:
        sql_query += " WHERE" + " AND ".join(sql_where)
    cursor = ...
    cursor.execute(sql_query, *sql_vars)
    return cursor.fetchall()
    """
    result = '{"jsonrpc": "2.0", "result": [{"first_name": "Brian", "last_name": "Python", "id": 1979, "number": 42}, {"first_name": "Monty", "last_name": "Python", "id": 4, "number": 1}], "id": 0}'
    print(result)
    return result

server.register_function(echo)
server.register_function(search)

# start server
server.serve()