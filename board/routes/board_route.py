from flask import request, render_template, redirect, Blueprint, session
from models import BoardService, Board

service = BoardService()

bp = Blueprint('board', __name__, url_prefix='/board')

@bp.route('/list')
def list():
    blist = service.getAll()
    return render_template('board/list.html', blist=blist)

@bp.route('/add')
def addForm():
    return render_template('board/form.html')


@bp.route('/add', methods=['POST'])
def add():
    writer = request.form['writer']
    title = request.form['title']
    content = request.form['content']
    service.addBoard(Board(writer=writer, title=title, content=content))
    return redirect('/board/list')

@bp.route('/detail/<int:num>')
def detail(num):
    b = service.getBoard(num)
    if b.writer == session['login_id']:
        flag = True
        msg = ''
    else:
        flag = False
        msg = 'readonly'
    return render_template('board/detail.html', b=b, flag=flag, msg=msg)

@bp.route('/edit', methods=['POST'])
def edit():
    num = request.form['num']
    title = request.form['title']
    content = request.form['content']
    service.editBoard(Board(num=num, title=title, content=content))
    return redirect('/board/list')