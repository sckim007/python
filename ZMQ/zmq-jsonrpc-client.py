'''
install : jsonrpcclient
'''
from jsonrpcclient.zeromq_client import ZeroMQClient

print(ZeroMQClient('tcp://localhost:5000').request(method_name='ping', 'kkk'))
print(ZeroMQClient('tcp://localhost:5000').request('ping1'))
print(ZeroMQClient('tcp://localhost:5000').request('ping2'))