# Flask
파이썬 웹 프레임워크
django보다는 라이트한 프레임워크

다른 라이브러리들과 충돌하지 않도록 /venv라는 가상환경을 설정했고(가상환경은 .gitignore 설정!), 거기에 라이브러리 다운받음!

*주의* 변수나 파일 이름을 flask로 사용하면 안 됨!

### 1. $ python -m venv venv   로 가상환경 설정

### 2. $ pip install flask    로 flask 다운

### 3. flask 설정
        from flask import Flask
        app = Flask(__name__)

### 4. 명령어 간소화 작업
        touch .bashrc
        vi .bashrc
            ```
            export FLASK_APP=hello.py
            ```
        source ~/.bashrc
        
        flask run   // 실행