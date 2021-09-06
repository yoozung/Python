from flask import Flask, request, render_template, redirect, session
from models import db, migrate
import routes.mem_route as mr
import routes.board_route as br
import routes.upload_route as ur

import config

#플라스크 객체 생성
app = Flask(__name__)

#시크릿 키 생성
app.secret_key = 'asfaf'

#플라스크 컨피그에 사용자정의 컨피그 추가
app.config.from_object(config)

#블루 프린트 등록
app.register_blueprint(mr.bp)
app.register_blueprint(br.bp)
app.register_blueprint(ur.bp)

# ORM 연동
db.init_app(app)
migrate.init_app(app, db)

@app.route('/')
def root():
    if 'flag' not in session.keys():
        session['flag']=False
    return render_template('index.html')


if __name__ == '__main__':
    app.run()#flask 서버 실행