'''
Logging
-------------------------------------------------------------------------------
로깅 프로세스는 로깅 스레드와 약간 다르다. 그 이유는 파이썬의 로깅 패키지가
프로세스 공유 잠금을 사용하지 않기 때문에 서로 다른 프로세스의 메시지가 섞여서
끝날 수 있기 때문이다. 이전 예제에 기본 로깅을 추가한다.
-------------------------------------------------------------------------------
'''
import logging
import multiprocessing

from multiprocessing import Process, Lock

def printer(item, lock):
    """
    Prints out the item that was passed in
    """
    lock.acquire()
    try:
        print(item)
    finally:
        lock.release()


if __name__ == '__main__':
    lock = Lock()
    items = ['tango', 'foxtrot', 10]
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    for item in items:
        p = Process(target=printer, args=(item, lock))
        p.start()
