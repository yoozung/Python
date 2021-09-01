#함수 정의
def my_input():
    name = input('name')
    age = int(input('age:'))
    dept = input('dept:')
    return name, age, dept

if __name__ == '__main__':      #프로그램의 시작점(main()함수)
    data = my_input()           #함수 호출 / data = name, age, dept
    print('name:', data[0])
    print('age:', data[1])
    print('dept:', data[2])

    name, age, dept = my_input()
    print('name:', name)
    print('age:', age)
    print('dept:', dept)

    name, age, _ = my_input()       #dept가 필요없으면 _로 이름. 그냥 비게 두면 오류남
    print('name:', name)
    print('age:', age)

