'''조건문: 괄호와 중괄호 없음

if 조건:
    print('asdf')
    print('asdf')
    print('asdf')

print('asdf')
'''
import sys

'''
a=10
if a>5:
    print('5보다 큼')
else:
    print('5보다 크지않음')

print('asdfgs')
'''

'''
#짝수 홀수 구분 과제
num=2
if num%2 == 0:
    print('짝수')
else:
    print('홀수')
'''

'''
if 조건:
    실행문
elif 조건:
    실행문
elif 조건:
    실행문
else
    실행문


#성적과제
score = 80
if score > 100 or score < 0:
    sys.exit(0) #프로그램종료

if score >= 90:
    print('A')
elif score >= 80:
    print(' B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
'''
# 반복문
'''
for i in [1,2,3]:
    print(i)


for i in range(0, 10): #0, 1, 2, 3, 4...9 / range(시작숫자, 마지막숫자-1, 간격(default=1))
    print(i)

for i in '가나다라마바':
    print(i)

# 구구단 5단
for i in range(1, 10):
    print('5 x', i, '=', i*5)

dan = 5
for i in range(1, 10):
    print(dan, '*', i, '=', (dan*i))
'''

'''
while 조건:
    실행문
'''

# i=5
# while i>0:
#     print(i)
#     i-=1

'''
<형변환함수>
int('123')
float(12)=> 12.0
float('23.456') -> 23.456
str(12)-> '12'
'''
'''
while True:
    flag = input('멈추려면 0입력') #입력함수, 기본으로 문자열로 입력받음
    if flag == '0':
        break   #루프 빠져나감

    num = int(input('숫자를 입력하라'))
    print('입력한 숫자:', num)
'''


for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i, end=', ') #end: 마지막 출력값, 기본값은 \n.

#컨티뉴는 컨티뉴 아래문장 실행안하고 다시 조건문끝날때까지 돌음

print()
for i in range(2, 11, 2):
    print(i, end=', ')

