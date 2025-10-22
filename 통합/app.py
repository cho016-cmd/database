import streamlit as st
import os
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="HTML 파일 뷰어",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# app.py와 htmls 폴더가 같은 위치에 있다고 가정합니다.
html_dir = os.path.join(os.path.dirname(__file__), 'htmls')

# HTML 파일 메타데이터 (표시용이 아니고 파일 목록 관리를 위해 유지)
HTML_FILES = {
    'index.html': {},
    'index2.html': {},
    'index3.html': {},
    'index4.html': {},
    'index5.html': {}
}

def load_html(file_name):
    file_path = os.path.join(html_dir, file_name)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return None

def create_sidebar():
    """사이드바: 파일명 버튼만 표시 (메타데이터나 설명 전혀 없음)"""
    with st.sidebar:
        st.title("HTML 뷰어")
        st.markdown("---")

        # 파일 목록: HTML_FILES 키 우선, 없으면 htmls 디렉터리 스캔
        files = list(HTML_FILES.keys())
        if not files:
            try:
                files = [f for f in os.listdir(html_dir) if f.endswith('.html')]
            except Exception:
                files = []

        # 쿼리파라미터로 초기 파일 설정 (st.query_params 사용)
        params = st.query_params
        param_file = params.get('file', [None])[0] if isinstance(params, dict) else None
        if 'selected_file' not in st.session_state:
            if param_file in files:
                st.session_state.selected_file = param_file
            elif files:
                st.session_state.selected_file = files[0]
            else:
                st.session_state.selected_file = None

        # 파일 버튼 (파일명만)
        for fname in files:
            label = fname  # 필요하면 파일명 대신 아이콘만으로 바꿀 수 있음
            if st.button(label, key=f"btn_{fname}"):
                st.session_state.selected_file = fname
                st.experimental_set_query_params(file=fname)
                st.rerun()

        st.markdown("---")

        return st.session_state.get('selected_file')

def main():
    selected_file = create_sidebar()

    if not selected_file:
        st.error("열 수 있는 HTML 파일이 없습니다.")
        return

    html_code = load_html(selected_file)
    if not html_code:
        st.error(f"오류: '{selected_file}' 파일을 불러올 수 없습니다.")
        return

    # 추가 UI 없이 HTML만 바로 렌더
    try:
        components.html(html_code, height=900, scrolling=True)
    except Exception:
        st.error("HTML 렌더링 중 오류가 발생했습니다.")

if __name__ == "__main__":
    main()

