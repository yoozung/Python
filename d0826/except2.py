#예외 발생 구문
try:
    num = int(input('5이하 숫자를 입력하시오'))
    if num > 5:
        raise ValueError('value error') #예외 발생 Valueerror라는 객체를 생성하고 사용활 메세지를 생성자에 넣어중
    print('입력값: ', num)
except ValueError as e:
    print('5이하의 값만 입력')
    print(e)
print('stop')


