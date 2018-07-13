'''
Multiprocessing
-------------------------------------------------------------------------------
멀티 프로세싱 모듈은 Python 버전 2.6에 추가되었다.
원래 버전은 Jesse Noller와 Richard Oudkerk에 의해  PEP 371에서 정의되었다.
multiprocessing 모듈을 사용하면 스레딩 모듈로 스레드를 생성 할 수있는 것과
동일한 방식으로 프로세스를 생성 할 수 있다.
여기서 주요 포인트는 프로세스를 생성하기 때문에 GIL (Global Interpreter Lock)을
피하고 시스템의 여러 프로세서를 최대한 활용할 수 있다는 것이다.
multiprocessing  패키지에는 또한 스레딩 모듈에 없는 몇 가지 API가 포함되어 있다.
예를 들어 여러 입력에서 함수 실행을 병렬화하는 데 사용할 수있는 깔끔한
Pool 클래스가 있다. 우리는 이후 섹션에서 Pool을 볼 것이다.
먼저 multiprocessing   모듈의 Process 클래스부터 시작한다.
-------------------------------------------------------------------------------
'''
import os
from multiprocessing import Process

def doubler(number):
    result = number * 2
    proc = os.getpid()
    print('{0} doubled to {1} by process id: {2}'.format(number, result, proc))

if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []
    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()