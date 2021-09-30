import requests
from bs4 import BeautifulSoup

import urllib.request
import json
from pprint import pprint

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import session

db = SQLAlchemy()
migrate = Migrate()

class NationWide(db.Model):
    rk = db.Column(db.Integer, primary_key=True)
    itsBroNm = db.Column(db.String(20), nullable=True)
    areaNm = db.Column(db.String(20), nullable=True)
    areaCode = db.Column(db.String(20), nullable=False)
    baseYm = db.Column(db.String(20), nullable=False)
    imgLink = db.Column(db.String(100), nullable=False)
    dtlAddrNm = db.Column(db.String(50), nullable=False)

class Board(db.Model):
    #게시글 번호, 내용, 작성자, 작성일
    num = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    writer = db.Column(db.String(20), nullable=False)
    w_date = db.Column(db.DateTime(), nullable=False)

    itsBroNm = db.Column(db.String(20), nullable=True)
    # b_itsBroNm = db.Column(db.String(20), db.ForeignKey('nationwide.itsBroNm', ondelete='CASCADE'))

class Region(db.Model):
    rk = db.Column(db.Integer, primary_key=True)
    itsBroNm = db.Column(db.String(20), nullable=True)
    areaNm = db.Column(db.String(20), nullable=True)
    areaCode = db.Column(db.String(20), nullable=False)
    baseYm = db.Column(db.String(20), nullable=False)
    imgLink = db.Column(db.String(500), nullable=True)
    dtlAddrNm = db.Column(db.String(50), nullable=False)


#vo/dto:값 담는 객체. 캡슐화. 생성자에 멤버변수 정의하면 끝.
class tmap:
    def __init__(self, resultCode=None, areaCode=None, areaNm=None, itsBroNm=None, dtlAddrNm=None, rk=None, baseYm=None, imgLink=None):
        self.resultCode=resultCode
        self.areaCode=areaCode
        self.areaNm=areaNm
        self.itsBroNm=itsBroNm
        self.dtlAddrNm=dtlAddrNm
        self.rk=rk
        self.baseYm=baseYm
        self.imgLink=imgLink
        self.rkList = [resultCode, areaCode, areaNm, itsBroNm, dtlAddrNm, rk, baseYm]
        self.rkList2 = []
        self.rkList3 = []


#서비스: 기능구현. 멤버변수, 메서드
class NationWideService:

    #이 클래스의 메서드들이 공통을 사용하는 값
    def __init__(self):
        self.base_url ='http://api.visitkorea.or.kr/openapi/service/rest/DataLabService'
        self.api_key = 'MtWzipherkRRrBAwuOqmCl4zW19bJlO0pCXCxotIIQQ6AC3BuWFIECx4YVrmSSAe6HWF9qPdqdsjB6hpQb2UAg=='

    #route_id를 받아서 정보 검색을 open-api에 요청
    #요청에 대한 응답으로 xml받음
    #받은 xml 파싱 => 노선 정보를 추출 => vo에 담아서 반환
    def getRouteInfo(self):
        cmd = '/tmapFoodTarItsBroDDList'
        url = self.base_url+cmd+'?ServiceKey='+self.api_key+'&pageNo='+ '1' +'&numOfRows='+ '50' +'&MobileOS=' + 'IOS' + '&MobileApp=' + 'AppTest' +'&baseYm='+ '202106'
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')  # pip install lxml
        code = root.find('resultCode').get_text()
        rkList3 = []

        print('NationWide.query.count()', NationWide.query.count())
        self.deleteNationWide()

        if code == '0000':
            items = root.find_all('item')
            for item in items:
                areaCode = item.find('areaCode').get_text()
                areaNm = item.find('areaNm').get_text()
                baseYm = item.find('baseYm').get_text()
                dtlAddrNm = item.find('dtlAddrNm').get_text()
                itsBroNm = item.find('itsBroNm').get_text()
                rk = item.find('rk').get_text()
                imgLink = self.getImgLink(itsBroNm)


                self.addNationWide(NationWide(areaCode=areaCode, areaNm=areaNm, baseYm=baseYm, dtlAddrNm=dtlAddrNm, itsBroNm=itsBroNm, rk=rk, imgLink=imgLink))

        else:
            print('오류발생 code:', code)
        # print(rkList3)
        # print(len(rkList3))


    def getImgLink(self, title:str):
        client_id = "Zfr7HfACo7UsKhIlPfvN"
        client_secret = "QFoQfQvspa"
        encText = urllib.parse.quote(title)
        url = "https://openapi.naver.com/v1/search/image?query=" + encText + "&display=1&start=1&sort=sim"  # json 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()

            # 다음 세개 구동때 키기
            # print(json.loads(response_body)['items'][0]['thumbnail'])
            print(encText)
            print(title, type(title))
            print(json.loads(response_body)['items'])
            # print(response_body.decode('utf-8'))

            return json.loads(response_body)['items'][0]['thumbnail']
        else:
            print("Error Code:" + rescode)


    def addNationWide(self, b:NationWide):
        db.session.add(b)
        db.session.commit()

    def deleteNationWide(self):
        w = NationWide.query.count()
        for i in range(1, w+1):
            q = NationWide.query.get(i)
            db.session.delete(q)
        db.session.commit()

    def getNationWide(self, num:int):
        db.session.commit()
        return NationWide.query.get(num)


    def getAll(self):
        db.session.commit()
        return NationWide.query.order_by(NationWide.rk.asc())


class BoardService:
    # def getAll(self, itsBroNm):
    #     return Board.query.filter_by(itsBroNm=itsBroNm).order_by(Board.num.asc())

    def getAll(self, itsBroNm):
        return Board.query.filter_by(itsBroNm=itsBroNm).order_by(Board.num.asc())

    def getByNum(self, num):
        return Board.query.get(num)

    def addBoard(self, c:Board):  # b: content, writer, w_date
        db.session.add(c)
        db.session.commit()
        return c

    def editBoard(self, c): #내용
        bb = Board.query.get(c.num)
        bb.content = c.content
        db.session.commit()

    def delBoard(self, num):
        b = Board.query.get(num)
        db.session.delete(b)
        db.session.commit()

class RegionService:
    def addRegion(self, c: Region):
        db.session.add(c)
        db.session.commit()

    def deleteRegion(self):
        w = Region.query.count()
        for i in range(1, w + 1):
            q = Region.query.get(i)
            db.session.delete(q)
        db.session.commit()

    def getRegion(self, areaNm: str):
        # return Region.query.get()
        # return Region.query.filter_by(areaNm=areaNm)
        return NationWide.query.filter_by(areaNm=areaNm).order_by(NationWide.rk.asc())
        # return NationWide.query.filter_by(areaNm=areaNm).order_by(NationWide.rk.asc())

    def getAll(self):
        db.session.commit()
        return Region.query.order_by(Region.rk.asc())