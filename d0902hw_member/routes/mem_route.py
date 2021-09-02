from flask import request, render_template, redirect, Blueprint
import d0902hw_member.model.member as m

m_service = m.Service()
bp = Blueprint('member', __name__, url_prefix='/member')



@bp.route('/addForm')  #여기서 전송방식 지정안하면 기본이 get /포스트면은 포스트로 지정해줘야됨
def member_add_get():
    return render_template('/add.html')

@bp.route('/add', methods=['POST'])
def member_add_post():
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name']
    email = request.form['email']
    m_service.addMember(m.Member(id=id, pwd=pwd, name=name, email=email))

@bp.route('/get')
def member_get():
    id = request.args.get('id', None, str)   #url?뒤에 붙여 보낸 파라메터 읽는 함수(파람이름, 디폴트값(값을 제대로 못읽어올 경우 이 값을 사용), 타입)
    m = m_service.getMemberById(id)
    return render_template('member/detail.html', m=m)
