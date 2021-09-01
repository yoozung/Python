import copy
#vo, dao, service
class Product:  #한개의 제품 정보 담는 클래스
    cnt = 0     #클래스 변수. 등록된 제퓸 갯수 카운팅
    def __init__(self, num=None, name=None, price=None, amount=None):
        if num == None: #등록용 vo
            Product.cnt += 1    #새번호 발급
            self.__num = Product.cnt    #프라이빗멤버 표현 : __이름
        else:   # 검색, 수정용 vo
            self.__num = num

        self.__name = name
        self.__price = price
        self.__amount = amount

    def __str__(self):  #자바의 toString()
        return 'num: ' + str(self.__num) + ' / name: ' + self.__name + ' / price: ' + str(self.__price) + ' / amount: ' + str(self.__amount)

    def setNum(self, num):
        self.__num = num

    def getNum(self):
        return self.__num

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setPrice(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price

    def setAmount(self, amount):
        self.__amount = amount

    def getAmount(self):
        return self.__amount

class Dao:
    def __init__(self):
        self.__prods = []   #제품 저장소. 제품 여러개를 담을 테이블과 동일

    def insert(self, p):
        self.__prods.append(p)

    def selectByNum(self, num): #번호로 검색. 만약 같은 번호가 없다면 아무것도 반환 안 함. 파이썬의 함수는 아무값도 반환 안하면 자동으로 None 상수를 반환
        for p in self.__prods:
            if p.getNum() == num:
                return p

    def selectByName(self, name):   #이름으로 검색. 제품명은 중복허용. 이름으로 검색하면 결과가 여러개 나올 수 있음
        arr = []  #검색 결과를 담을 리스트
        for p in self.__prods:
            if p.getName() == name:
                arr.append(p)

        if len(arr) == 0:  #arr의 길이가 0이면 동일한 이름의 제품이 하나도 없는 것
            return None
        else:
            return arr

    def selectAll(self):
        arr = copy.deepcopy(self.__prods)
        return arr

    def update(self, p):
        pp = self.selectByNum(p.getNum())   #수정할 제품 번호로 검색
        if pp == None:
            return False
        else:
            name = p.getName()
            price = p.getPrice()
            amount = p.getAmount()

            if name != None:
                pp.setName(name)

            if price != None:
                pp.setPrice(price)

            if amount != None:
                pp.setAmount(amount)

            return True

    def delete(self, num):
        p = self.selectByNum(num)
        if p == None:
            return False
        else:
            self.__prods.remove(p)
            return True

class Service:  #비즈니스 로직. 외부에 제공할 기능구현
    def __init__(self):
        self.__dao = Dao()

    def addProduct(self):
        print('==== 제품등록 ===')
        name = input('name: ')
        price = int(input('price: '))
        amount = int(input('amount: '))
        self.__dao.insert(Product(name=name, price=price, amount=amount))

    def getProductByNum(self, num=None):
        if num == None:
            print('==== 제품 번호로 검색 ===')
            num = int(input('검색할 제품 번호: '))
        p = self.__dao.selectByNum(num)
        if p == None:
            print('없는 제품 번호')
        else:
            print(p)
        return p

    def getProductByName(self):
        print('==== 제품 이름으로 검색 ===')
        name = input('검색할 제품 name: ')
        p = self.__dao.selectByName(name)
        if p == None:
            print('없는 제품 이름')
        else:
            for x in p:
                print(x)

    def editProduct(self):
        print('==== 제품 수정 ===')
        num = int(input('수정할 제품 번호: '))
        p = self.__dao.selectByNum(num)
        if p == None:
            print('없는 제품 번호')
        else:
            print('수정 전 제품 정보')
            print(p)
            name = input('new name(수정안하려면 엔터)')
            if name == '':
                name = None

            price = int(input('new price(수정안하려면 0)'))
            if price == 0:
                price = None

            amount = int(input('new amount(수정안하려면 0)'))
            if amount == 0:
                amount = None

            flag = self.__dao.update(Product(num=num, name=name, price=price, amount=amount))

            if flag:
                print('수정 완료')
            else:
                print('수정 취소')

    def delProduct(self):
        print('==== 제품 삭제 ===')
        num = int(input('삭제할 제품 번호: '))
        flag = self.__dao.delete(num)
        if flag:
            print('삭제 완료')
        else:
            print('삭제 취소')

    def printAll(self):
        a = self.__dao.selectAll()
        for p in a:
            print(p)