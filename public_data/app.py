from flask import Flask, request, render_template, redirect, session
import routes as r
app = Flask(__name__)

#블루 프린트 등록
app.register_blueprint(r.bp)

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()