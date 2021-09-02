from flask import request, render_template, redirect, Blueprint  #
import web1.model.factory as f
import web1.model.cu as cu

p_service = f.Service()
cu_service = cu.Service()

bp = Blueprint('order', __name__, url_prefix='/order')  #urlprefix는 매핑할때 앞에 고정으로 들어가는 거 지정

@bp.route('/list')
def order_list():
    olist = cu_service.orderList()
    return render_template('order/list.html', olist=olist)

@bp.route('/add', methods=['POST'])
def order_add():
    pnum = request.form['pnum']
    pname = request.form['pname']
    amount = request.form['amount']
    total_pay = request.form['total_pay']
    cu_service.addOrder(cu.Order(prod=f.Product(num=pnum, name=pname), amount=amount, total_pay=total_pay))
    return redirect('/order/list')

@bp.route('/pay/<int:num>')
def order_pay(num):
    cu_service.pay(num)
    return redirect('/order/list')

@bp.route('/del/<int:num>')
def order_del(num):
    cu_service.delOrder(num)
    return redirect('/order/list')