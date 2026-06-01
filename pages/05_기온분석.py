import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="서울 기온 예측",
    page_icon="🌡️",
    layout="wide"
)

plt.rcParams["axes.unicode_minus"] = False

st.title("🌡️ 서울 날짜별 기온 분석 및 미래 예측")

uploaded_file = st.file_uploader(
    "seoul.csv 파일 업로드",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file, encoding="cp949")
    except:
        df = pd.read_csv(uploaded_file, encoding="utf-8")

    # 날짜 정리
    df["날짜"] = (
        df["날짜"]
        .astype(str)
        .str.replace("\t", "", regex=False)
        .str.strip()
    )

    df["날짜"] = pd.to_datetime(df["날짜"])

    df["연도"] = df["날짜"].dt.year
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day

    st.sidebar.header("날짜 선택")

    month = st.sidebar.selectbox(
        "월",
        range(1, 13),
        index=7
    )

    day = st.sidebar.selectbox(
        "일",
        range(1, 32),
        index=0
    )

    future_year = st.sidebar.number_input(
        "예측 연도",
        min_value=2020,
        max_value=2100,
        value=2030
    )

    selected = df[
        (df["월"] == month) &
        (df["일"] == day)
    ].copy()

    selected = selected.dropna(
        subset=["최저기온(℃)", "최고기온(℃)"]
    )

    selected = selected.sort_values("연도")

    if len(selected) < 10:
        st.warning("학습 데이터가 부족합니다.")
        st.stop()

    years = selected["연도"].values
    highs = selected["최고기온(℃)"].values
    lows = selected["최저기온(℃)"].values

    # 머신러닝 학습
    X = years.reshape(-1, 1)

    high_model = LinearRegression()
    high_model.fit(X, highs)

    low_model = LinearRegression()
    low_model.fit(X, lows)

    pred_high = high_model.predict([[future_year]])[0]
    pred_low = low_model.predict([[future_year]])[0]

    st.subheader(
        f"📈 {month}월 {day}일 기온 예측 ({future_year}년)"
    )

    col1, col2 = st.columns(2)

    col1.metric(
        "예상 최고기온",
        f"{pred_high:.1f}℃"
    )

    col2.metric(
        "예상 최저기온",
        f"{pred_low:.1f}℃"
    )

    # 예측점 추가
    years_all = np.append(years, future_year)
    highs_all = np.append(highs, pred_high)
    lows_all = np.append(lows, pred_low)

    fig, ax = plt.subplots(figsize=(15, 7))

    rainbow = cm.rainbow(
        np.linspace(0, 1, len(years))
    )

    # 실제 최고기온
    for i in range(len(years)-1):
        ax.plot(
            years[i:i+2],
            highs[i:i+2],
            color=rainbow[i],
            linewidth=2
        )

    ax.scatter(
        years,
        highs,
        c=np.linspace(0, 1, len(years)),
        cmap="rainbow",
        s=30,
        label="실제 최고기온"
    )

    # 실제 최저기온
    ax.plot(
        years,
        lows,
        color="lightblue",
        linewidth=3,
        marker="o",
        markersize=4,
        label="실제 최저기온"
    )

    # 예측점
    ax.scatter(
        future_year,
        pred_high,
        marker="*",
        s=300,
        label=f"{future_year} 최고기온 예측"
    )

    ax.scatter(
        future_year,
        pred_low,
        marker="D",
        s=200,
        label=f"{future_year} 최저기온 예측"
    )

    ax.axvline(
        future_year,
        linestyle="--",
        alpha=0.4
    )

    ax.set_title(
        f"{month}월 {day}일 연도별 기온 및 미래 예측"
    )

    ax.set_xlabel("연도")
    ax.set_ylabel("기온(℃)")

    ax.grid(alpha=0.3)

    ax.legend()

    st.pyplot(fig)

    st.subheader("데이터")

    st.dataframe(
        selected[
            [
                "연도",
                "최저기온(℃)",
                "최고기온(℃)"
            ]
        ],
        use_container_width=True
    )

    st.info(
        "예측은 선형회귀(Linear Regression)를 사용한 단순 장기추세 예측입니다."
    )
