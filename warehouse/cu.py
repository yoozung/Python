import copy
#편의점

#vo: 주문번호(자동) / 주문상품(product객체) / 수량 / 결제금액 / 결제유무
class Order:
    cnt = 0
    def __init__(self, num=None, prod=None, amount=None, total_pay=None, isPay=False):
        if num == None:
            Order.cnt += 1
            self.__num = Order.cnt
        else:
            self.__num = num

        self.__prod = prod
        self.__amount = amount
        self.__total_pay = total_pay
        self.__isPay = isPay

    def __str__(self):
        return 'num:' + str(self.__num) + ' / prod num:' + str(
            self.__prod.getNum()) + ' / prod name:' + self.__prod.getName() \
               + ' / amount:' + str(self.__amount) + ' / total_pay:' + str(
            self.__total_pay) + ' / isPay:' + str(self.__isPay)

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
        self.__orders = []

    def insert(self, o):    #o:주문객체를 받아서 orders에 추가
        #결제금액: 단가*수량
        o.setTotal_pay(o.getProd().getPrice() * o.getAmount())  #결제금액계산
        self.__orders.append(o)

    def selectByNum(self, num): #주문번호로 검색해서 반환
        for o in self.__orders:
            if o.getNum() == num:
                return o

    def selectByisPay(self, flag):  #flag:True/False isPay가 Flag값과 동일한 것 찾아서 리스트에 담아서 반환
        arr = []
        for o in self.__orders:
            if o.isPay() == flag:
                arr.append(o)
        return arr

    def selectAll(self):    #전체검색
        arr = copy.deepcopy(self.__orders)
        return arr

    def delete(self, num):  #주문취소. 주문번호로 삭제
        o = self.selectByNum(num)
        if o == None:
            return False, '없는 주문 번호'
        else:
            if o.isPay():
                return False, '결제한 주문은 취소 불가'
            else:
                self.__orders.remove(o)
                return True, ''

    def updatePay(self, num):   #결제시 isPay를 True로 변경
        o = self.selectByNum(num)
        if o == None:
            return False, '없는 주문 번호'
        else:
            if o.isPay():
                return False, '이미 결제된 주문'
            else:
                o.setPay(True)
                return True, ''


class Service:
    def __init__(self):
        self.__dao = Dao()

    def addOrder(self, p):  #주문. p:주문할 제품(product)객체
        #주문수량 입력받아 Order 객체 생성해서 dao.insert() 호출
        amount = int(input('주문수량: '))
        self.__dao.insert(Order(prod=p, amount=amount))

    def delOrder(self): #주문취소. 취소할 주문번호 입력받아 dao.delete()호출
        print('=== 주문 취소 ===')
        num = int(input('취소할 주문번호: '))
        flag, msg = self.__dao.delete(num)
        if flag == False:
            print('에러종류: ', msg)
            print('주문을 취소할 수 없음')
        else:
            print('주문 취소 완료')

    def orderList(self):    #주문 리스트 출력. dao,selectAll()
        print('=== 주문 목록 ===')
        arr = self.__dao.selectAll()
        for a in arr:
            print(a)

    def pay(self):  #결제. 결제대상목록출력(pay가 False인 주문목록). 결제할 주문번호 입력받아 dao.updatePay() 호출
        print('=== 결제 ===')

        arr = self.__dao.selectByisPay(False)
        print('=== 결제 대상 주문 목록 ===')
        for a in arr:
            print(a)

        num = int(input('결제할 주문 번호: '))
        flag, msg = self.__dao.updatePay(num)
        if flag == False:
            print('에러종류: ', msg)
            print('결제가 취소됨')
        else:
            print('결제 완료')

