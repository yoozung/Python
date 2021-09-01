a = [1,2,3]
b = a   #얕은 복사
print(a)
print(b)

b[1]=20
print(a)
print(b)

print(id(a))
print(id(b))

####################################
import copy

a = [1,2,3]
b = copy.copy(a)    #깊은복사1

print(a)
print(b)

print(id(a))
print(id(b))

###################################
a = [1,2,[3,4]]
b = copy.copy(a)    #깊은복사1

print(a)
print(b)

print(id(a))
print(id(b))

b[2][0]=300
print(a)
print(b)

#####################################
a = [1,2,[3,4]]
b = copy.deepcopy(a)    #딥카피 : 참고값의 메모리도 다 복사해줌

print(a)
print(b)

print(id(a))
print(id(b))

b[2][0]=300
print(a)
print(b)