# 재귀함수: 함수 안에서 자신을 호출하는 함수.
# 보통 반복 연산에 많이 사용됨. 스택 사용량이 늘어나서 속도가 느리거나, 멈출 수 있다.
# 가능하면 루프나 리스트 등으로 대체하는 것이 좋다.

#팩토리얼
def fact(x):
    if x== 1:
        return 1
    else:
        return x*fact(x-1)

def fact2(x):
    res = 1
    for i in range(1, x+1):
        res *= i
    return res

res = fact(4)
print('fact(4): ', res)

res = fact(4)
print('fact2(4): ', res)


#피보나치
def fibo1(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fibo1(x-2)+fibo1(x-1)

for i in range(1, 101):
    print(fibo1(i), end=', ')
    if i%10 == 0:
        print()

def fibo2():
    x = y = 1

    for i in range(1, 101):
        if i < 3:
            z = 1
        else:
            z = x + y

        print(z, end =', ')
        x = y
        y = z

        if i % 10 == 0:
            print()

fibo2()

def fibo3(cnt): #수열 개수
    nums = [1]*cnt
    for i in range(2, len(nums)):
        nums[i] = nums[i-2] + nums[i-1]

    return nums

res = fibo3(100)
print(res)