'''
집합 데이터 관련 api

1. list
[1,2,3]=> 값만 저장
리스트 자체는 변경 가능(요소 추가 삭제 가능)
요소 자체 변경 가능

2. set: 집합. 중복허용안함. 순서없음. 변경가능. 요소는 변경 불가
{1,2,3}

3. tuple: 자체 변경불가, 요소도 변경불가(우회적으로 변경 가능한 방법 있다.)
(1,2,3). (1.) <- 하나만 넣을때는 뒤에 꼭 . 붙이기!
함수의 리턴값이 여러개일 경우 튜플 많이 사용
함수의 파라메터나 리턴값을 주고 받을 때 값 변경 원하지 않을때 활용

4. directory
: 자체 변경 가능, 키는 중복, 변경안됨(숫자, 문자열, 튜플만 키로 사용 가능),
값은 중복 허용 변경가능
{'키':'값', '키':'값'}
'''

###튜플###
#튜플 자체도 변경불가, 요소도 변경 불가 / 하지만 요소를 리스트로 하면 우회적으로 변경 가능
#고정된 집합으로 요소를 추가 변경 삭제 안됨
#값의 순서(인덱스)기 있음. 그래서 방번호로 접근 가능
#활용: 함수와 값 주고 받을 때 값 변경을 허용하지 않을 경우 사용

'''
b = [1,2,3]
l = list[] #빈 리스트 l=[]
t1 = [0]*7
'''

a = (1,2,3,4,5)
print(a)

t = tuple() #빈 튜플

t1 = (1,)*3
print(t1)

t2 = ('hello',)*5
print(t2)

x = (1, 2.345, 'adg', True, [1,2,3])
print(x)
print(type(x))

for i in a:
    print(i)

for i in range(len(a)):
    print(a[i])

for i in range(-5, 0):
    print(a[i])

'''
b = ((1,2,3), {3,4,5})

for i in b:
    for j in i:
        print(j)
'''

###############################
#요소 슬라이싱 : 잘라온다고 해서 원본에 영향을 주진 않음.
a = [1,2,3,4,5]     #리스트
b = (6,7,8,9,10)    #튜플
r1 = a[0:3]         #a의 요소 0~2
print(r1)
r2 = b[2:5]         #b의 요소 2~$
print(r2)

#len(): 길이
#sum(): 리스트나 튜플 요소의 합
#max(): 최대값
#min(): 최소값
a_len = len(a)
print(a_len)

b_len = len(b)
print(b_len)

s1 = sum(a)
s2 = sum(b)
print(s1, '/', s2)

max_a = max(a)
max_b = max(b)
print(max_a, '/', max_b)

#################################
#검색, 비교
#in: 멤버쉽 연산자. 집합에 비교하는 값이 있나 없나를 True, False로 반환
print(3 in a)
print(13 in a)

print(3 not in a)
print(13 not in a)

print(3 in b)
print(8 in b)

c = (11,12,13)
x = b + c
print(x)

#x, y, z = 1,2,3 => int 변수 3개 만들어짐
t1 = 1,2,3
t2 = 3,4,5
t3 = 1,2,3

print(t1)
print(type(t1))

print(t2)
print(type(t2))

print(t3)
print(type(t3))

print(t1==t2)
print(t1==t3)

print(t1!=t2)
print(t1!=t3)

##############################
#요소 추가, 삭제, 변경 안됨
a = (1,2,3,[])      #리스트는 mutable요소이므로 변경 가능
#a[0]=4 => 에러발생, 튜플은 요소에 =(대입연산자)를 사용할 수 없음
a[3].append(10)
a[3].append(20)
print(a)
a[3][0]=150
print(a)
del a[3][0]
print(a)

