import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# 페이지 설정
# -----------------------------------
st.set_page_config(
    page_title="서울 인구 분석",
    layout="wide"
)

st.title("📊 서울 행정구별 연령 인구 분석")

# -----------------------------------
# 한글 설정
# -----------------------------------
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# -----------------------------------
# 데이터 불러오기
# -----------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("population(1).csv", encoding="cp949")
    return df

df = load_data()

# -----------------------------------
# 첫 번째 컬럼 = 행정구
# -----------------------------------
region_col = df.columns[0]

# -----------------------------------
# 연령 컬럼 추출
# -----------------------------------
age_columns = []
age_numbers = []

for col in df.columns:

    if col.endswith("세"):

        number = ''.join(filter(str.isdigit, col))

        if number != "":
            age_columns.append(col)
            age_numbers.append(int(number))

# -----------------------------------
# 행정구 선택
# -----------------------------------
regions = df[region_col].unique()

selected_region = st.selectbox(
    "행정구를 선택하세요",
    regions
)

# -----------------------------------
# 선택 데이터
# -----------------------------------
selected_df = df[df[region_col] == selected_region]

# -----------------------------------
# 그래프
# -----------------------------------
if len(selected_df) > 0:

    values = selected_df[age_columns].iloc[0]

    # 쉼표 제거
    values = values.astype(str).str.replace(",", "")

    # 숫자 변환
    values = pd.to_numeric(values)

    fig, ax = plt.subplots(figsize=(14, 6))

    ax.plot(
        age_numbers,
        values,
        color="hotpink",
        linewidth=3,
        marker="o"
    )

    ax.set_title(f"{selected_region} 연령별 인구수", fontsize=20)
    ax.set_xlabel("나이", fontsize=14)
    ax.set_ylabel("인구수", fontsize=14)

    # 10살 단위 구분선
    ax.set_xticks(range(0, max(age_numbers) + 1, 10))
    ax.grid(True, axis="x", linestyle="--", alpha=0.5)

    plt.tight_layout()

    st.pyplot(fig)

    # 표 출력
    result_df = pd.DataFrame({
        "나이": age_numbers,
        "인구수": values
    })

    st.subheader("📋 데이터 보기")
    st.dataframe(result_df, use_container_width=True)

else:
    st.error("데이터를 찾을 수 없습니다.")
