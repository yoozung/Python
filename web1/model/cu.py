import cx_Oracle
import web1.model.factory as f

class Order:
    def __init__(self, num=None, prod=None, amount=None, total_pay=None, isPay=False):
        self.__num = num
        self.__prod = prod  #사용자가 선택한 상품 객체
        self.__amount = amount
        self.__total_pay = total_pay
        self.__isPay = isPay    #True:결제 / False:미결제

    def __str__(self):
        return 'num:'+str(self.__num)+' / prod num:'+str(self.__prod.getNum())+' / prod name:'+self.__prod.getName()\
               +' / amount:'+str(self.__amount)+' / total_pay:'+str(self.__total_pay)+' / isPay:'+str(self.__isPay)

    def setNum(self, num):
        self.__num = num

    def getNum(self):
        return self.__num

    def setProd(self, p):
        self.__prod = p

    def getProd(self):
        return self.__prod

    def setAmount(self, amount):
        self.__amount = amount

    def getAmount(self):
        return self.__amount

    def setTotal_pay(self, total_pay):
        self.__total_pay = total_pay

    def getTotal_pay(self):
        return self.__total_pay

    def setPay(self, isPay):
        self.__isPay = isPay

    def isPay(self):
        return self.__isPay

class Dao:
    def __init__(self):
        self.conn = None  # 커넥션 객체

    def connect(self):
        self.conn = cx_Oracle.connect("scott", "tiger", "localhost:1521/XE", encoding='utf-8')
        return self.conn.cursor()

    def insert(self, o):
        cursor = self.connect()
        sql = 'insert into prod_order values(seq_prod_order.nextval, :1, :2, :3, :4)'
        d = (o.getProd().getNum(), o.getAmount(), o.getTotal_pay(), 'false')
        cursor.execute(sql, d)
        self.conn.commit()
        self.conn.close()

    def selectByNum(self, num):#주문번호로 검색해서 반환
        cursor = self.connect()
        sql = 'select o.num, o.amount, total_pay, ispay, p.num, p.name from prod_order o, product p where o.prod_num=p.num and o.num=:1'
        d = (num,)
        cursor.execute(sql, d)
        row = cursor.fetchone() #검색결과에서 한 줄만 추출
        self.conn.close()
        if row is not None:
            return Order(num=row[0], prod=f.Product(num=row[4], name=row[5]), amount=row[1], total_pay=row[2], isPay=row[3])


    def selectByisPay(self, flag):#flag:True/False. isPay가 flag값과 동일한것 찾아서 리스트에 담아서 반환
        arr = []
        cursor = self.connect()
        sql = 'select o.num, o.amount, total_pay, ispay, p.num, p.name ' \
              'from prod_order o, product p ' \
              'where o.prod_num=p.num and ispay=:1'
        d = (flag,)
        cursor.execute(sql, d)
        for row in cursor:
            arr.append(Order(num=row[0], prod=f.Product(num=row[4], name=row[5]), amount=row[1], total_pay=row[2], isPay=row[3]))
        self.conn.close()
        return arr


    def selectAll(self):  # 전체검색
        arr = []
        cursor = self.connect()
        sql = 'select o.num, o.amount, total_pay, ispay, p.num, p.name from prod_order o, product p where o.prod_num=p.num order by o.num'
        cursor.execute(sql)
        for row in cursor:
            arr.append(Order(num=row[0], prod=f.Product(num=row[4], name=row[5]), amount=row[1], total_pay=row[2],
                             isPay=row[3]))
        self.conn.close()
        return arr

    def delete(self, num): #주문취소. 주문번호로 삭제
        cursor = self.connect()
        sql = "delete prod_order where num=:1 and ispay='false'"
        d = (num,)
        cursor.execute(sql, d)
        self.conn.commit()
        self.conn.close()

    def updatePay(self, num):#결제시 isPay를 True로 변경
        cursor = self.connect()
        sql = "update prod_order set ispay=:1 where num=:2 and ispay='false'"
        d = ('true', num)
        cursor.execute(sql, d)
        self.conn.commit()
        self.conn.close()

class Service:
    def __init__(self):
        self.__dao = Dao()

    def addOrder(self, o):
        self.__dao.insert(o)

    def delOrder(self, num):
        self.__dao.delete(num)

    def orderList(self):
        return self.__dao.selectAll()

    def pay(self, num):
        self.__dao.updatePay(num)

