import requests
from bs4 import BeautifulSoup

class tmap:
    def __init__(self, resultCode=None, areaCode=None, areaNm=None, itsBroNm=None, dtlAddrNm=None, rk=None, baseYm=None):
        self.resultCode=resultCode
        self.areaCode=areaCode
        self.areaNm=areaNm
        self.itsBroNm=itsBroNm
        self.dtlAddrNm=dtlAddrNm
        self.rk=rk
        self.baseYm=baseYm


class tmapService:
    def __init__(self):
        self.base_url ='http://api.visitkorea.or.kr/openapi/service/rest/DataLabService'
        self.api_key = 'MtWzipherkRRrBAwuOqmCl4zW19bJlO0pCXCxotIIQQ6AC3BuWFIECx4YVrmSSAe6HWF9qPdqdsjB6hpQb2UAg=='

    def regionRank(self, y):
        cmd = '/tmapFoodTarItsBroDDList'
        url = self.base_url+cmd+'?ServiceKey='+self.api_key+'&pageNo='+ '1' +'&numOfRows='+ '100' +'&MobileOS=' + 'IOS' + '&MobileApp=' + 'AppTest' +'&baseYm='+ '202106'
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').get_text()
        rlist = []
        if code == '0000':
            items = root.find_all('item')
            for item in items:
                areaCode = item.find('areaCode').get_text()
                areaNm = item.find('areaNm').get_text()
                baseYm = item.find('baseYm').get_text()
                dtlAddrNm = item.find('dtlAddrNm').get_text()
                itsBroNm = item.find('itsBroNm').get_text()
                rk = item.find('rk').get_text()
                if y == areaNm:
                    rlist.append(tmap(areaCode=areaCode, areaNm=areaNm, baseYm=baseYm, dtlAddrNm=dtlAddrNm, itsBroNm=itsBroNm, rk=rk))
        else:
            print('오류발생 code:', code)
        print(rlist)
        return rlist

'''
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

        # return stations
'''