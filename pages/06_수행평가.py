import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="청소년 비만 솔루션 AI",
    page_icon="💪",
    layout="wide"
)

# --------------------
# 제목
# --------------------

st.title("💪 청소년 비만 솔루션 AI")

st.markdown("""
### 📊 청소년 건강 관리 도우미

건강 상태를 확인하고,
나에게 맞는 운동 · 식품 · 도서 · 진로를 추천받아보자!
""")

# --------------------
# BMI 계산기
# --------------------

st.header("🧮 BMI 계산기")

col1, col2 = st.columns(2)

with col1:
    height = st.number_input(
        "키(cm)",
        min_value=100,
        max_value=220,
        value=170
    )

with col2:
    weight = st.number_input(
        "몸무게(kg)",
        min_value=20,
        max_value=200,
        value=65
    )

height_m = height / 100
bmi = weight / (height_m ** 2)

st.metric("현재 BMI", round(bmi, 1))

if bmi < 18.5:
    obesity_type = "저체중형"
    color = "🟦"

elif bmi < 23:
    obesity_type = "정상형"
    color = "🟩"

elif bmi < 25:
    obesity_type = "과체중형"
    color = "🟨"

else:
    obesity_type = "비만형"
    color = "🟥"

st.success(f"{color} 현재 상태 : {obesity_type}")

# --------------------
# 비만 유형 TOP3
# --------------------

st.header("📈 청소년 비만 유형 TOP3")

top3 = pd.DataFrame(
    {
        "유형": [
            "운동부족형",
            "식습관불균형형",
            "복부비만형"
        ],
        "비율": [
            42,
            34,
            24
        ]
    }
)

fig, ax = plt.subplots(figsize=(7,4))

ax.bar(
    top3["유형"],
    top3["비율"]
)

ax.set_ylabel("비율(%)")
ax.set_title("청소년 비만 유형 TOP3")

st.pyplot(fig)

# --------------------
# 추천 데이터
# --------------------

recommend = {
    "저체중형": {
        "exercise":["🏋️ 근력운동", "🚴 자전거"],
        "food":["🥚 계란", "🥛 우유"],
        "book":"내 몸 혁명",
        "book_review":"건강한 생활습관을 쉽고 재미있게 알려주는 책!",
        "movie":"포크스 오버 나이브스",
        "movie_review":"식습관이 건강에 미치는 영향을 보여주는 다큐!"
    },

    "정상형": {
        "exercise":["🏸 배드민턴", "🚶 걷기"],
        "food":["🍎 사과", "🥗 샐러드"],
        "book":"나는 질병 없이 살기로 했다",
        "book_review":"생활습관의 중요성을 쉽게 이해할 수 있어요!",
        "movie":"게임 체인저스",
        "movie_review":"운동과 영양의 관계를 흥미롭게 알려주는 영화!"
    },

    "과체중형": {
        "exercise":["🏊 수영", "🏃 조깅"],
        "food":["🥦 브로콜리", "🍌 바나나"],
        "book":"당신은 뇌를 고칠 수 있다",
        "book_review":"건강한 음식 선택의 중요성을 알려주는 책!",
        "movie":"슈퍼 사이즈 미",
        "movie_review":"패스트푸드가 건강에 미치는 영향을 보여주는 작품!"
    },

    "비만형": {
        "exercise":["🚶 빠르게 걷기", "🚴 자전거"],
        "food":["🥗 샐러드", "🍎 사과"],
        "book":"내 몸 혁명",
        "book_review":"작은 습관 변화가 건강을 크게 바꿀 수 있음을 알려주는 책!",
        "movie":"슈퍼 사이즈 미",
        "movie_review":"건강한 식습관의 중요성을 다시 생각하게 하는 영화!"
    }
}

data = recommend[obesity_type]

# --------------------
# 운동 추천
# --------------------

st.header("🏃 추천 운동")

for item in data["exercise"]:
    st.success(item)

# --------------------
# 식품 추천
# --------------------

st.header("🥗 추천 식품")

for item in data["food"]:
    st.success(item)

# --------------------
# 책 추천
# --------------------

st.header("📚 추천 도서")

st.info(data["book"])

st.write("📝 한줄 서평")
st.write(data["book_review"])

# --------------------
# 영화 추천
# --------------------

st.header("🎬 추천 영화")

st.info(data["movie"])

st.write("⭐ 한줄 영화평")
st.write(data["movie_review"])

# --------------------
# 진로 추천
# --------------------

st.header("🎯 건강 관련 진로 추천")

career_df = pd.DataFrame(
    {
        "진로": [
            "운동처방사",
            "스포츠 트레이너",
            "영양사",
            "보건교사",
            "간호사"
        ],
        "추천 학과": [
            "스포츠과학과",
            "체육학과",
            "식품영양학과",
            "보건교육학과",
            "간호학과"
        ],
        "어울리는 성격": [
            "분석적이고 책임감 있는 사람",
            "활동적이고 긍정적인 사람",
            "꼼꼼하고 배려심 있는 사람",
            "친절하고 의사소통이 좋은 사람",
            "봉사정신이 강한 사람"
        ]
    }
)

st.dataframe(
    career_df,
    use_container_width=True
)

# --------------------
# 건강 미션
# --------------------

st.header("🔥 오늘의 건강 미션")

missions = [
    "🚶 30분 걷기",
    "💧 물 6잔 이상 마시기",
    "🍎 과일 1개 먹기",
    "📵 자기 전 스마트폰 줄이기",
    "😴 7시간 이상 수면"
]

for m in missions:
    st.write(m)

st.balloons()

st.success(
    "👏 건강은 하루아침에 만들어지지 않아요! 오늘의 작은 실천이 미래를 바꿉니다!"
)
