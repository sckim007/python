'''
Thread 클래스
-------------------------------------------------------------------------------
메소드/속성        설명
-------------------------------------------------------------------------------
daemon              데몬쓰레드인지-기본은 False, 부모쓰레드가 종료되도 살아있다.
__init__(group,target,name,args,kwargs={},verbose,daemon)  객체를 초기화한다
start()             쓰레드를 실행한다.
run()               쓰레드의 기능을 정희하는 메소드 (상속해서 오버라이드됨)
jon(timeout=None)   쓰레드가 종료될때까지 대기한다.
-------------------------------------------------------------------------------
'''
import threading
from time import sleep, ctime

loops = [8, 2]

def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'at:', ctime())


def test():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all Done at: ', ctime())

if __name__ == '__main__':
   test()