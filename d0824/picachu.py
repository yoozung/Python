name = ''
hp = 0
exp = 0
lv = 1

#각 캐릭터 활동정보
datas = {'picachu':{'eat':5, 'sleep':10, 'play':(-10, 8), 'exc':(-15, 10), 'lv_exp': 30},
         'gobbok': {'eat':3, 'sleep':5, 'play':(-6, 5), 'exc':(-9, 7), 'lv_exp': 20},
         'leesanghae': {'eat':15, 'sleep':20, 'play':(-30, 15), 'exc':(-40, 30), 'lv_exp': 60}}

def eat():
    global hp
    print(name, '밥먹음')
    hp += datas[name]['eat']

def sleep():
    global hp
    print(name, '잠잠')
    hp += datas[name]['sleep']

def play(): #반환값 트루는 캐릭터 살았음. 펄스는 죽었음을 나타냄
    global hp, exp
    print(name, '논다')
    h, e = datas[name]['play']
    hp += h
    if hp <= 0:
        return False
    else:
        exp += e
        levelUp()
        return True

def exc():
    global hp, exp
    print(name, '운동함')
    h, e = datas[name]['exc']
    hp += h
    if hp <= 0:
        return False
    else:
        exp += e
        levelUp()
        return True

def levelUp():
    global lv, exp
    lu = datas[name]['lv_exp'] #현재 캐릭터의 레벨업 기준 수치
    if exp >= lu:
        lv += 1
        exp -= lu
        print(name, '레벨 1 증가: 현재 레벨 ', lv)

def printInfo():
    print(name, '의 정보 hp: ', hp, 'exp:', exp, 'lv: ', lv)

def menu():
    flag = True
    while flag:
        mm = input('1.밥먹기 2.잠자기 3.놀기 4.운동하기 5.정보확인 6.종료')
        if mm == '1':
            eat()
        elif mm == '2':
            sleep()
        elif mm == '3':
            flag = play()
            if not flag:
                print('캐릭터 사망')
        elif mm == '4':
            flag = exc()
            if not flag:
                print('캐릭터 사망')
        elif mm == '5':
            printInfo()
        elif mm == '6':
            break


if __name__ == '__main__':
    ch = input('캐릭터를 선택하세요. 1. 피카추(기본) 2.꼬부기 3. 이상해씨')

    if ch == '2':
        name = 'gobook'
        hp = 20
    elif ch == '3':
        name = 'leesanghae'
        hp = 10
    else:
        name = 'picachu'
        hp = 30

    menu()

    print('게임 종료')
