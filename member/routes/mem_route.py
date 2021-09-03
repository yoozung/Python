from flask import request, render_template, redirect, Blueprint, session
from member.models.mem_model import Service, Member

bp = Blueprint('member', __name__, url_prefix='/member')

service = Service()

@bp.route('/list')
def list():
    mlist = service.getAll()
    return render_template('member/list.html', mlist=mlist)

@bp.route('/join')
def joinForm():
    return render_template('member/form.html')

@bp.route('/join', methods=['POST'])
def join():
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name']
    email = request.form['email']
    service.addMember(Member(id, pwd, name, email))
    return redirect('/member/list')

@bp.route('/get/<string:id>')
def get(id):
    m:Member = service.getMember(id)
    return render_template('member/detail.html', m=m)

@bp.route('/edit', methods=['POST'])
def edit():
    id = request.form['id']
    pwd = request.form['pwd']
    service.editMember(Member(id=id, pwd=pwd))
    return redirect('/member/list')

@bp.route('/del/<string:id>')
def delete(id):
    service.delMember(id)
    return redirect('/member/logout')

@bp.route('/login')
def loginForm():
    return render_template('member/login.html')

@bp.route('/login', methods=['POST'])
def login():
    id = request.form['id']
    pwd = request.form['pwd']
    m:Member = service.getMember(id)
    msg = ''
    if m==None:
        msg = '없는 아이디'
    else:
        if m.pwd == pwd:
            session['login_id']=id  # 뷰페이지에서 표현: {{session.login_id}}
            session['flag']=True
        else:
            msg = '패스워드 불일치'
    session['msg'] = msg
    return redirect('/member/list')

@bp.route('/logout')
def logout():
    session['flag'] = False
    session.pop('login_id')  #로그아웃
    session.pop('msg')
    return redirect('/member/list')