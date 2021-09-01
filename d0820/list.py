'''
리스트: 배열, 집합 데이터 편하게 사용
변수정의: 값을 저장하기 위해 메모리를 할당받음
1. 리스트생성
a = [1,2,3]
b = list(a)
c = list([4,5,6])
d = list()

2. 요소에 접근
a = [1,2,3]
a[0]
a[1]
a[2]

for i in range(0, len(a)):
    print(a[1])

for i in a:
    print(i)


a = [1,2,3,4,5]
for i in a:
    print(i)

# 하나의 리스트에 여러 타입의 값 저장 가능
b = [1,2.234, 'asdf', True]
for i in b:
    print(i)

c = list(range(1, 6))
print(c)


#요소 추가
a = [1,2,3]
#a[3] = 4 이렇게하면 에러
print(len(a))
print(a)
a.append(4)
print(len(a))
print(a)

#요소 수정
a[0] = 123
a[1] = 456
print(a)

#요소 삭제
del a[0]    #방번호로 삭제
print(len(a))
print(a)

a.remove(3)   #요소 값으로 삭제
print(a)

# a.remove(3)   #없는 값 삭제시 에러
# print(a)

# 전체삭제
a.clear()
print(a)

# 정수타입으로 캐스팅해서 input으로 숫자 열개입력받고 배열에 담기
# 리스트에서 최대값 최소값 출력

a = []
for i in range(1, 11):
    num = int(input('입력 : '))
    a.append(num)
print(a)

#_max: 가장 큰 값 담을 변수
#_min: 가장 작은 값 담을 변수
_max = _min = a[0]

for idx, i in enumerate(a):
    if _max < i:
        _max = i
        max_idx = idx

    if _min > i:
        _min = i
        min_idx = idx

print('max:', _max, ' / max_idx: ', max_idx)
print('min:', _min, ' / min_idx: ', min_idx)


# 요소 검색
in : 멤버 연산자. 왼쪽의 값이 오른쪽 리스트의 요소인지 True, False로 반환
'''
a = [1,2,3,4,5]
print(3 in a)
print(8 in a)

if 3 in a:
    print('3은 리스트 a의 멤버가 맞다')
    print(a.index(3), '번재 방에 있음')
    #print(a.index(7)) -> 없는 값은 에러

b = [7,3,9,4,6]
b.sort()    #sort는 오름차순으로 정렬
print(b)

b.sort(reverse=True)    #sort에 reverse 속성쓰면 내림차순으로 정렬
print(b)

##############################################################
#           2차원 리스트

a = [[1,2], [4,5,6]]
for i in a:
    for j in i: #[1,2,3]
        print(j, end=', ')
    print()

for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        print(a[i][j], end=', ')
    print()

b =[['aaa', 1, True, 34.567], [23, False]]

'''
숙제
3학생의 이름, 번호, 국, 영, 수 점수를 입력 받아서 각 학생의 총점, 평균을 계산하여 결과를 출력
이름 번호 국  영  수  총점  평균
aaa  1   65  45 45  546  56.6
bbb  1   65  45 45  546  56.6
ccc  1   65  45 45  546  56.6
'''
list = [[],[], []]
titles = ['name', 'num', 'kor', 'eng', 'mat', 'total', 'avg']
for i in range(0, len(list)):
    add = input('이름 : ')
    list[i].append(add)
    add = input('번호 : ')
    list[i].append(add)
    add = input('국어점수 : ')
    list[i].append(add)
    add = input('영어점수 : ')
    list[i].append(add)
    add = input('수학점수 : ')
    list[i].append(add)

    total = int(list[i][2]) + int(list[i][3]) + int(list[i][4])
    list[i].append(total)
    avg = int(total/3)
    list[i].append(avg)

print('  이름    번호   국어   영어   수학   총점   평균')
print(titles)
for i in range(0, len(list)):
    print(list[i])

