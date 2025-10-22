import streamlit as st
import os
import streamlit.components.v1 as components
from datetime import datetime

# 페이지 설정
st.set_page_config(
    page_title="HTML 파일 뷰어",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# app.py와 htmls 폴더가 같은 위치에 있다고 가정합니다.
html_dir = os.path.join(os.path.dirname(__file__), 'htmls')

# HTML 파일 메타데이터
HTML_FILES = {
    'index.html': {
        'title': '급식 만족도 개선 연구',
        'description': '데이터 분석 기반의 학교 급식 만족도 향상 방안 연구 계획서',
        'category': '연구 계획서',
        'icon': '🍽️'
    },
    'index2.html': {
        'title': '첸토 게임 시뮬레이터',
        'description': 'Python을 활용한 첸토 게임 시뮬레이션 프로그램',
        'category': '게임 시뮬레이터',
        'icon': '🎮'
    },
    'index3.html': {
        'title': 'Python 코드 실행 시뮬레이터',
        'description': '로또 번호 생성기를 시뮬레이션하는 Python 코드 데모',
        'category': '코드 데모',
        'icon': '🐍'
    },
    'index4.html': {
        'title': '실시간 버스 도착 알림 시스템',
        'description': '공공데이터 API를 활용한 실시간 버스 도착 알림 시스템 개발 계획서',
        'category': '연구 계획서',
        'icon': '🚌'
    },
    'index5.html': {
        'title': '상황 기반 최적 정글 경로 분석기',
        'description': '상대 정글러 상성을 고려해 최적의 초반 정글 동선을 계산하고 인터랙티브하게 시각화합니다.',
        'category': '게임 도구',
        'icon': '🗺️'
    }
}

def load_html(file_name):
    """지정된 HTML 파일을 읽어 그 내용을 반환하는 함수"""
    file_path = os.path.join(html_dir, file_name)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        st.error(f"오류: '{file_name}' 파일을 찾을 수 없습니다. 경로를 확인해주세요.")
        return None
    except Exception as e:
        st.error(f"파일 읽기 중 오류가 발생했습니다: {str(e)}")
        return None

def create_sidebar():
    """사이드바 생성 - 파일 버튼 클릭 시 즉시 이동"""
    with st.sidebar:
        st.title("📄 HTML 파일 뷰어")
        st.markdown("---")
        file_options = list(HTML_FILES.keys())

        # 카테고리별 그룹화
        categories = {}
        for file_name, info in HTML_FILES.items():
            category = info['category']
            categories.setdefault(category, []).append((file_name, info))

        for category, files in categories.items():
            st.markdown(f"**{category}**")
            for file_name, info in files:
                if st.button(f"{info['icon']} {info['title']}", key=f"btn_{file_name}"):
                    st.session_state.selected_file = file_name
                    st.experimental_set_query_params(file=file_name)
                    st.rerun()
            st.markdown("")

        # 쿼리파라미터에서 초기 파일 설정
        params = st.experimental_get_query_params()
        param_file = params.get('file', [None])[0]
        if 'selected_file' not in st.session_state:
            if param_file in HTML_FILES:
                st.session_state.selected_file = param_file
            else:
                st.session_state.selected_file = file_options[0]

        st.markdown("---")
        st.markdown(f"🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        return st.session_state.selected_file

def main():
    selected_file = create_sidebar()

    # HTML 로드
    with st.spinner(f"{HTML_FILES[selected_file]['title']}을(를) 불러오는 중..."):
        html_code = load_html(selected_file)

    if not html_code:
        st.error("❌ 파일을 불러올 수 없습니다.")
        st.info("💡 파일이 존재하는지 확인해주세요.")
        return

    # index.html 또는 mode=html 쿼리일 때도 동일하게 HTML만 렌더.
    # 불필요한 데코레이션/설정/카드/애니메이션 전부 제거하여 바로 렌더링합니다.
    try:
        components.html(html_code, height=900, scrolling=True)
    except Exception as e:
        st.error("❌ HTML 렌더링 중 오류가 발생했습니다")
        with st.expander("오류 세부사항", expanded=False):
            st.code(str(e))
        st.warning("📄 HTML 내용 미리보기:")
        with st.expander("HTML 소스 코드", expanded=False):
            st.code(html_code[:2000] + "..." if len(html_code) > 2000 else html_code)

if __name__ == "__main__":
    main()

