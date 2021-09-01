###딕셔너리#####
# 키와 값 같이 저장
# 키는 중복, 변경 안됨. 키의 타입은 숫자, 문자열, 튜플만 가능
# 값은 중복, 변경 허용. 값의 타입은 제약 없음

#########################
# 생성
d1 = {'name':'aaa', 'age':23, 'dept':'eng'}
print(d1)
print(type(d1))

d2 = {1:'aaa', 2:'bbb', 3:'ccc'}
print(d2)
print(type(d2))

d3 = {(1,2):255, (3,4):23}
print(d3)
print(type(d3))

# 빈 딕셔너리 생성
d4 = {}
print(d4)
print(type(d4))

d5 = {}
print(d5)
print(type(d5))

########################
# 요소 접근
print('name', d1['name'])
print('age', d1['age'])
print('dept', d1['dept'])

# 키 이름 모를 때
for key in d1:
    print(key, ':', d1[key])

#튜플형태로 키와 값 쌍으로 가져오고 싶다면
print(d1.items())

# 요소 추가: 새 키 이름으로 항목 추가
d1['new1'] = 'asdfasd'
d1['new2'] = 'sdfwer'

for key in d1:
    print(key, ':', d1[key])

# 요소 수정: 수정하려는 키이름으로 새 값 할당
d1['name'] = 'bbb'
d1['age'] = '32'

for key in d1:
    print(key, ': ', d1[key])

#요소 삭제
del d1['new1']
print(d1)

d1.pop('new2')  # 키 이름으로 삭제
print(d1)

d1.popitem()    #임의의 항목 삭제
print(d1)

# 전체 항목 삭제
d1.clear()
print(d1)

# 이름 삭제
del d1
#print(d1) => d1은 삭제 되었으므로 에러