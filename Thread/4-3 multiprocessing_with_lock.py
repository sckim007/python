'''
Locks
-------------------------------------------------------------------------------
멀티 프로세싱 모듈은 스레딩 모듈과 거의 같은 방식으로 잠금을 지원한다.
가져 오기 잠금, 가져 오기, 무언가를 수행하고 해제만 하면 된다.
-------------------------------------------------------------------------------
'''

from multiprocessing import Process, Lock

def printer(item, lock):
    lock.acquire()
    try:
        print(item)
    finally:
        lock.release()

if __name__ == '__main__':
    lock = Lock()
    items = ['tango', 'foxtrot', 10]
    for item in items:
        p = Process(target=printer, args=(item, lock))
        p.start()
