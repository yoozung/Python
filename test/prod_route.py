from flask import request, render_template, redirect, Blueprint  #
import models.factory as f

p_service = f.Service()
#Blueprint: route 등록 객체 / 라우트 잘라 쓸 때는 app못쓰고 블루프린트 써야됨
bp = Blueprint('product', __name__, url_prefix='/product')  #urlprefix는 매핑할때 앞에 고정으로 들어가는 거 지정

#route파일은 클라이언트 요청 url을 설계하고, 각 요청 url마다 실행할 코드를 함수로 등록
#웹에서는 요청을 url로 함

@bp.route('/list', methods=['POST', 'GET'])  #사용자가 기능 요청
def prod_list():
    arr = p_service.getAll()
    return render_template('product/list.html', plist=arr)  #plist: 뷰페이지에서 부를 이름 / arr: 전달할 값

@bp.route('/add')  #여기서 전송방식 지정안하면 기본이 get /포스트면은 포스트로 지정해줘야됨
def prod_add_get():
    return render_template('product/addForm.html')

@bp.route('/add', methods=['POST'])
def prod_add_post():
    name = request.form['name'] #폼양식 읽어오는 방법: request.form['폼양식이름']
    price = request.form['price']
    amount = request.form['amount']
    p_service.addProduct(f.Product(name=name, price=price, amount=amount))
    return redirect('/product/list')

@bp.route('/get')
def prod_get():
    num = request.args.get('num', 0, int)   #url?뒤에 붙여 보낸 파라메터 읽는 함수(파람이름, 디폴트값(값을 제대로 못읽어올 경우 이 값을 사용), 타입)
    p = p_service.getProductByNum(num)
    return render_template('product/detail.html', p=p)


@bp.route('/edit', methods=['POST'])
def prod_edit():
    num = request.form['num']
    name = request.form['name']
    price = request.form['price']
    amount = request.form['amount']
    p_service.editProduct(f.Product(num=num, name=name, price=price, amount=amount))
    return redirect('/product/list')

@bp.route('/del')
def prod_del():
    num = request.args.get('num', 0, int)
    p_service.delProduct(num)
    return redirect('/product/list')

@bp.route('/prod-detail/<int:p_num>')
def prod_order_detail(p_num):
    p = p_service.getProductByNum(p_num)
    return render_template('order/detail.html', p=p)
