'''
1. 쓰레드

파이썬에서의 쓰레드는 보통 Thread 혹은 Threading 모듈을 사용할 수 있다.
또한 Queue 모듈을 통해서 생산자-소비자 패턴을 구현한다. 여러가지 이유로
Thread 보다는 Threading 모듈을 사용하길 추천한다.
따라서 이 글에서는 Threading 과 Queue 에 대해서 알아본다.
파이썬에서 thread 는 기본적으로 daemon 속성이 False 인데, 메인 쓰레드가
종료되도 자신의 작업이 끝날 때까지 계속 실행된다. 부모가 종료되면 즉시
끝나게 하려면 True 를 해줘야한다. 데몬속성은 반드시 start 이전에 호출해야 한다.

Threading
Threading 모듈은 아래와 같은 객체들을 가지고 있다.
-------------------------------------------------------------------------------
객체                  설명
-------------------------------------------------------------------------------
Thread              단일 실행 쓰레드를 만드는 객체
Lock                기본적인 락 객체
RLock               재진입 가능한 락객체. 이미 획득한 락을 다시 획득 할 수 있다.
Condition           다른 쓰레드에서 신호를 줄 때까지 기다릴 수 있는 컨디션 객체
Event               컨디션 변수의 일반화 버전.
Semaphore           정해놓은 갯수만큼의 쓰레드를 허용하는 동기화 객체.
BoundedSemaphore    초기 설정된 값 이상으로 증가 될 수 없게 재한한 Semaphore
Timer               Thread 와 비슷하지마 실행되기 전에 지정된 시간 동안 대기
Barrier             쓰레드들이 계속 진행 할 수 있으려면 지정된 숫자의 쓰레드가
                    해당 지점까지 도달해야하게 만듬
                    (파이썬 3.2에서 처음 소개됨)
-------------------------------------------------------------------------------
'''
import threading
from time import sleep, ctime

loops = [8,2]

def loop(nloop, nsec):
    print('start loop', nloop, 'at:',ctime())
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

if  __name__ == '__main__' :
   test()