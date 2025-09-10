import streamlit as st
import os

def load_html(file_path):
    """
    지정된 경로의 HTML 파일을 읽어와서 반환합니다.
    """
    if not os.path.exists(file_path):
        st.error(f"Error: The file at {file_path} was not found.")
        return ""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Streamlit 페이지 설정
st.set_page_config(
    page_title="게임 봇 분석 연구 웹페이지",
    layout="wide"
)

st.title("Streamlit 기반 웹페이지")

# htmls 폴더 안의 index.html 파일 경로 설정
html_file_path = os.path.join(os.path.dirname(__file__), "htmls", "index.html")

# HTML 코드 로드 및 표시
html_code = load_html(html_file_path)

if html_code:
    st.components.v1.html(html_code, height=1200, scrolling=True)

# 하단에 추가적인 내용이나 Streamlit 위젯을 배치할 수 있습니다.
st.markdown("---")
st.markdown("### Streamlit에서 렌더링된 웹페이지")
st.info("이 페이지는 HTML 파일을 불러와서 표시한 것입니다. `app.py` 파일을 수정하여 다른 기능들을 추가할 수 있습니다.")
