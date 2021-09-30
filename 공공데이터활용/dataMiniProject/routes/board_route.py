from datetime import datetime

from flask import request, render_template, redirect, session, Blueprint
import models as mo
from models import Board
import os


bp = Blueprint('board', __name__, url_prefix='/board')

service = mo.NationWideService()
boardService = mo.BoardService()



# @bp.route('/add/form/<int:num>/<string:itsBroNm>')
# def addForm(num, itsBroNm):
#     # itsBroNm = request.form['itsBroNm']
#     return render_template('board/form.html', num=num, itsBroNm=itsBroNm)

@bp.route('/add/<int:num>', methods=['POST'])
def add(num):
    content = request.form['content']
    writer = request.form['writer']
    w_date = datetime.now()
    itsBroNm = request.form['itsBroNm']
    print(content)
    print('board_routes:itsBroNm', itsBroNm)
    boardService.addBoard(Board(content=content, writer=writer, w_date=w_date, itsBroNm=itsBroNm))


    b = service.getNationWide(num)

    c = boardService.getAll(itsBroNm)

    # b = service.getNationWide(num)
    # w = b.num
    # print(w)
    # return redirect('nationWide/detail/'+str(request.form[num]), c=c, num=num)
    return render_template('nationWide/nationWideInfoDetail.html', b=b, c=c, num=num)
# +str(request.form[num])

@bp.route('/list')
def list():
    blist = service.getAll()
    return render_template('board/list.html', blist=blist)

@bp.route('/detail/<int:num>')
def detail(num):
    b = service.getByNum(num)
    return render_template('board/detail.html', b=b)


@bp.route('/edit/<int:num>')
def edit(num):
    b = service.getByNum(num)
    return render_template('board/editForm.html', b=b)

@bp.route('/editBoard', methods=['POST'])
def editBoard():
    content = request.form['content']
    w_date = datetime.now()
    service.editBoard(content=content, w_date=w_date)
    return redirect('/board/detail/'+str(request.form['num']))

#@bp.route('/del/<int:num>')
@bp.route('/del/<int:num>')
def delBoard(num):
    service.delBoard(num)
    return redirect('/board/list')
