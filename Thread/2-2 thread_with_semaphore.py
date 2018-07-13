'''
Semaphore
-------------------------------------------------------------------------------
파이썬의 Semaphore 는 정해진 갯수의 쓰레드만 통과시켜준다. 예를들어 웹크롤링을
하는 쓰레드를 50개정도로 한정지어 놓는데 사용할 수 있다.  아래 예제에서는
10개의 쓰레드 중에서 3개만 일을 하도록 한다. 만약 세마포어를 통과한 3개의
쓰레드가 동일한 리소스를 사용하려고 할 때는 그들끼리 Lock 을 통해서 상호배제
되어야 할 것이다.
-------------------------------------------------------------------------------
'''
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)

class ThreadPool(object):
    def __init__(self):
        super(ThreadPool, self).__init__()
        self.active = []
        self.lock = threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)

            time.sleep(5)
            logging.debug('Running: %s', self.active)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Running: %s', self.active)

def f(s, pool):
    logging.debug('Waiting to join the pool')
    with s:
        name = threading.currentThread().getName()
        pool.makeActive(name)
        time.sleep(1)
        pool.makeInactive(name)

if __name__ == '__main__':
    pool = ThreadPool()
    s = threading.Semaphore(3)
    for i in range(10):
        t = threading.Thread(target=f, name='thread_'+str(i), args=(s, pool))
        t.start()