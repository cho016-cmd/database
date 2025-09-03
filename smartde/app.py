import streamlit as st
import streamlit.components.v1 as components
import os

# 페이지 전체 레이아웃 설정
st.set_page_config(layout="wide")

# HTML 파일의 상대 경로 정의
html_file_path = "html/index.html"

# 파일이 존재하는지 확인
if not os.path.exists(html_file_path):
    st.error(f"오류: {html_file_path} 경로에 파일이 존재하지 않습니다.")
    st.info("app.py와 같은 위치에 'html' 폴더를 만들고, 그 안에 'index.html' 파일을 저장했는지 확인해주세요.")
else:
    # HTML 파일 내용 읽기
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Streamlit에 HTML 코드 렌더링
    # height와 scrolling은 필요에 따라 조절할 수 있습니다.
    components.html(html_content, height=1000, scrolling=True)
