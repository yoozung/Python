'''
<예외 발생 하기>
1. 예외 클래스 만들 수 있음. 파이썬에 정의되지 않은 예외 클래스 쓰고 싶을 때 직접 만들어서 사용.
class 예외클래스명(Exception):    <--- 이게 상속받는 문법임
def __init__(self, msg): #생성자. 객체 초기화 함수. 사용할 에러 메시지 할당
self.msg = msg

2. 예외 발생 시킴 => 파이썬이 인지하지 못하는 예외를 직접 발생시키고 싶을때 사용
raise 예외객체 생성
raise TypeError('에러 메시지')

3. 함수에서 예외가 발생하면 먼저 그 함수 안에서 예외처리 코드를 찾고 있으면 그것을 실행
없으면 이 함수를 호출한 위치에서 예외처리 구문을 또 찾음 (스택언롤링)
있으면 그 예외처리 구문을 실행하고 없으면 프로그램이 중단됨
'''

class NumError(Exception):
    def __init__(self, msg):
        self.msg = msg

def f1(num):
    if num>5:
        raise NumError('5를 넘으면 안됨') #예외발생

    print('num:', num)

def f2(num):
    print('f2() 시작')
    f1(num)
    print('f2() 끝')

def f3(num):
    print('f3() 시작')
    f2(num)
    print('f3() 끝')

try:
    f3(4)
    f3(8)
except NumError as e:
    print(e)