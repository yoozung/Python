import cx_Oracle

class Product:
    def __init__(self, num=None, name=None, price=None, amount=None):#생성자. 객체 멤버 변수 정의
        self.__num = num
        self.__name = name
        self.__price = price
        self.__amount = amount

    def __str__(self):#자바의 toString().
        return 'num:'+str(self.__num)+' / name:'+self.__name+' / price:'+str(self.__price)+' / amount:'+str(self.__amount)

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

class Dao:#db 작업 전담
    def __init__(self):
        self.conn = None    #커넥션 객체

    def connect(self):
        self.conn = cx_Oracle.connect("scott", "tiger", "localhost:1521/XE", encoding='utf-8')
        return self.conn.cursor()

    def insert(self, p):
        cursor = self.connect()
        sql = 'insert into product values(seq_product.nextval, :1, :2, :3)'
        d = (p.getName(), p.getPrice(), p.getAmount())
        cursor.execute(sql, d)
        self.conn.commit()
        self.conn.close()

    def selectByNum(self, num):
        cursor = self.connect()
        sql = 'select * from product where num=:1'
        d = (num,)
        cursor.execute(sql, d)
        row = cursor.fetchone()
        self.conn.close()
        if row is not None:
            return Product(row[0], row[1], row[2], row[3])

    def selectByName(self, name):
        res = []
        cursor = self.connect()
        sql = 'select * from product where name=:1'
        d = (name,)
        cursor.execute(sql, d)
        for row in cursor:
            res.append(Product(row[0], row[1], row[2], row[3]))
        self.conn.close()
        return res

    def selectAll(self):
        res = []
        cursor = self.connect()
        sql = 'select * from product'
        cursor.execute(sql)
        for row in cursor:
            res.append(Product(row[0], row[1], row[2], row[3]))
        self.conn.close()
        return res

    def update(self, p):
        cursor = self.connect()
        sql = 'update product set name=:1, price=:2, amount=:3 where num=:4'
        d = (p.getName(), p.getPrice(), p.getAmount(), p.getNum())
        cursor.execute(sql, d)
        self.conn.commit()
        self.conn.close()

    def delete(self, num):
        cursor = self.connect()
        sql = 'delete product where num=:1'
        d = (num,)
        cursor.execute(sql, d)
        self.conn.commit()
        self.conn.close()

class Service:#비즈니스 로직. 외부에 제공할 기능구현
    def __init__(self):
        self.__dao = Dao()

    def addProduct(self):
        print('=== 제품등록 ===')
        name = input('name:')
        price = int(input('price:'))
        amount = int(input('amount:'))
        self.__dao.insert(Product(name=name, price=price, amount=amount))

    def getProductByNum(self, num=None):#파람 num은 주문에서만 사용. 주문에서 선택한 제품번호를 파람으로 받음
        if num==None:
            print('=== 제품 번호로 검색 ===')
            num = int(input('검색할 제품 번호:'))
        p = self.__dao.selectByNum(num)
        if p==None:
            print('없는 제품 번호')
        else:
            print(p)
        return p

    def getProductByName(self):
        print('=== 제품 이름으로 검색 ===')
        name = input('검색할 제품 name:')
        p = self.__dao.selectByName(name)
        if p==None:
            print('없는 제품명')
        else:
            for x in p:
                print(x)

    def editProduct(self):
        print('=== 제품 수정 ===')
        num = int(input('수정할 제품 번호:'))
        p = self.__dao.selectByNum(num)
        if p == None:
            print('없는 제품 번호')
        else:
            print('수정전 제품 정보')
            print(p)
            name = input('new name(수정안하려면 엔터):')
            if name!='':
                p.setName(name)

            price = int(input('new price(수정안하려면 0):'))
            if price != 0:
                p.setPrice(price)

            amount = int(input('new amount(수정안하려면 0):'))
            if amount != 0:
                p.setAmount(amount)

            self.__dao.update(p)



    def delProduct(self):
        print('=== 제품 삭제 ===')
        num = int(input('삭제할 제품 번호:'))
        self.__dao.delete(num)

    def printAll(self):
        print('=== 제품 리스트 ===')
        a = self.__dao.selectAll()
        for p in a:
            print(p)