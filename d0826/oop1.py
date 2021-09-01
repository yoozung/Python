'''
객체 지향 프로그래밍(중, 대형 프로젝트 수행할 때 객체 지향 프로그래밍이 적합함.)
순차적 프로그래밍은 시간의 흐름 순서대로 코드를 짰다면,
객체 지향 프로그래밍은 객체를 중심으로 개발하는 것.
객체를 정의하고 객체와 객체 사이의 관계를 정의하는 방식으로 프로그래밍 한다.

객체: 세상을 프로그램으로 모델링 할 때 모델링의 대상이 되는 사람이나 사물, 개념, 즉 샘플.

기능정의
입금, 출금, 조회, 이체

기능명세
출금 기능 명세
카드를 넣는다 -> 카드 비밀번호입력 -> 출금금액입력 -> 카드 연결 계좌 조회(잔액여부)  -> (yes) -> 기기지페확인 -> 계좌 출금
                                                                         -> (no)  -> 메시지 출력 -> 메인

객체 샘플 도출 => 클래스 정의 및 클래스 관계 정의(클래스 다이어그램)

클래스: 설계상에서 도출된 객체 샘플링을 통해 정리된 속성과 기능을 정의

클래스의 구성: 속성(값)과 메서드(기능)


카드
--------------------
카드번호(str)
카드비밀번호(int)
유효기간(date)
계좌(obj)
--------------------
print()

----------<디폴트생성자>--------------------
class Card:
    def __init__(self): #생성자
        self.number = ''
        self.pwd = ''
        self.date = ''
        self.account = None

    def printInfo(self): #메서드
        print(self.number)
        print(self.pwd)
        print(self.date)
        print(self.account)

c1 = Card()
c1.number = '123-345-4564'
c1.pwd = '1234'
c1.date = '03/24'
c1.account = '3532215'

c1.printInfo()
'''

#####################파람 있는 생성자######################
class Card:
    def __init__(self, number, pwd, date, account): #생성자
        self.number = number
        self.pwd = pwd
        self.date = date
        self.account = account

    def printInfo(self): #메서드
        print(self.number)
        print(self.pwd)
        print(self.date)
        print(self.account)

c1 = Card('123-345-4564', '1234', '03/24', '3532215')
c1.printInfo()

#################<생성자 파람 디폴트>#######################
class Card:
    def __init__(self, number='', pwd=None, date=None, account=None): #생성자
        self.number = number
        self.pwd = pwd
        self.date = date
        self.account = account

    def printInfo(self): #메서드
        print(self.number)
        print(self.pwd)
        print(self.date)
        print(self.account)

c1 = Card(number='123-345-4564')
c1.printInfo()
print(c1)

c2 = Card(number='123-345-4564', pwd='56745')
c2.printInfo()
print(c2)