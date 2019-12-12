from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def hello():
    #return "Hello World!"
    return render_template('index.html')

@app.route('/t4ir')
def t4ir():
    return 'This is T4IR'

@app.route('/ssafy')
def ssafy():
    return 'SSAFY'

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end = datetime.datetime(2020, 4, 21)
    td = end - today
    return f'{td.days}일 남았습니다.'

@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag!</h1>'

@app.route('/html_line')
def html_line():        # """ """ 으로 묶으면 여러 줄 보낼 수 있음!
    return """
        <h1> 여러 줄을 보내봅시다. </h1>
        <ul>
            <li>1번</li>
            <li>2번</li>
        </ul>
    """

@app.route('/greeting/<name>')      #'/greeting/<string:name>' 이라고 해도 됨 string 디폴트 생략
def greeting(name):
    #return f'반갑습니다! {name}님'
    return render_template('greeting.html', html_name=name) # html에서 html_name으로 불러온 변수 사용 가능!

@app.route('/cube/<int:number>')      #'/cube/<int:number>' 같은 경우는 꼭 int 붙여줘야함!
def cube(number):
    return f'{number}의 3제곱 {number**3}입니다.'

@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['짜장면', '짬뽕', '볶음밥', '고추잡채밥', '유산슬', '탕수육']
    order = random.sample(menu, people)
    return str(order)

@app.route('/movie')
def movie():
    movies =['겨울왕국2','머니게임','백두산','블랙위도우','나이브스아웃']
    return render_template('movie.html', movies = movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html', age_in_html=age)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

@app.route('/isitbirth')
def isitbirth():
    today = datetime.now()
    if today.month == 11 and today.day == 21:
        result = True
    else:
        result = False
    return render_template('isitbirth.html', result = result)

@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

@app.route('/godmademe')
def godmademe():
    name = request.args.get('username')
    first_list = ['잘생기고','못생기고','어중간하고']
    str[0] = random.choice(first_list)
    second_list = ['작은','큰','보통키의']
    str[1] = random.choice(second_list)
    third_list = ['화난','무표정한','행복한']
    str[2] = random.choice(third_list)
    return render_template('godmademe.html', str = str, user = username)

# 따로 클릭하지 않고도 바로 창 뜨게 만들어 줌
if __name__ == "__main__":
    app.run(debug=True) 
