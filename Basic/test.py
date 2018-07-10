'''
파일, 라인 출력
'''
import inspect

print("File : ", inspect.currentframe().filename)
print("Line : ", inspect.currentframe().f_lineno)


'''
Pack/Unpack Example
'''
import struct

var = struct.pack('hhl', 5, 10, 15)
print(var)

var = struct.pack('iii', 10, 20, 30)
print(var)

var_dict = dict()
var_dict['aa'] = 100
var_dict['bb'] = 200
print(var_dict)

var_10 = 10
var_20 = 20

bb = bytes('abcd'.encode())
print(bb)

pack_var = struct.pack('ib', var_10, bb)


