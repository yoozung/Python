import requests
from bs4 import BeautifulSoup

#vo/dto:값 담는 객체. 캡슐화. 생성자에 멤버변수 정의하면 끝.
class tmap:
    def __init__(self, resultCode=list, areaCode=list, areaNm=list, itsBroNm=list, dtlAddrNm=list, rk=list, baseYm=list):
        self.resultCode=resultCode
        self.areaCode=areaCode
        self.areaNm=areaNm
        self.itsBroNm=itsBroNm
        self.dtlAddrNm=dtlAddrNm
        self.rk=rk
        self.baseYm=baseYm
        self.rkList = [resultCode, areaCode, areaNm, itsBroNm, dtlAddrNm, rk, baseYm]
        self.rkList2 = []


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
        url = self.base_url+cmd+'?ServiceKey='+self.api_key+'&pageNo='+ '1' +'&numOfRows='+ '10' +'&MobileOS=' + 'IOS' + '&MobileApp=' + 'AppTest' +'&baseYm='+ '202106'
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')  # pip install lxml
        code = root.find('resultCode').get_text()
        if code == '0000':
            items = root.find_all('itemList')
            for item in items:
                areaCode = item.find('areaCode').get_text()
                areaNm = item.find('areaNm').get_text()
                baseYm = item.find('baseYm').get_text()
                dtlAddrNm = item.find('dtlAddrNm').get_text()
                itsBroNm = item.find('itsBroNm').get_text()
                rk = item.find('rk').get_text()


                tmap().rkList.append(areaCode)
                tmap().rkList.append(areaNm)
                tmap().rkList.append(baseYm)
                tmap().rkList.append(itsBroNm)
                tmap().rkList.append(dtlAddrNm)
                tmap().rkList.append(rk)

                # tmap().rkList2.append(tmap().rkList())

                # tmap().rkList = []

            # return tmap(areaCode=areaCode, areaNm=areaNm, baseYm=baseYm, dtlAddrNm=dtlAddrNm, itsBroNm=itsBroNm, rk=rk)
        else:
            print('오류발생 code:', code)
        print(tmap().rkList2)

    def getStListByRouteId(self, routeId:str):
        cmd = '/getStaionByRoute'
        url = self.base_url + cmd + '?ServiceKey=' + self.api_key + '&busRouteId=' + routeId
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')  # pip install lxml
        code = root.find('headerCd').get_text()
        stations=[]
        if code == '0':
            items = root.find_all('itemList')
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