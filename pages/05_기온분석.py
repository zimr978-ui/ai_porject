import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

st.set_page_config(
    page_title="서울 날짜별 기온 분석",
    page_icon="🌡️",
    layout="wide"
)

st.title("🌡️ 서울 날짜별 최고·최저기온 분석")

uploaded_file = st.file_uploader(
    "seoul.csv 업로드",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file, encoding="cp949")
    except:
        df = pd.read_csv(uploaded_file, encoding="utf-8")

    # 날짜 문자열 정리
    df["날짜"] = (
        df["날짜"]
        .astype(str)
        .str.replace("\t", "", regex=False)
        .str.strip()
    )

    # 날짜형 변환
    df["날짜"] = pd.to_datetime(df["날짜"])

    # 연월일 생성
    df["연도"] = df["날짜"].dt.year
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day

    month = st.sidebar.selectbox("월 선택", range(1, 13))
    day = st.sidebar.selectbox("일 선택", range(1, 32))

    selected = df[
        (df["월"] == month) &
        (df["일"] == day)
    ].copy()

    selected = selected.dropna(
        subset=["최저기온(℃)", "최고기온(℃)"]
    )

    selected = selected.sort_values("연도")

    if len(selected) == 0:
        st.warning("해당 날짜 데이터가 없습니다.")
        st.stop()

    years = selected["연도"].values
    highs = selected["최고기온(℃)"].values
    lows = selected["최저기온(℃)"].values

    fig, ax = plt.subplots(figsize=(15, 7))

    rainbow = cm.rainbow(
        np.linspace(0, 1, len(years))
    )

    # 최고기온 무지개색
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
        s=25,
        label="최고기온"
    )

    # 최저기온 연파랑
    ax.plot(
        years,
        lows,
        color="lightblue",
        linewidth=3,
        marker="o",
        markersize=4,
        label="최저기온"
    )

    ax.set_title(
        f"{month}월 {day}일 연도별 최고·최저기온"
    )

    ax.set_xlabel("연도")
    ax.set_ylabel("기온(℃)")
    ax.grid(alpha=0.3)

    ax.legend()

    st.pyplot(fig)

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
