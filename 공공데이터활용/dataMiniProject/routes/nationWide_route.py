import math
from tkinter import messagebox as msg
from tkinter import Tk

import pyautogui as pg

from itertools import zip_longest

from flask import Flask, request, render_template, redirect, Blueprint
import models as mo
import matplotlib.pyplot as plt

bp = Blueprint('nationWide', __name__, url_prefix='/nationWide')

service = mo.NationWideService()
boardService = mo.BoardService()

@bp.route('/nationWide_info', methods=['POST', 'GET'])
def nationWide_info():

    page = request.args.get('page', type=int, default=1)  # 페이지
    nationWide = service.getAll()  # DB에 저장되게 다시 코딩해야되나?? 리퀘스트가 너무많고 리스폰도 너무 느려진다. 한번 불러온다음 객체에 저장되어있게끔 못하는건가?
    nationWide = nationWide.paginate(page, per_page=5)

    return render_template(
        'nationWide/nationWideInfo.html',
        page=page, nationWide=nationWide)

@bp.route('/api_to_db', methods=['POST', 'GET'])
def api_to_db():

    service.getRouteInfo()

    # 얼랏방식 메시지박스
    # a = pg.alert(text='데이터가 최신화 되었습니다.', title='알림창', button='OK')
    # print(a)

    # tkinter 방식 메시지 박스
    msg.showinfo('알림창', '데이터가 최신화 되었습니다.')
    return render_template('index.html')


@bp.route('/detail/<int:num>') #<a href="/board/detail/{{b.num}}">
def detail(num):
   b = service.getNationWide(num)
   print(num)
   d= b.itsBroNm
   print(d)
   c = boardService.getAll(d)
   return render_template('nationWide/nationWideInfoDetail.html', b=b, c=c, num=num)



@bp.route('/route-path', methods=['POST'])
def route_path():
    routeid = request.form['routeid']
    stList:list = service.getStListByRouteId(routeId=routeid)
    return render_template('nationWide/stList.html', stList=stList, routeid=routeid)

@bp.route('/graph')#get 방식
def graph():
    img_path = '../static/graph/my_plot.png'

    x = [1, 2, 3, 4]
    y = [3, 8, 5, 6]
    fig, ax = plt.subplots()#그래프 이미지 객체 생성
    plt.plot(x, y) #fig 객체에 그래프를 그림
    fig.savefig(img_path)#fig 객체를 파라메터로 지정한 패스의 파일로 저장
    img_path = '/' + img_path
    return render_template('graph.html', img_path=img_path)