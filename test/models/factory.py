from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

# dao 만들 필요 없이 밑에 이거만 만들면 됨. / db테이블로 만들 vo
class Product(db.Model):   # vo겸 테이블
    num = db.Column(db.Integer, primary_key=True)   #autoincrement (자동할당)
    name = db.Column(db.String(20), nullable=False) #nullable=False = not null
    price = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)

class Service: # 비즈니스 로직. 외부에 제공할 기능구현
    def addProduct(self, p:Product):
        db.session.add(p) # dao의 insert()호출
        db.session.commit()

    def getAll(self):
        # Product.query.all()  # 전체검색
        plist = Product.query.order_by(Product.num.asc())   #오름차asc 내림차desc
        return plist

    def getProductByNum(self, num:int):
        return Product.query.get(num)  # get(): primary key 기준으로 검색

    def getProductByName(self, name:str):
        return Product.query.filter(Product.name==name).all()  # filter(): 검색할 때 조건 추가하는 함수

    def editProduct(self, p:Product): #p:수정할 제품의 번호와 새정보
        p2 = Product.query.get(p.num)   #p2: num으로 검색한 객체의 수정 전 데이터
        p2.name = p.name
        p2.price = p.price
        p2.amount = p.amount
        db.session.commit()


    def delProduct(self, num:int):
        p = Product.query.get(num)
        db.session.delete(p)    # 검색한 객체 삭제
        db.session.commit()

