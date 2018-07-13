'''
The Pool Class
-------------------------------------------------------------------------------
Pool 클래스는 작업자 프로세스 풀을 나타내는 데 사용됩니다. 여기에는 작업을
작업 프로세스로 offload  할 수있는 방법이 있다.
-------------------------------------------------------------------------------
'''
from multiprocessing import Pool

def doubler(number):
    return number * 2

'''
기본적으로 여기서 발생하는 것은 Pool의 인스턴스를 만들고 세 개의 작업자 프로세스를
생성하도록 지시한다. 그런 다음 map 메소드를 사용하여 함수와 반복 가능한 것을 
각 프로세스에 매핑한다. 마지막으로 결과를 인쇄한다.
실행결과 : [10, 20, 40].

'''
'''
if __name__ == '__main__':
    numbers = [5, 10, 20]
    pool = Pool(processes=3)
    print(pool.map(doubler, numbers))
'''
'''
또한 apply_async 메소드를 사용하여 풀에서 프로세스의 결과를 얻을 수 있습니다.
'''
if __name__ == '__main__':
    pool = Pool(processes=3)
    result = pool.apply_async(doubler, (25,))
    print(result.get(timeout=1))