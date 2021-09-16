import requests
from bs4 import BeautifulSoup

#vo/dto: 값 담는 객체. 캡슐화. 생성자에 멤버변수 정의하면 끝.
class Bus:
    def __init__(self, route_id=None, bus_name=None, st_station=None, ed_station=None, term=None, first_tm=None, last_tm=None, corp_name=None):
        self.route_id=route_id
        self.bus_name=bus_name
        self.st_station=st_station
        self.ed_station=ed_station
        self.term=term
        self.first_tm=first_tm
        self.last_tm=last_tm
        self.corp_name=corp_name

class Station:
    def __init__(self, seq=None, arsld=None, stationNm=None, beginTm=None, lastTm=None, gpsX=None, gpsY=None):
        self.seq=seq
        self.arsld=arsld
        self.stationNm=stationNm
        self.beginTm=beginTm
        self.lastTm=lastTm
        self.gpsX=gpsX
        self.gpsY=gpsY

class Station:
    def __init__(self, seq=None, arsId=None, stationNm=None, beginTm=None, lastTm=None, gpsX=None, gpsY=None):
        self.seq=seq
        self.arsId=arsId
        self.stationNm=stationNm
        self.beginTm=beginTm
        self.lastTm=lastTm
        self.gpsX=gpsX
        self.gpsY=gpsY

#서비스: 기능구현, 멤버변수, 메서드
class BusService:

    #이 클래스의 메서드들이 공통으로 사용하는 값값
    def __init__(self):
        self.base_url ='http://ws.bus.go.kr/api/rest/busRouteInfo/'
        self.api_key = 'BYgs6%2FjSL0du1z8yK4GxYdW1SepukkJ0gXtUP3tGUQpjThEU4JeQKRlspdSnxTWcjia6U6r5oPxW%2F7tK7HZ2sg%3D%3D'

    #route id를 받아서 정보 검색을 open-api에 요청
    #요청에 대한 응답으로 xml받음
    #받은 xml 파싱 => 노선 정보를 추출 => vo에 담아서 반환
    def getRouteInfo(self, routeId:str):
        cmd = '/getRouteInfo'
        url = self.base_url+cmd+'?ServiceKey='+self.api_key+'&busRouteId='+routeId
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')  # pip install lxml
        code = root.find('headerCd').get_text()
        if code == '0':
            bus_id = root.find('busRouteId').get_text() # 대신에 .text 가능
            bus_name = root.find('busRouteNm').get_text()
            edstation = root.find('edStationNm').get_text()
            ststation = root.find('stStationNm').get_text()
            firsttm = root.find('firstBusTm').get_text()
            lasttm = root.find('lastBusTm').get_text()
            term = root.find('term').get_text()
            corp_name = root.find('corpNm').get_text()

            return Bus(route_id=bus_id, bus_name=bus_name, st_station=ststation, ed_station=edstation, term=term, first_tm=firsttm,
                       last_tm=lasttm, corp_name=corp_name)
        else:
            print('오류발생 code:', code)

    def getStListByRouteId(self, routeId:str):
        cmd = '/getStaionByRoute'
        url = self.base_url + cmd + '?ServiceKey=' + self.api_key + '&busRouteId=' + routeId
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')  # pip install lxml
        code = root.find('headerCd').get_text()
        stations=[]
        if code == '0':
            items = root.select('itemList')
            for item in items:
                seq = item.find('seq').get_text()
                arsId = item.find('arsId').get_text()
                stationNm = item.find('stationNm').get_text()
                beginTm = item.find('beginTm').get_text()
                lastTm = item.find('lastTm').get_text()
                gpsX = item.find('gpsX').get_text()
                gpsY = item.find('gpsY').get_text()
                stations.append(Station(seq=seq, arsId=arsId, stationNm=stationNm, beginTm=beginTm, lastTm=lastTm, gpsX=gpsX, gpsY=gpsY))
        else:
            print('오류발생 code:', code)

        return stations
