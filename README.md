# Python
## **1일차 (210820)**<br>
- 연산자 / 조건문 반복문 / 형변환함수 / 리스트


## **2일차 (210823)**<br>
- list / set / tuple / dictionary / 함수 정의와 호출


## **3일차 (210824)**<br>
- mutable, immutable / param type / 재귀함수(팩토리얼, 피보나치)


## **4일차 (210825)**<br>
- 표준입출력 / file - 입출력, 복사, 파일커서제어, 파일제어 / 패키지


## **5일차 (210826)**
- 예외처리 / 클래스 정의 / 클래스 변수, 메서드


## **6일차 (210830)**<br>
- 상속 / 메서드재정의 / 실습(피카추게임)


## **7일차 (210831)**<br>
- 공장과 편의점 실습 (vo, dao ,service)


## **8일차 (210901)**<br>
- OracleDB연결 / 공장과 편의점실습 DB 반영하여 변경


## **9일차 (210902)**<br>
- Flask 설치 / templates폴더에 뷰 생성 / route를 분할하여 쓰는 blueprint
- url에 primary key 값을 받아올 때, @bp.route('/url/<int:num>')과 같은 형식으로 받아온다.
  int는 읽는 타입이고 뒤에 변수는 url에 등록된 함수 파라메터 변수를 나타낸다.

## **10일차 (210903)**<br>
파이참 프로젝트
1. 터미널에서 플라스크 설치
pip install flask
2. app 개발할 새 디렉토리 하나를 생성(ex.myapp1)
3. html, js.. 뷰 페이지 담을 디렉토리(templates)를 myapp1 하위에 만듬
/myapp1/templates
4. 메인 역할의 파일 app.py생성. 이 파일의 이름은 자유
  다음 내용이 있어야 함.
    1) 플라스크 객체 생성 코드
    app = Flask(__name__)
    2) 블루프린트가 있다면 등록
    app.register_blueprint(등록할 블루프린트 객체)
    3) Flask 실행하는 코드
    app.run()
5. 라우트 파일 생성, 작성
라우트 파일은 스프링의 컨트롤러와 비슷
요청 url을 등록하고 해당 url로 요청이 왔을 때 처리 코드 작성
결과인 뷰 페이지 생성 및 실행
절차: 1) 이 페이지에서 생성한 url들을 등록할 Blueprint() 객체 생성
      2) Blueprint 객체에 url 등록 
6. 뷰페이지는 templates 디렉토리에 저장. 그 밑에 하위 디렉토리 생성하여 사용

**blueprint**: 요청 url 등록 객체
*********************************************************
tcp통신은 연결 지향적이기 때문에 한 쪽에서 close하면 끊김
web은 클라이언트가 요청을 하면 바로 응답하고 연결이 끊어짐
sessoin에서는 아이디로 클라이언트를 구분하고 유효성을 체크

**Flask ORM**
1. orm 설치
pip install Flask-Migrate

2. config 파일 작성

3. model 작성: vo를 작성한다

4. db 초기화
test>flask db init

5. 앱에 db연동
test>flask db migrate

6. db 변경사항 커밋
test>flask db upgrade


## **11일차 (210906)**<br>

- on delete cascade: 어떤 tuple이 삭제될 때 foreign key로 연결된 tuple 또한 같이 삭제되는 것
- relationship 함수는 역참조
