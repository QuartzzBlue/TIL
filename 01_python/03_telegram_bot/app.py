from flask import Flask, render_template, request
from decouple import config
import requests
app = Flask(__name__)

# .env 파일에 있는 것들! -> git이 관리하지 않는 것들은 이렇게 끌어서 사용!
base = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('message')
    requests.get(f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return render_template('send.html',text = text)

@app.route(f'/{token}', methods=['POST'])
def telegram():
    # step 1. 구조 print 해보기 & 변수 저장
    print(request.get_json())
    from_telegram = request.get_json()

    # step 2. 그대로 돌려보내기
    if from_telegram.get('message') is not None: # NoneType일 경우만 예외처리
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')
        # url = f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        

        # text의 0~3글자가 '/한영 ' 일 때, 
        if text[0:4] == '/한영 ' : 
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret':naver_client_secret
                }
            data = {'source':'ko', 'target':'en', 'text':text[4:]}  # 데이터 안의 text에는 4글자부터의 문장을 넣겠다
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText') # text 에 번역된 결과 넣어줌

        if text[0:4] == '/영한 ' : 
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret':naver_client_secret
                }
            data = {'source':'en', 'target':'ko', 'text':text[4:]}  # 데이터 안의 text에는 4글자부터의 문장을 넣겠다
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText') # text 에 번역된 결과 넣어줌


        if text[0:4] == '/로또 ':
            num = text[4:]
            res = request.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
            lotto = res.json()

            winner = []
            for i in range(1,7):
                winner.append(lotto[f'drwtNo{i}'])
            bonus_num = lotto['bnusNo']
            text = f'{num}회차 로또 당첨번호는 {winner}입니다. 보너스 당첨번호는 {bonus_num}입니다.'


        requests.get(f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

    return '', 200


