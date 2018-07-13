'''
import wmi

computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]

print("os_info: ", os_info)
print("proc_info: ", proc_info)
print("gpu_info: ", gpu_info)

os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

print('OS Name: {0}'.format(os_name.decode()))
print('OS Version: {0}'.format(os_version))
print('CPU: {0}'.format(proc_info.Name))
print('RAM: {0} GB'.format(system_ram))
print('Graphics Card: {0}'.format(gpu_info.Name))
'''

'''
import multiprocessing
#import os
#import ssl

def main():
    server_process = multiprocessing.Process(target=server, name='server')
    server_process.start()

    client_process = multiprocessing.Process(target=client, name='client')
    client_process.start()

def client():
    i = 0;
    while True:
        i += 1
        print("Client: ", i)

def server():
    i = 0;
    while True:
        i += 1
        print("Server: ", i)

if __name__ == "__main__":
    main()
'''

import threading
from time import sleep, ctime

loops = [8,2]

def loop(nloop,nsec):
    print('start loop', nloop, 'at:',ctime())
    sleep(nsec)
    print('loop', nloop, 'at:', ctime())


def test() :
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all Done at: ', ctime())

if  __name__ == '__main__' :
   test()
