#1. 요구인자: 함수 호출시 아규먼트의 개수와 순서가 맞아야함
def f1(name, tel, age):
    print('name:', name)
    print('tel:', tel)
    print('10년 후 age:', age+10)

f1('aaa', '111', 12)

#2. 키워드인자: 각 아규먼트가 어느 파라메터로 전달될지 지정하므로 순서 바뀌어도 됨
def f2(name, tel, age):
    print('name:', name)
    print('tel:', tel)
    print('10년 후 age:', age+10)

#f2('111', 12, 'aaa'): 아규먼트의 순서가 안맞아서 에러
f2(tel='111', age=12, name='aaa')

#3. 디폴트 인자: 아규먼트의 기본 값을 지정하므로 함수 호출시 생략가능함
def f3(name='aaa', tel='1234', age=10):
    print('name:', name)
    print('tel:', tel)
    print('10년 후 age:', age+10)

f3('bbb')
f3('ccc', 12)
f3(age=22)

def f4(name, tel='1234', age=10):#정상. 디폴트값이 없는 파라메터가 앞에 있어야 함
    print('name:', name)
    print('tel:', tel)
    print('10년 후 age:', age+10)

f4('asdf')
f4('qwer', '111')
f4('sdfg', '222', 23)

#def f5(name='aaa', tel, age):=>에러
#    print('name:', name)
#    print('tel:', tel)
#    print('10년 후 age:', age+10)

#4. 가변인자: 아규먼트의 개수가 가변. 튜플형태로 전달됨
def f6(*param):#가변인자. 튜플로 받아옴. param: ('aaa','bbb'...)
    print('함수시작')
    for i in param:
        print(i)
    print('함수끝')

f6()
f6('aaa')
f6('aaa', 'bbb', 'ccc')

def my_sum(*nums):#nums: (1,2,3)
    res = 0
    for i in nums:
        res += i
    return res

print('파라메터 없음:', my_sum())
print('1,2,3:', my_sum(1,2,3))
print('1,2,3,4,5:', my_sum(1,2,3,4,5))

def memInfo(num, name, kor, eng, math):
    print('num:', num)
    print('name:', name)
    print('total:', kor+eng+math)

data = [1, 'aaa', 65,46,54]
memInfo(*data)