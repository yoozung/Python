'''
포켓몬
피카추
hp=30
exp=0
lv=1

메뉴
1. 밥먹기 > 피카추 밥먹음. hp +
2. 잠자기 > 피카추 잠잠. hp +10
3. 운동하기 > 피카추 운동함. hp -15, exp +10
4. 놀기 > 피카추 놀음. hp -10, exp +5
5. 상태확인 > 정보출력
6. 종료

lv: exp 30마다 1 올라감
hp가 0 이하이면 캐릭터 사망 -> 게임자동종료
'''

# hp = 30
# exp = 0
# lv = 1
#
# while True:
#     flag = int(input('1.밥먹기 2.잠자기 3.운동하기 4.놀기 5.상태확인 6.종료'))
#     if flag == 1:
#         hp += 5
#         print('피카추 밥먹음')
#
#     elif flag == 2:
#         hp += 10
#         print('피카추 잠잠')
#
#     elif flag == 3:
#         hp -= 15
#         exp += 10
#         print('피카추 운동함')
#         if exp >= 30:
#             lv += 1
#             exp -= 30
#             print('lv 1증가')
#         if hp <= 0:
#             print('피카추죽음')
#
#
#     elif flag == 4:
#         hp -= 15
#         exp += 10
#         if exp >= 30:
#             lv += 1
#             exp -= 30
#             print('lv 1증가')
#         print('피카추 놀기')
#         if hp <= 0:
#             print('피카추죽음')
#
#
#     elif flag == 5:
#         print('상태확인')
#         print('hp: ', hp)
#         print('exp: ', exp)
#         print('lv: ', lv)
#         if hp <= 0:
#             print('피카추죽음')
#
#
#     elif flag == 6:
#         print('종료')
#         break

name = 'picachu'
hp = 30
exp = 0
lv = 1

while True:
    menu = int(input('1.밥먹기 2.잠자기 3.놀기 4.운동하기 5.정보확인 6.종료'))
    if menu == 1:
        print(name, '밥먹음')
        hp += 5
    elif menu == 2:
        print(name, '잠잠')
        hp += 10
    elif menu == 3:
        print(name, '놀기')
        hp -= 10
        if hp <= 0:
            print('캐릭터 사망')
            break
        exp += 5
        if exp >= 30:
            lv += 1
            exp -= 30
            print(name, '레벨 1증가함')
    elif menu == 4:
        print(name, '운동하기')
        hp -= 15
        if hp <= 0:
            print('캐릭터 사망')
            break
        exp += 10
        if exp >= 30:
            lv += 1
            exp -= 30
            print(name, '레벨 1증가함')
    elif menu == 5:
        print(name, '정보확인')
        print('hp:', hp)
        print('exp:', exp)
        print('lv:', lv)
    elif menu == 6:
        break

print('게임종료')