#스프링에서 컨트롤러 같은역할하는 곳. 이름은 맘대로 정해도 상관없음
from flask import Flask, render_template  #render_template눈 뷰페이지 만들어쥬는애
import routes.prod_route as pr
import routes.order_route as ort

app = Flask(__name__)   #웹 어플리케이션 객체 생성

app.register_blueprint(pr.bp)   #app(여기)에다가 라우드 등록하는거
app.register_blueprint(ort.bp)

@app.route('/')
def root():
    return render_template('index.html', msg='hello flask~')



if __name__ == '__main__':
    app.run()#flask 서버 실행