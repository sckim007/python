'''
Condition
-------------------------------------------------------------------------------
파이썬의 Condidtion 은 쉽게 생각하면 Event + Mutex 쯤으로 보면된다.
다음예를보면 소비자 쓰레드들은 Condition 이 set 이 되길 기다리고 있다. 생산자
쓰레드는 이 Condition을 set 해줘서 다른 쓰레드들에게 진행해도 좋다고 고지한다.
기다리고 있던 쓰레드 모두가 통과할 수 는 없고 상호 배제되어 하나씩 통과된다 .
-------------------------------------------------------------------------------
'''
import threading
import time
import logging
logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)

def consumer(cv):
    logging.debug('Consumer thread started ...')
    with cv:
        logging.debug('Consumer waiting ...')
        cv.wait()
        time.sleep(3)
        logging.debug('Consumer consumed the resource')

def producer(cv):
    logging.debug('Producer thread started ...')
    with cv:
        logging.debug('Making resource available')
        logging.debug('Notifying to all consumers')
        cv.notifyAll()

if __name__ == '__main__':
    condition = threading.Condition()
    cs1 = threading.Thread(name='consumer1', target=consumer, args=(condition,))
    cs2 = threading.Thread(name='consumer2', target=consumer, args=(condition,))
    pd = threading.Thread(name='producer', target=producer, args=(condition,))
    cs1.start()
    time.sleep(1)
    cs2.start()
    time.sleep(2)
    pd.start()
