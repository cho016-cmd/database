from flask import Flask, render_template

# Flask 애플리케이션 인스턴스 생성 및 템플릿 폴더 경로 설정
app = Flask(__name__, template_folder='html')

# 루트 URL(예: http://127.0.0.1:5000/)에 대한 라우트 정의
@app.route('/')
def home():
    # 'html' 폴더에 있는 'index.html' 파일을 렌더링하여 반환
    return render_template('index.html')

# 이 파일이 직접 실행될 때 웹 서버를 구동
if __name__ == '__main__':
    # 디버그 모드를 활성화하여 코드 수정 시 자동으로 서버 재시작
    app.run(debug=True)
