###set(셋)#########
#집합. 인덱스 없음.
# 요소의 중복허용 안함
# 요소를 추가, 삭제 가능
# 요소 자체는 변경 불가
# 요소는 immutable
# 인덱스 없음

s1 = {1,2,3}
print(s1)
#s2 = {1,2,[3,4]} => 에러
s2 = set()      #빈 셋
s3 = {}         # 빈 딕셔너리
print(type(s2))
print(type(s3))
s3 = {'aaa', 'ccc', 'bbb'}
print(s3)
print(type(s3))

s4 = {1, 'asdf', (3,4)}
print(s4)
print(type(s4))

list1 = [1,2,3,4,5]
s5 = set(list1)
print(s5)
print(type(s5))

ch = 'abcdefghij'
s6 = set(ch)
print(s6)
print(type(s6))

#####################
#요소 추가
a={1,2,3}
a.add(4)
print(a)
a.add(3)
print(a)

#요소 여러개 추가
a.update([5,6,7])
print(a)

#########################
#검색
print(3 in a)
print(13 in a)

print(len(a))
print(max(a))
print(min(a))
print(sum(a))

##########################
#삭제
a.remove(3)
print(a)
#a.remove(3) #없는 값 삭제시 에러
#print(a)

a.discard(5)
print(a)
a.discard(5) #없는 값 삭제시 무시(에러안남)
print(a)

a.pop() #끝 요소 하나 삭제
print(a)

#전체삭제
a.clear()   # => 빈 셋
print(a)

#변수 자체를 삭제
#del a #a 자체가 없어짐
#print(a)

###############################
# 집합연산
s1 = {1,2,3,4,5}
s2 = {4,5,6}

# 합집합
s3 = s1 | s2
print('s1 합집합 s2:', s3)
s4 = s1.union(s2)
print('s1 합집합 s2:', s4)

#교집합
s5 = s1 & s2
print('s1 교집합 s2:', s5)
s6 = s1.intersection(s2)
print('s1 교집합 s2:', s6)

#차집합
s7 = s1 - s2
print('s1 차집합 s2:', s7)
s8 = s1.difference(s2)
print('s1 차집합 s2:', s8)

#대칭차집합(합집합-교집합)
s9 = s1.symmetric_difference(s2)
print('s1 대칭차집합 s2:', s9)

################################
# 포함관계 확인
a = {1,2,3,4,5}
b = {4,2}

print(b.issubset(a))    #b가 a의 하위집합이면 True, 아니면 False
print(a.issuperset(b))  #a가 b의 상위집합이면 True, 아니면 False