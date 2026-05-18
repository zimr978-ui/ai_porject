import streamlit as st
import pandas as pd
import numpy as np

# 1. 페이지 설정
st.set_page_config(
    page_title="나의 첫 스트림릿 대시보드",
    page_icon="📊",
    layout="wide"
)

# 2. 앱 제목 및 설명
st.title("📊 스트림릿 클라우드 테스트 앱")
st.markdown("""
이 앱은 **스트림릿 클라우드(Streamlit Cloud)**에서 완벽하게 작동하는 대시보드 예시입니다.
사이드바에서 옵션을 조절하거나 데이터를 확인해 보세요!
""")

st.divider()

# 3. 사이드바 구성
st.sidebar.header("⚙️ 설정 매뉴얼")
user_name = st.sidebar.text_input("이름을 입력하세요", "홍길동")
sample_data_size = st.sidebar.slider("생성할 샘플 데이터 개수", 10, 100, 50)

# 웰컴 메시지 데이터 정제
st.sidebar.success(f"환영합니다, {user_name}님!")

# 4. 메인 화면: 데이터 생성 및 시각화
st.subheader("📈 무작위 트렌드 데이터 분석")

# 샘플 데이터 생성 (시간 흐름에 따른 가상 데이터)
chart_data = pd.DataFrame(
    np.random.randn(sample_data_size, 3),
    columns=['A 제품', 'B 제품', 'C 제품']
).cumsum() # 누적 합계로 트렌드 생성

# 레이아웃 분할 (컬럼 사용)
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("**제품별 트렌드 차트**")
    st.line_chart(chart_data)

with col2:
    st.markdown("**최근 데이터 요약 (상위 5개)**")
    st.dataframe(chart_data.tail(5))
    
    # 간단한 메트릭 표시
    latest_a = round(chart_data['A 제품'].iloc[-1], 2)
    latest_b = round(chart_data['B 제품'].iloc[-1], 2)
    st.metric(label="A 제품 최종 스코어", value=latest_a, delta=round(latest_a - chart_data['A 제품'].iloc[-2], 2))
    st.metric(label="B 제품 최종 스코어", value=latest_b, delta=round(latest_b - chart_data['B 제품'].iloc[-2], 2))

st.divider()

# 5. 파일 업로드 기능 테스트
st.subheader("📁 내 파일 업로드 테스트")
uploaded_file = st.file_uploader("CSV 파일을 선택하세요", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("파일 업로드 성공!")
    st.dataframe(df.head())
else:
    st.info("여기에 CSV 파일을 드래그앤드롭하여 본인의 데이터를 확인해볼 수 있습니다.")
