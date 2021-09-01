class PocketMon:    #하위 클래스에 상속을 목적으로 만든 클래스
    def __init__(self, hp, exp, level, name):
        self.hp = hp
        self.exp = exp
        self.level = level
        self.name = name
        print(self.name,'캐릭터 생성됨')

    def eat(self):
        print(self.name, '밥먹음')

    def sleep(self):
        print(self.name, '잠잔다')

    def play(self):
        print(self.name, '논다')

    def exc(self):
        print(self.name, '운동함')

    def levelUpCheck(self):
        print(self.name, '레벨업 체크')

    def printState(self):
        print(self.name, '상태확인')
        print('hp', self.hp)
        print('exp', self.exp)
        print('level', self.level)

class Picachu(PocketMon):
    def __init__(self):
        super().__init__(hp=30, exp=0, level=1, name='피카추')

    def eat(self):
        super().eat()
        self.hp += 5

    def sleep(self):
        super().sleep()
        self.hp += 10

    def play(self):
        super().play()
        self.hp -= 8
        if self.hp > 0:
            self.exp += 5
            self.levelUpCheck()
            return True
        else:
            print(self.name, '가 사망함')
        return False

    def exc(self):
        super().exc()
        self.hp -= 13
        if self.hp > 0:
            self.exp += 8
            self.levelUpCheck()
            return True
        else:
            print(self.name, '가 사망함')
        return False

    def levelUpCheck(self):
        super().levelUpCheck()
        if self.exp > 20:
            self.level += 1
            self.exp -= 20
            print(self.name, '레벨 1증가')

    def 백만볼트(self):
        print('삐까삐까')

class gobook(PocketMon):
    def __init__(self):
        super().__init__(hp=35, exp=0, level=1, name='꼬부기')

    def eat(self):
        super().eat()
        self.hp += 8

    def sleep(self):
        super().sleep()
        self.hp += 13

    def play(self):
        super().play()
        self.hp -= 10
        if self.hp > 0:
            self.exp += 8
            self.levelUpCheck()
            return True
        else:
            print(self.name, '가 사망함')
        return False

    def exc(self):
        super().exc()
        self.hp -= 16
        if self.hp > 0:
            self.exp += 12
            self.levelUpCheck()
            return True
        else:
            print(self.name, '가 사망함')
        return False

    def levelUpCheck(self):
        super().levelUpCheck()
        if self.exp > 20:
            self.level += 1
            self.exp -= 20
            print(self.name, '레벨 1증가')

    def 물대포(self):
        print('물대포 발사')

class isanghae(PocketMon):
    def __init__(self):
        super().__init__(hp=40, exp=0, level=1, name='이상해씨')

    def eat(self):
        super().eat()
        self.hp += 15

    def sleep(self):
        super().sleep()
        self.hp += 19

    def play(self):
        super().play()
        self.hp -= 20
        if self.hp > 0:
            self.exp += 18
            self.levelUpCheck()
            return True
        else:
            print(self.name, '가 사망함')
        return False

    def exc(self):
        super().exc()
        self.hp -= 22
        if self.hp > 0:
            self.exp += 16
            self.levelUpCheck()
            return True
        else:
            print(self.name, '가 사망함')
        return False

    def levelUpCheck(self):
        super().levelUpCheck()
        if self.exp > 20:
            self.level += 1
            self.exp -= 20
            print(self.name, '레벨 1증가')

    def 넝쿨공격(self):
        print('넝쿨넝쿨')

class Menu:
    def __init__(self, ch):
        self.ch = ch

    def run(self):
        flag = True
        while flag:
            menu = int(input('1.밥먹기 2.잠자기 3.놀기 4.운동하기 5.상태확인 6.종료 7.특기공격'))
            if menu == 1:
                self.ch.eat()
            elif menu == 2:
                self.ch.sleep()
            elif menu == 3:
                self.ch.play()
            elif menu == 4:
                self.ch.exc()
            elif menu == 5:
                self.ch.printState()
            elif menu == 6:
                break
            elif menu ==7:
                if isinstance(self.ch, Picachu):    #isinstance: 타입비교함수, 첫 파람의 타입이 두 번째 파람과 같으면 True, 아니면 False
                    self.ch.백만볼트()
                elif isinstance(self.ch, gobook):
                    self.ch.물대포()
                elif isinstance(self.ch, isanghae):
                    self.ch.넝쿨공격()

if __name__ == '__main__':
    sel = input('캐릭터를 선택하시오\n1.피카추(기본) 2.꼬부기 3.이상해씨')
    if sel == '2':
        ch = gobook()
    elif sel == '3':
        ch = isanghae()
    else:
        ch = Picachu()

    mm = Menu(ch)
    mm.run()
    print('게임종료')