'''
<예외>
컴파일시 에러: 문법적 에러.
예외: 런타임시 문제 발생
<예외발생>
예외발생 => 파이썬 시스템이 예외 객체를 생성해서 던진다. => 프로그램이 예외객체를 맞으면 죽어.
<예외처리>
프로그램이 예외객체를 맞았을때 죽지않게 처리
파이썬에서 예외처리가 필수는 아니지만 프로그램의 안정성을 높이기 위해서 사용하는 것이 좋다




<예외처리 구문>
try - except 구문
try:
예외발생 예측
res = 3/0
except 예외명1 as x: #as x는 발생한 예외 객체를 변수 x에 저장
예외처리작성
except 예외명2:
예외처리작성
except Exception as e: #모든 예외 객체를 받음
예외처리작성
except: #예외가 발생했지만 위 except에서 잡지 못하면 여기로 온다
예외처리작성
else: #예외가 발생하지 않았을때 실행되는 블록
실행문
finally: #무조건 실행되는 블록
실행문

'''

print('start')
a=0
arr = []
try: #예외가 발생할만한 코드를 포함한 블록
    a=3/0
    print(a)
    b = '1'+2
    arr[0]=1
except ZeroDivisionError: #try블록에서 던진 예외 객체를 받는 블록. 지정한 예외 객체만 받음
    print('0으로 나눌 수 없다')
except TypeError as e: #try블록에서 던진 예외 객체를 받는 블록. 지정한 예외 객체만 받음
    print('피연산자들의 타입이 안맞음')
    #print(e.__str__())
    print(e)
except:    #except Exception as e:
    print('모든 에러')
else:
    print('예외없이 정상실행 됐을때 실행되는 블록')
finally:
    print('예외 발생 유무와 상관없이 무조건 실행') #자원 반환

print('end')