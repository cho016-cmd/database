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
# Assuming app.py and the htmls folder are in the same location.
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
    """A function that reads a specified HTML file and returns its content"""
    file_path = os.path.join(html_dir, file_name)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # HTML 내용을 안전하게 처리
            return content
    except FileNotFoundError:
        st.error(f"오류: '{file_name}' 파일을 찾을 수 없습니다. 경로를 확인해주세요.")
        st.error(f"Error: '{file_name}' file not found. Please check the path.")
        return None
    except Exception as e:
        st.error(f"파일 읽기 중 오류가 발생했습니다: {str(e)}")
        st.error(f"An error occurred while reading the file: {str(e)}")
        return None

def create_sidebar():
    """사이드바 생성"""
    with st.sidebar:
        st.title("📄 HTML 파일 뷰어")
        st.markdown("---")
        
        # 파일 선택 섹션
        st.subheader("📁 파일 선택")
        
        # 파일 옵션과 라벨 생성
        file_options = list(HTML_FILES.keys())
        file_labels = [f"{HTML_FILES[file]['icon']} {HTML_FILES[file]['title']}" for file in file_options]
        
        # 카테고리별로 그룹화해서 표시
        categories = {}
        for file_name, info in HTML_FILES.items():
            category = info['category']
            if category not in categories:
                categories[category] = []
            categories[category].append((file_name, info))
        
        # 카테고리별 표시 (버튼으로 즉시 이동)
        for category, files in categories.items():
            st.markdown(f"**{category}**")
            for file_name, info in files:
                if st.button(f"{info['icon']} {info['title']}", key=f"btn_{file_name}"):
                    st.session_state.selected_file = file_name
                    # 쿼리 파라미터로 현재 파일을 반영하면 외부에서 직접 링크로 열 수 있음
                    st.experimental_set_query_params(file=file_name)
                    st.rerun()
            st.markdown("")
        
        # 쿼리 파라미터에서 초기 파일 확인
        params = st.experimental_get_query_params()
        param_file = params.get('file', [None])[0]
        if 'selected_file' not in st.session_state:
            if param_file in HTML_FILES:
                st.session_state.selected_file = param_file
            else:
                st.session_state.selected_file = file_options[0]
        
        # 현재 시간 표시
        st.markdown("---")
        st.markdown(f"🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        return st.session_state.selected_file

def display_file_info(selected_file):
    """선택된 파일 정보 표시 - 애니메이션 적용"""
    info = HTML_FILES[selected_file]
    
    # 애니메이션 헤더 섹션
    st.markdown(f"""
    <div class="main-header">
        <div class="icon-container" style="font-size: 4rem; margin-bottom: 1rem;">
            {info['icon']}
        </div>
        <h1 style="margin: 0; font-size: 2.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            {info['title']}
        </h1>
        <p style="margin: 0.5rem 0 0 0; font-size: 1.2rem; opacity: 0.9;">
            {info['description']}
        </p>
        <div style="margin-top: 1rem;">
            <span style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem;">
                📁 {info['category']}
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 추가 정보 카드들
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="file-card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🎨</div>
            <h4 style="margin: 0; color: #667eea;">인터랙티브</h4>
            <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">실시간 미리보기</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="file-card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚡</div>
            <h4 style="margin: 0; color: #764ba2;">빠른 로딩</h4>
            <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">최적화된 성능</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="file-card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔧</div>
            <h4 style="margin: 0; color: #f093fb;">커스터마이징</h4>
            <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">설정 가능</p>
        </div>
        """, unsafe_allow_html=True)

def main():
    # 세션 상태 초기화
    if 'fullscreen_mode' not in st.session_state:
        st.session_state.fullscreen_mode = False
    
    # 사이드바에서 파일 선택
    selected_file = create_sidebar()
    
    # 메인 컨텐츠 영역 - 고급 애니메이션과 그라데이션 스타일
    st.markdown("""
    <style>
    /* 전역 애니메이션 설정 */
    * {
        animation-duration: 0.3s;
        animation-timing-function: ease-in-out;
    }
    
    /* 그라데이션 배경 애니메이션 */
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    @keyframes shimmer {
        0% { background-position: -200px 0; }
        100% { background-position: calc(200px + 100%) 0; }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    
    /* 메인 헤더 - 그라데이션 애니메이션 */
    .main-header {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c, #4facfe, #00f2fe);
        background-size: 400% 400%;
        animation: gradientShift 8s ease infinite, fadeInUp 0.8s ease-out;
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        animation: shimmer 2s infinite;
    }
    
    /* 파일 카드 - 호버 애니메이션 */
    .file-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #667eea;
        margin-bottom: 1rem;
        transition: all 0.3s ease;
        animation: slideInLeft 0.6s ease-out;
        position: relative;
        overflow: hidden;
    }
    
    .file-card:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border-left-color: #f093fb;
    }
    
    .file-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.1), transparent);
        transition: left 0.5s;
    }
    
    .file-card:hover::after {
        left: 100%;
    }
    
    /* 아이콘 애니메이션 */
    .icon-container {
        animation: float 3s ease-in-out infinite, pulse 2s ease-in-out infinite;
        display: inline-block;
    }
    
    /* 버튼 애니메이션 */
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        border: none;
        border-radius: 25px;
        color: white;
        font-weight: bold;
        transition: all 0.3s ease;
        animation: fadeInUp 0.5s ease-out;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) scale(1.05);
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
        animation: bounce 0.6s ease;
    }
    
    .stButton > button:active {
        transform: translateY(0) scale(0.98);
    }
    
    /* 사이드바 스타일 */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        animation: gradientShift 10s ease infinite;
    }
    
    /* 슬라이더 스타일 */
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #667eea, #764ba2);
    }
    
    /* 체크박스 스타일 */
    .stCheckbox > label > div[data-checked="true"] {
        background: linear-gradient(45deg, #667eea, #764ba2);
        animation: pulse 0.3s ease;
    }
    
    /* 스피너 커스터마이징 */
    .stSpinner > div {
        border-top-color: #667eea;
        animation: spin 1s linear infinite;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* 라디오 버튼 애니메이션 */
    .stRadio > div > label > div[data-testid="stMarkdownContainer"] {
        transition: all 0.3s ease;
        padding: 0.5rem;
        border-radius: 10px;
        animation: fadeInUp 0.4s ease-out;
    }
    
    .stRadio > div > label > div[data-testid="stMarkdownContainer"]:hover {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
        transform: translateX(5px);
    }
    
    /* 경고 메시지 애니메이션 */
    .stAlert {
        animation: slideInLeft 0.5s ease-out, pulse 0.5s ease-out 0.5s;
        border-radius: 15px;
    }
    
    /* 정보 박스 애니메이션 */
    .stInfo {
        background: linear-gradient(135deg, #e3f2fd, #bbdefb);
        border-radius: 15px;
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* 에러 메시지 애니메이션 */
    .stError {
        background: linear-gradient(135deg, #ffebee, #ffcdd2);
        border-radius: 15px;
        animation: bounce 0.6s ease-out;
    }
    
    /* 성공 메시지 애니메이션 */
    .stSuccess {
        background: linear-gradient(135deg, #e8f5e8, #c8e6c9);
        border-radius: 15px;
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* 제목 애니메이션 */
    h1 {
        animation: fadeInUp 0.8s ease-out;
        background: linear-gradient(45deg, #667eea, #764ba2, #f093fb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* 서브헤더 애니메이션 */
    h2 {
        animation: slideInLeft 0.6s ease-out;
    }
    
    h3 {
        animation: fadeInUp 0.5s ease-out;
    }
    
    /* 전체 페이지 페이드인 */
    .main .block-container {
        animation: fadeInUp 0.8s ease-out;
    }
    
    /* 스크롤바 스타일링 */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: linear-gradient(180deg, #f1f1f1, #e1e1e1);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #667eea, #764ba2);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #764ba2, #f093fb);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # 파일 정보 표시 (미리보기 전용 모드가 아닌 경우에만)
    # 쿼리에서 mode=html 이면 미리보기 전용 강제
    params = st.experimental_get_query_params()
    force_html_mode = params.get('mode', [''])[0] == 'html'
    minimal_mode = force_html_mode or HTML_FILES.get(selected_file, {}).get('minimal', False) or selected_file == 'index.html'
    
    # 로딩 인디케이터와 함께 HTML 로드
    with st.spinner(f"{HTML_FILES[selected_file]['title']}을(를) 불러오는 중..."):
        html_code = load_html(selected_file)

    if html_code:
        # 미리보기 전용 모드면 추가 UI 없이 HTML만 렌더
        if minimal_mode:
            try:
                components.html(html_code, height=900, scrolling=True)
            except Exception as e:
                st.error("❌ HTML 렌더링 중 오류가 발생했습니다")
                with st.expander("오류 세부사항", expanded=False):
                    st.code(str(e))
            # 더 이상 다른 UI를 표시하지 않음
            st.stop()

        # (기존대로 상세 UI 표시)
        display_file_info(selected_file)
        # HTML 렌더링 섹션
        st.subheader("🖥️ 미리보기")
        
        # 애니메이션 컨트롤 패널
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f8f9fa, #e9ecef); 
                    padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;
                    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                    animation: fadeInUp 0.6s ease-out;">
            <h3 style="margin: 0 0 1rem 0; color: #667eea; text-align: center;">
                ⚙️ 미리보기 설정
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
        
        with col1:
            st.markdown("""
            <div style="text-align: center; margin-bottom: 1rem;">
                <span style="color: #667eea; font-weight: bold;">📏 화면 높이</span>
            </div>
            """, unsafe_allow_html=True)
            height = st.slider("", min_value=600, max_value=1600, value=1000, step=100, label_visibility="collapsed")
        
        with col2:
            st.markdown("""
            <div style="text-align: center; margin-bottom: 1rem;">
                <span style="color: #764ba2; font-weight: bold;">📜 스크롤 설정</span>
            </div>
            """, unsafe_allow_html=True)
            scrolling = st.checkbox("", value=True, label_visibility="collapsed")
            st.markdown("""
            <div style="text-align: center; font-size: 0.9rem; color: #666;">
                스크롤 허용
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style="text-align: center; margin-bottom: 1rem;">
                <span style="color: #f093fb; font-weight: bold;">🔄 새로고침</span>
            </div>
            """, unsafe_allow_html=True)
            if st.button("새로고침", key="refresh_btn"):
                st.rerun()
        
        with col4:
            st.markdown("""
            <div style="text-align: center; margin-bottom: 1rem;">
                <span style="color: #00f2fe; font-weight: bold;">🖥️ 전체화면</span>
            </div>
            """, unsafe_allow_html=True)
            if st.button("전체화면", key="fullscreen_btn"):
                st.session_state.fullscreen_mode = True
                st.rerun()
        
        st.markdown("---")
        
        # 전체화면 모드 처리
        if st.session_state.fullscreen_mode:
            st.markdown(f"""
            <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; 
                        background: white; z-index: 9999; padding: 20px; box-sizing: border-box;
                        overflow: hidden;">
                <div style="display: flex; flex-direction: column; height: 100%;">
                    <div style="display: flex; justify-content: space-between; align-items: center; 
                                margin-bottom: 20px; padding: 10px; background: #f8f9fa; border-radius: 10px;">
                        <h2 style="margin: 0; color: #667eea;">
                            🖥️ 전체화면 모드 - {HTML_FILES[selected_file]['title']}
                        </h2>
                        <button onclick="exitFullscreen()" 
                                style="background: #dc3545; color: white; border: none; 
                                       padding: 10px 20px; border-radius: 5px; cursor: pointer;">
                            ❌ 전체화면 종료
                        </button>
                    </div>
                    <div style="flex: 1; border: 2px solid #667eea; border-radius: 10px; overflow: hidden;">
                        <div style="width: 100%; height: 100%; overflow: auto;">
                            {html_code}
                        </div>
                    </div>
                </div>
            </div>
            
            <script>
            function exitFullscreen() {{
                // 전체화면 종료를 위해 페이지 새로고침
                window.location.reload();
            }}
            </script>
            """, unsafe_allow_html=True)
            
            # 전체화면 종료 버튼 추가
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                if st.button("❌ 전체화면 종료", key="exit_fullscreen", type="primary"):
                    st.session_state.fullscreen_mode = False
                    st.rerun()
            
            # 전체화면 모드에서는 다른 컨텐츠를 숨김
            st.stop()
        
        # 일반 모드 HTML 렌더링 - 더 큰 화면으로 표시
        st.markdown("""
        <div style="border: 3px solid #667eea; border-radius: 15px; 
                    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
                    overflow: hidden; margin: 20px 0;">
        """, unsafe_allow_html=True)
        
        try:
            components.html(
                html_code, 
                height=height, 
                scrolling=scrolling
            )
        except Exception as e:
            st.error("❌ HTML 렌더링 중 오류가 발생했습니다")
            with st.expander("오류 세부사항", expanded=False):
                st.code(str(e))
            
            st.warning("📄 HTML 내용 미리보기:")
            with st.expander("HTML 소스 코드", expanded=False):
                st.code(html_code[:1000] + "..." if len(html_code) > 1000 else html_code)
        
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("❌ 파일을 불러올 수 없습니다.")
        st.info("💡 파일이 존재하는지 확인해주세요.")

if __name__ == "__main__":
    main()

