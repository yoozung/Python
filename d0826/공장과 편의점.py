'''
주말까지 완성하기
공장과 편의점
1. 공장 warehouse
    하위메뉴: 1.제품등록 2.검색 3.수정 4.삭제 5.전체출력 6.종료(상위메뉴)

2. 편의점 convenience store
    하위메뉴: 1.주문 2.주문취소(결제된제품은 취소 안됨) 3.주문목록
             4.결제(결제대상(결제유무가 False) 보여주고 사용자가 선택 5.종료(상위메뉴)

3. 종료(프로그램 종료)

product
제품번호(자동할당)
제품명
가격
수량

order
주문번호(자동할당)
주문상품(product)
주문수량
결제금액(단가*주문수량)
결제유무(True/False)
'''

'''
1. 공장 warehouse
    하위메뉴: 1.제품등록 2.검색 3.수정 4.삭제 5.전체출력 6.종료(상위메뉴)
'''
class warehouse:
    def __init__(self, pNo='', pName='', price='', quantity=''):
        self.pNo = pNo
        self.pName = pName
        self.price = price
        self.quantity = quantity

    # 5.전체출력
    def print(self):
        print('제품번호: ', self.pNo)
        print('제품명: ', self.pName)
        print('가격: ', self.price)
        print('수량: ', self.quantity)


class warehouseDao:
    def __init__(self):
        self.products = []

    def insert(self, p):
        self.products.append(p)

    def select(self, pNo):
        for p in self.products:
            if p.pNo == pNo:
                return p

    def selectAll(self):
        return self.products


    def delete(self, pNo):
        old = self.select(pNo)
        if old == None:
            return False
        else:
            self.products.remove(old)
            return True

class warehouseService:
    def __init__(self):
        self.dao = warehouseDao()

    # 1.제품등록
    def addProduct(self):
         #제품번호는 자동할당처리로 변경하기
        pNo = input('제품번: ')
        pName = input('제품명: ')
        price = input('가격: ')
        quantity = input('수량: ')
        return warehouse(pNo, pName, price, quantity)

    # 2.검색
    def getProduct(self):
        pNo = input('제품번호로 검색:')
        p = self.dao.select(pNo)
        if p == None:
            print('없는 제품입니다.')
        else:
            p.print()

def warehouseRun():
    ws = warehouseService()
    while True:
        w = int(input('1.제품등록 2.검색 3.수정 4.삭제 5.전체출력 6.종료'))
        if w == 1:
            ws.addProduct()
        elif w == 2:
            ws.getProduct()

if __name__ == '__main__':
    warehouseRun()