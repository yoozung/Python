# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json
from pprint import pprint

client_id = "Zfr7HfACo7UsKhIlPfvN"
client_secret = "QFoQfQvspa"
encText = urllib.parse.quote("동화가든")
url = "https://openapi.naver.com/v1/search/image?query=" + encText + "&display=1&start=1&sort=sim" # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
    # print(response.find())

    d = json.loads(response_body)
    print('------')

    pprint(d)
    print('------')

    # for e in d['total']:
    #     pprint(e['contact'])
    print('------')

    # for i, e in enumerate(d['test']):
    #     print(i, e['contact'][0]['email'])
    print(d['items'][0]['thumbnail'])
    #
    # emails = {e['contact'][0]['email'] for e in d['test']}
    # print(emails)
    # print('------')
else:
    print("Error Code:" + rescode)