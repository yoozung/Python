from flask import Flask, render_template, session
import member.routes.mem_route as memr

app = Flask(__name__)
app.register_blueprint(memr.bp)
app.secret_key = 'yoo'


@app.route('/')
def root():
    session['flag'] = False #flag:True=>로그인상태 / False: 미로그인
    return render_template('index.html')



if __name__ == '__main__':
    app.run()#flask 서버 실행