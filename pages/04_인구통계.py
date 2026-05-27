import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
page_title="인구통계",
layout="wide"
)

st.title("📊 행정구별 연령 인구 분석")

# 한글 설정

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# CSV 읽기

df = pd.read_csv("population.csv", encoding="cp949")

# 첫 번째 컬럼 = 지역명

region_col = df.columns[0]

# 연령 컬럼 찾기

age_cols = []
ages = []

for col in df.columns:

```
if "세" in col:

    num = "".join(filter(str.isdigit, col))

    if num != "":
        age_cols.append(col)
        ages.append(int(num))
```

# 지역 선택

region = st.selectbox(
"행정구 선택",
df[region_col].unique()
)

# 데이터 선택

selected = df[df[region_col] == region]

# 인구 데이터

values = selected[age_cols].iloc[0]

values = values.astype(str).str.replace(",", "")

values = pd.to_numeric(values)

# 그래프

fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(
ages,
values,
color="hotpink",
linewidth=3
)

ax.set_title(f"{region} 연령별 인구수")

ax.set_xlabel("나이")
ax.set_ylabel("인구수")

# 10살 단위 선

ax.set_xticks(range(0, max(ages)+1, 10))

ax.grid(
True,
axis="x",
linestyle="--",
alpha=0.5
)

st.pyplot(fig)
