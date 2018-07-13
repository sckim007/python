'''
Process Communication
-------------------------------------------------------------------------------
communicating 모듈은 프로세스 간 통신시 Queues 와 Pipes라는 두 가지 기본 방법을
사용한다. 큐는 실제로 스레드와 프로세스에서 빈번히 사용되며 잘 구현되어 있다.
-------------------------------------------------------------------------------
* 주의 사항 : multiprocessing 의 Queue 입니다. 그냥 import Queue 는 쓰레드간에 사용됨.

먼저 Queue 및 Process를 import 한다. 그런 다음 데이터를 생성하여 큐에 추가하고
데이터를 소비하고 처리하는 두 가지 기능을 수행한다. Queue에 데이터를 추가하는 것은
Queue의 put () 메소드를 사용하는 반면 Queue에서 데이터를 가져 오는 것은
get 메소드를 통해 수행된다. 코드의 마지막 덩어리는 Queue 객체와 두 개의 프로세스를
생성 한 다음 실행한다. Queue 자체보다는 프로세스 객체에 대해 join ()을 호출한다.
'''
from multiprocessing import Process, Queue

sentinel = -1

def creator(data, q):
    """ Creates data to be consumed and waits for the consumer to finish processing """
    print('Creating data and putting it on the queue')
    for item in data:
        q.put(item)

def my_consumer(q):
    while True:
        data = q.get()
        print('data found to be processed: {}'.format(data))
        processed = data * 2
        print(processed)
        if data is sentinel:
            break

if __name__ == '__main__':
    q = Queue()
    data = [5, 10, 13, -1]
    process_one = Process(target=creator, args=(data, q))
    process_two = Process(target=my_consumer, args=(q,))
    process_one.start()
    process_two.start()

    q.close()
    q.join_thread()

    process_one.join()
    process_two.join()