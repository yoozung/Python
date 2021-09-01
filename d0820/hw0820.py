'''
숙제
3학생의 이름, 번호, 국, 영, 수 점수를 입력 받아서 각 학생의 총점, 평균을 계산하여 결과를 출력
이름 번호 국  영  수  총점  평균
aaa  1   65  45 45  546  56.6
bbb  1   65  45 45  546  56.6
ccc  1   65  45 45  546  56.6
'''

list = [[],[], []]
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
for i in range(0, len(list)):
    print(list[i])