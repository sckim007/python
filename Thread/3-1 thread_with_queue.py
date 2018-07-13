'''
Queue
-------------------------------------------------------------------------------
다음 예 에서는 생산자-소비자 패턴의 가장 중요한 큐를 다룰 것이다. 생산자가
아이템을 큐에 넣어주면 소비자들은 그것을 가져와서 사용하는데 , 그것들 사이의
동기화는 Queue 에서 모두 해결해준다.
즉 더이상 생산자가 task 를 추가할 수 없으면 put 에서 대기를 하게되고, 소비자가
더 이상 가져올 task 가 없으면 get 에서 기다리게 된다.
-------------------------------------------------------------------------------
'''
import threading
import time
import logging
import random
import queue


logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s', )

BUF_SIZE = 10
q = queue.Queue(BUF_SIZE)

class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ProducerThread, self).__init__()
        self.target = target
        self.name = name

    def run(self):
        while True:
            if not q.full():
                item = random.randint(1, 10)
                q.put(item)
                logging.debug('Putting ' + str(item)
                              + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(random.random())
        return

class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerThread, self).__init__()
        self.target = target
        self.name = name
        return

    def run(self):
        while True:
            if not q.empty():
                item = q.get()
                logging.debug('Getting ' + str(item)
                              + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(random.random())
        return


if __name__ == '__main__':
    p = ProducerThread(name='producer')
    c = ConsumerThread(name='consumer')

    p.start()
    time.sleep(2)
    c.start()
    time.sleep(2)