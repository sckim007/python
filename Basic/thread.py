import threading
import time

'''
쓰레드 (Thread)
파이썬 프로그램은 기본적으로 하나의 쓰레드(Single Thread)에서 실행된다. 즉, 하나의 메인 쓰레드가 파이썬 코드를 
순차적으로 실행한다. 코드를 병렬로 실행하기 위해서는 별도의 쓰레드(Subthread)를 생성해야 하는데, 파이썬에서 
쓰레드를 생성하기 위해서는 threading 모듈 (High 레벨) 혹은 thread 모듈 (Low 레벨)을 사용할 수 있다. 
일반적으로 쓰레드 처리를 위해서는 thread 모듈 위에서 구현된 threading 모듈을 사용하고 있으며, 
thread 모듈은 (deprecate 되어) 거의 사용하고 있지 않다.

파이썬(오리지날 파이썬 구현인 CPython)은 전역 인터프리터 락킹(Global Interpreter Lock) 때문에 특정 시점에 하나의 
파이썬 코드만을 실행하게 되는데, 이 때문에 파이썬은 실제 다중 CPU 환경에서 동시에 여러 파이썬 코드를 병렬로 실행할 수 
없으며 인터리빙(Interleaving) 방식으로 코드를 분할하여 실행한다. 
다중 CPU 에서 병렬 실행을 위해서는 다중 프로세스를 이용하는 multiprocessing 모듈을 사용한다.

threading 모듈
파이썬에서 쓰레드를 실행하기 위해서는, threading 모듈의 threading.Thread() 함수를 호출하여 Thread 객체를 얻은 후 
Thread 객체의 start() 메서드를 호출하면 된다. 서브쓰레드는 함수 혹은 메서드를 실행하는데, 일반적인 구현방식으로 
(1) 쓰레드가 실행할 함수 혹은 메서드를 작성하거나 또는 
(2) threading.Thread 로부터 파생된 파생클래스를 작성하여 사용하는 방식 등이 있다.

먼저 첫번째 함수 및 메서드 실행 방식은 쓰레드가 실행할 함수 (혹은 메서드)를 작성하고 그 함수명을 hreading.Thread() 함수의 
target 아큐먼트에 지정하면 된다. 예를 들어, 아래 예제에서 sum 이라는 함수를 쓰레드가 실행하도록 threading.Thread() 함수의 
파라미터로 target=sum 을 지정하였다. 여기서 한가지 주의할 점은 target=sum() 처럼 지정하면, 이는 sum() 함수를 실행하여 
리턴한 결과를 target에 지정하는 것이므로 잘못된 결과를 초래할 수 있다. 
만약 쓰레드가 실행하는 함수(혹은 메서드)에 입력 파라미터를 전달해야 한다면, args (혹은 키워드 아규먼트인 경우 kwargs) 에 
필요한 파라미터를 지정하면 된다. args는 튜플로 파라미터를 전달하고, kwargs는 dict로 전달한다. 
아래 예제에서 sum() 함수는 두 개의 파라미터를 받아들이기 때문에 "args=(1, 100000)" 와 같이 입력파라미터를 지정하였다.
'''
'''
def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
        print("Subthread", total)
        time.sleep(1)

t = threading.Thread(target=sum, args=(1, 10))
t.start()

print("Main Thread")
str = input("exit")
'''

'''
threading.Thread 로부터 파생클래스를 만드는 방식은 Thread 클래스를 파생하여 쓰레드가 실행할 run() 메서드를 재정의해서
사용하는 방식이다. Thread 클래스에서 run() 메서드는 쓰레드가 실제 실행하는 메서드이며, start() 메서드는 내부적으로 이 
run() 메서드를 호출한다. 예를 들어, 아래 예제(A)는 getHtml() 라는 함수를 사용한 방식인데 
이를 예제(B)와 같이 파생클래스를 사용하는 방식으로 바꿔 쓸 수 있다. 예제(B)에서 t.start()는 HtmlGetter 클래스에서 
재정의된 run() 메서드를 호출하게 된다.
'''
'''
# 예제(A)
import threading, requests, time

def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')
    print(resp.text)

t1 = threading.Thread(target=getHtml, args=('http://google.com',))
t1.start()

print("### End ###")
'''

# 예제(B)
import threading, requests, time

class HtmlGetter(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), ' chars')
        print(resp.text)

t = HtmlGetter('http://google.com')
t.start()

print("### End ###")


'''
Thread 클래스에서 daemon 속성은 서브쓰레드가 데몬 쓰레드인지 아닌지를 지정하는 것인데, 데몬 쓰레드란 백그라운드에서
실행되는 쓰레드로 메인 쓰레드가 종료되면 즉시 종료되는 쓰레드이다. 반면 데몬 쓰레드가 아니면 해당 서브쓰레드는 
메인 쓰레드가 종료할 지라도 자신의 작업이 끝날 때까지 계속 실행된다.

아래 예제는 데몬 쓰레드를 예시하기 위한 것으로 Thread 객체의 daemon 속성을 True로 설정한 후 start() 하면, 해당 
서브쓰레드는 데몬 쓰레드가 되고 아래와 같이 메인 쓰레드가 곧바로 종료되면 getHtml 메서드를 마저 실행하지 못하고 
바로 데몬 쓰레드를 종료하게 된다. daemon 속성은 디폴트로 False 이므로 별도로 지정하지 않으면 메인 쓰레드가 종료되어도 
서브쓰레드는 끝까지 작업을 수행한다.
'''
'''
import threading, requests, time


def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')
    print(resp.text)


# 데몬 쓰레드
t1 = threading.Thread(target=getHtml, args=('http://google.com',))
#t1.daemon = True
t1.start()

print("### End ###")
'''