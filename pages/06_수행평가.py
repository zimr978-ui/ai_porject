import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="청소년 비만 솔루션",
    page_icon="💪",
    layout="wide"
)

st.title("💪 청소년 비만 솔루션 TOP3")
st.markdown("### 📊 나에게 맞는 건강 관리 방법과 진로까지 확인해보자!")

# ------------------------
# 비만 유형 데이터
# ------------------------
obesity_data = {
    "복부비만형": {
        "rate": 42,
        "desc": "배 주변에 지방이 집중되는 유형",
        "exercise": [
            "🚶 빠르게 걷기",
            "🚴 자전거 타기"
        ],
        "food": [
            "🥗 샐러드",
            "🍎 사과"
        ],
        "book": {
            "title": "내 몸 혁명",
            "review": "작은 습관 변화가 건강을 크게 바꾼다는 점을 쉽게 알려주는 책!"
        },
        "career": {
            "major": "체육교육과, 스포츠과학과",
            "personality": "활동적이고 사람들과 어울리는 것을 좋아하는 성격"
        }
    },

    "운동부족형": {
        "rate": 35,
        "desc": "활동량 부족으로 체중이 증가하는 유형",
        "exercise": [
            "🏸 배드민턴",
            "🏊 수영"
        ],
        "food": [
            "🥚 삶은 계란",
            "🍌 바나나"
        ],
        "book": {
            "title": "나는 질병없이 살기로 했다",
            "review": "건강한 생활습관의 중요성을 쉽게 설명해주는 책!"
        },
        "career": {
            "major": "체육학과, 레저스포츠학과",
            "personality": "도전정신이 강하고 새로운 경험을 좋아하는 성격"
        }
    },

    "식습관불균형형": {
        "rate": 23,
        "desc": "패스트푸드와 간식 섭취가 많은 유형",
        "exercise": [
            "🏃 조깅",
            "🕺 댄스 운동"
        ],
        "food": [
            "🥛 저지방 우유",
            "🥦 브로콜리"
        ],
        "book": {
            "title": "당신은 뇌를 고칠 수 있다",
            "review": "음식과 건강의 관계를 흥미롭게 알려주는 책!"
        },
        "career": {
            "major": "식품영양학과, 보건학과",
            "personality": "꼼꼼하고 사람을 돕는 것을 좋아하는 성격"
        }
    }
}

# ------------------------
# TOP3 차트
# ------------------------
st.header("📈 청소년 비만 유형 TOP3")

df = pd.DataFrame({
    "유형": list(obesity_data.keys()),
    "비율": [v["rate"] for v in obesity_data.values()]
})

fig, ax = plt.subplots(figsize=(8,4))
ax.bar(df["유형"], df["비율"])
ax.set_ylabel("비율(%)")
ax.set_title("청소년 비만 유형 TOP3")

st.pyplot(fig)

# ------------------------
# 유형 선택
# ------------------------
st.header("🔍 나의 유형 알아보기")

selected = st.selectbox(
    "비만 유형을 선택하세요",
    list(obesity_data.keys())
)

info = obesity_data[selected]

st.subheader(f"✨ {selected}")
st.info(info["desc"])

# ------------------------
# 운동 추천
# ------------------------
st.subheader("🏃 추천 운동")

for ex in info["exercise"]:
    st.success(ex)

# ------------------------
# 식품 추천
# ------------------------
st.subheader("🥗 추천 식품")

for food in info["food"]:
    st.success(food)

# ------------------------
# 추천 이유
# ------------------------
st.subheader("💡 왜 추천할까?")

if selected == "복부비만형":
    st.write("배 주변 지방 감소와 체지방 연소에 도움을 줄 수 있어요!")

elif selected == "운동부족형":
    st.write("활동량을 늘려 기초대사량 향상에 도움이 될 수 있어요!")

else:
    st.write("건강한 식습관 형성과 칼로리 조절에 도움을 줄 수 있어요!")

# ------------------------
# 도서 추천
# ------------------------
st.subheader("📚 건강 도서 추천")

st.markdown(
    f"""
**도서명:** {info['book']['title']}

📝 한줄 서평

{info['book']['review']}
"""
)

# ------------------------
# 진로 추천
# ------------------------
st.subheader("🎯 추천 진로")

st.write(f"📖 추천 학과 : **{info['career']['major']}**")

st.write(
    f"😀 적합한 성격 : **{info['career']['personality']}**"
)

# ------------------------
# 건강 미션
# ------------------------
st.header("🔥 오늘의 건강 미션")

mission = [
    "🚶 30분 걷기",
    "🥤 물 6잔 이상 마시기",
    "🍎 과일 1개 먹기",
    "📵 자기 전 스마트폰 사용 줄이기"
]

for m in mission:
    st.write(m)

st.success("👏 작은 습관이 큰 변화를 만듭니다! 오늘부터 도전해보세요!")
