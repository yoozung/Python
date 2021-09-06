from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import session
from datetime import datetime

db = SQLAlchemy()
migrate = Migrate()

#멤버(회원관리)
class Member(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    pwd = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)

#게시판 테이블. 글번호, 작성자, 작성자별세트, 작성일, 제목, 내용
class Board(db.Model):
    num = db.Column(db.Integer, primary_key=True)
    writer = db.Column(db.String(20), db.ForeignKey('member.id', ondelete='CASCADE'))   #작성자컬럼은 문자열에 크기가 20 / 포링키 - 멤버테이블에 아이디를 참조하는 참조키 / 온딜리트캐스케이드: 글을 하나라도 작성한 사람은 회원에서 삭제 안되고 이사람이 탈퇴하면 글까지 삭제됨
    #릴레이션쉽함수는 역참조/ 멤버테이블에서 역참조를 하겠다고 써놓은 것임. ///선생님 질문이 있습니다 ForeignKey로 테이블간 연결이 되어 있지 않으면 역참조가 불가능한건가요?!
    member = db.relationship('Member', backref=db.backref('board_set'))
    w_date = db.Column(db.DateTime(), nullable=False)   #DateTime는 데이터타입이 날짜인 것.
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(200), nullable=False)

class MemService:
    def join(self, m:Member):#회원가입
        db.session.add(m)
        db.session.commit()

    def login(self, id:str, pwd:str):#로그인
        mem = Member.query.get(id)
        if mem is not None:
            if pwd == mem.pwd:
                session['login_id']=id
                session['flag']=True
                return True

        return False

    def myInfo(self):#로그인 한 id로 검색한 객체 반환
        id = session['login_id']
        return Member.query.get(id)

    def editMyInfo(self, pwd:str): #새 pwd받아서 현재 로그인 중인 id로 검색하여 수정
        mem = self.myInfo()
        mem.pwd = pwd
        db.session.commit()

    def logout(self):#session에서 id 삭제 및 flag =False로 변환
        session.pop('login_id')
        session['flag']=False

    def out(self):#로그인한 id를 db에서 삭제. 로그아웃 처리.
        mem = self.myInfo()
        db.session.delete(mem)
        db.session.commit()
        self.logout()



class BoardService:
    def addBoard(self, b:Board):#작성자id, title, content
        b.w_date = datetime.now()
        db.session.add(b)
        db.session.commit()

    def getBoard(self, num):
        return Board.query.get(num)

    def getAll(self):
        return Board.query.order_by(Board.num.desc())

    def getByTitle(self, tit):
        return Board.query.filter(Board.title.like('%'+tit+'%')).all()

    def getByWriter(self, writer):
        mem = Member.query.get(writer)
        if mem is not None:
            return mem.board_set #작성자가 쓴 모든 글 검색해서 반환

    def editBoard(self, b:Board):
        b2 = self.getBoard(b.num)
        b2.title = b.title
        b2.content = b.content
        #b2.w_date = datetime.now()
        db.session.commit()

    def delBoard(self, num):
        b = self.getBoard(num)
        db.session.delete(b)
        db.session.commit()
