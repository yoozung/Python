'''
함수 정의
    함수가 어떤 동작, 이 때 필요한 값이 어떤 거고, 어떻게 받을 지 정의

    def 함수명(param1, param2):
        실행문
        return 결과값

함수 호출
    함수의 이름을 불러서 함수를 실행. 이때 파라메터가 있다면 값 전달(아규먼트)

    res = 함수명(10, 20)
'''

#함수정의
def hello(name):
    print('hello ', name)

#함수호출
hello('aaa')
hello(10)
hello(3.14)

#함수정의
def add(num1, num2):
    return num1+num2

#함수호출
print(add(1, 2))
print(add('1', '2'))
# print(add(1, '2'))

# 구구단 함수

def gugudan(dan):
    print(dan,'단')
    for i in range(1, 10):
        print(dan, ' * ', i, ' = ', dan*i)
    print()

for i in range(2, 10):
    gugudan(i)

###########################################
# 함수 밖에 정의하고 모든 함수들이 사용할 수 있는 변수: 전역변수
nums = []
def add_num(num): #nums에 항목 추가
    nums.append(num)

def print_nums(): #nums의 모든 요소 출력
    for i in nums:
        print(i, end=', ')
    print()

def edit_num(idx, num):
    nums[idx] = num

def del_num(idx):
    del nums[idx]

for i in range(1, 6):
    add_num(i)

print_nums()

edit_num(2, 30)

print_nums()

del_num(2)

print_nums()
