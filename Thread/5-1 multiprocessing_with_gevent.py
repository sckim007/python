'''
import gevent
from gevent import Greenlet

class MyGreenlet(Greenlet):

    def __init__(self, message, n):
        Greenlet.__init__(self)
        self.message = message
        self.n = n

    def _run(self):
        print(self.message, self.n)
        gevent.sleep(self.n)
        print("See you", self.n)

g = []
for i in range(5):
    g.append(MyGreenlet("Hi there!", i))
for i in range(5):
    g[i].start()
for i in range(5):
    g[i].join()
'''

'''
import gevent
from gevent import Timeout

def wait():
    gevent.sleep(1)

timer = Timeout(2).start()
thread1 = gevent.spawn(wait)

try:
    thread1.join(timeout=timer)
except Timeout:
    print('Thread 1 timed out')

# --

timer = Timeout.start_new(2)
thread2 = gevent.spawn(wait)

try:
    thread2.get(timeout=timer)
except Timeout:
    print('Thread 2 timed out')

# --

try:
    gevent.with_timeout(2, wait)
except Timeout:
    print('Thread 3 timed out')
'''

import gevent
from gevent.queue import Queue, Empty

tasks = Queue(maxsize=100)

def worker(n):
    try:
        while True:
            task = tasks.get(timeout=1) # decrements queue size by 1
            print('Worker %s got task %s, len %s' % (n, task, tasks.qsize()))
            gevent.sleep(0)
    except Empty:
        print('Quitting time!')

def boss():
    """
    Boss will wait to hand out work until a individual worker is
    free since the maxsize of the task queue is 3.
    """

    for i in range(1,10):
        tasks.put(i)
    print('Assigned all work in iteration 1')

    for i in range(10,20):
        tasks.put(i)
    print('Assigned all work in iteration 2')

    while True:
        i += 1
        tasks.put(i)

gevent.joinall([
    gevent.spawn(boss),
    gevent.spawn(worker, 'steve'),
    gevent.spawn(worker, 'john'),
    gevent.spawn(worker, 'bob'),
])
