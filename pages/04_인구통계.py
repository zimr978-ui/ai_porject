import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# -----------------------------
# 한글 폰트 설정
# -----------------------------
plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="서울 인구 연령 분석",
    layout="wide"
)

st.title("서울시 행정구별 연령 인구 분석")
st.write("행정구를 선택하면 연령별 인구 분포를 볼 수 있습니다.")

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():

    # CP949 우선 시도
    try:
        df = pd.read_csv(
            "population.csv",
            encoding="cp949"
        )

    # 실패 시 UTF-8 시도
    except:
        df = pd.read_csv(
            "population.csv",
            encoding="utf-8"
        )

    return df


df = load_data()

# -----------------------------
# 컬럼 설정
# -----------------------------
region_col = df.columns[0]

# 지역 이름 정리
regions = (
    df[region_col]
    .astype(str)
    .str.replace("서울특별시 ", "", regex=False)
)

# -----------------------------
# 행정구 선택
# -----------------------------
selected_region = st.selectbox(
    "행정구 선택",
    regions
)

# 선택된 행
selected_row = df[regions == selected_region]

# -----------------------------
# 연령 / 인구수 처리
# -----------------------------
ages = list(range(101))

# 숫자 안전 변환
population_data = selected_row.iloc[0, 3:104]

populations = (
    pd.to_numeric(
        population_data,
        errors="coerce"
    )
    .fillna(0)
    .astype(int)
    .values
)

# -----------------------------
# 그래프 생성
# -----------------------------
fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(
    ages,
    populations,
    color="hotpink",
    linewidth=3
)

# 제목
ax.set_title(
    f"{selected_region} 연령별 인구 분포",
    fontsize=18
)

# 축 라벨
ax.set_xlabel("나이", fontsize=14)
ax.set_ylabel("인구수", fontsize=14)

# x축 10살 단위
ax.set_xticks(range(0, 101, 10))

# 세로 구분선
ax.grid(
    axis="x",
    linestyle="--",
    alpha=0.5
)

# 디자인
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Streamlit 출력
st.pyplot(fig)

# -----------------------------
# 데이터 표
# -----------------------------
st.subheader("연령별 인구 데이터")

chart_df = pd.DataFrame({
    "나이": ages,
    "인구수": populations
})

st.dataframe(
    chart_df,
    use_container_width=True
)
