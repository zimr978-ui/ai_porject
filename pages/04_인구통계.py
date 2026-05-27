# app.py

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="서울 인구 연령별 분석",
    layout="wide"
)

st.title("📊 서울 행정구별 연령 인구 분석")
st.markdown("행정구를 선택하면 연령별 인구 분포를 꺾은선 그래프로 보여줍니다.")

# -----------------------------
# 한글 폰트 설정
# -----------------------------
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv('population(1).csv', encoding='cp949')


df = load_data()

# -----------------------------
# 행정구 컬럼
# -----------------------------
region_col = df.columns[0]

# -----------------------------
# 연령 컬럼 찾기
# -----------------------------
age_columns = []
age_labels = []

for col in df.columns:
    if col.endswith('세'):
        age = ''.join(filter(str.isdigit, col))

        if age:
            age_columns.append(col)
            age_labels.append(int(age))

# -----------------------------
# 행정구 선택
# -----------------------------
regions = df[region_col].unique()

selected_region = st.selectbox(
    '행정구를 선택하세요',
    regions
)

# -----------------------------
# 데이터 추출
# -----------------------------
selected_data = df[df[region_col] == selected_region]

if not selected_data.empty:

    population_values = (
        selected_data[age_columns]
        .iloc[0]
        .replace(',', '', regex=True)
    )

    population_values = pd.to_numeric(population_values, errors='coerce')

    # -----------------------------
    # 그래프
    # -----------------------------
    fig, ax = plt.subplots(figsize=(14, 6))

    ax.plot(
        age_labels,
        population_values,
        color='hotpink',
        linewidth=3,
        marker='o'
    )

    ax.set_title(f'{selected_region} 연령별 인구 분포', fontsize=18)
    ax.set_xlabel('나이', fontsize=14)
    ax.set_ylabel('인구수', fontsize=14)

    # 10살 단위 구분선
    ax.set_xticks(range(0, max(age_labels) + 1, 10))
    ax.grid(True, axis='x', linestyle='--', alpha=0.7)

    plt.tight_layout()

    st.pyplot(fig)

    # 데이터 표
    chart_df = pd.DataFrame({
        '나이': age_labels,
        '인구수': population_values
    })

    st.subheader('📋 연령별 인구 데이터')
    st.dataframe(chart_df, use_container_width=True)

else:
    st.warning('데이터를 찾을 수 없습니다.')
```

---

# requirements.txt

```txt
streamlit
pandas
matplotlib
```

---

# 스트림릿 클라우드 배포 방법

## 1. 파일 구성

아래처럼 파일을 구성하세요.

```text
project/
├── app.py
├── requirements.txt
└── population(1).csv
```

---

## 2. GitHub 업로드

* GitHub 저장소 생성
* 파일 업로드

---

## 3. Streamlit Cloud 배포

* Streamlit Cloud 접속
* GitHub 저장소 연결
* app.py 선택
* Deploy 클릭

---

## 4. 실행 결과

기능:

* 행정구 선택 가능
* 연령별 인구 꺾은선 그래프 출력
* 핫핑크 색상 적용
* 10살 단위 세로 구분선 표시
* 한글 깨짐 방지
