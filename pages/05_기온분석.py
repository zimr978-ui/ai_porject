import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

st.set_page_config(
    page_title="서울 기온 분석",
    page_icon="🌡️",
    layout="wide"
)

st.title("🌡️ 서울 날짜별 기온 분석")

uploaded_file = st.file_uploader(
    "seoul.csv 파일을 업로드하세요",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file, encoding='cp949')
    except:
        df = pd.read_csv(uploaded_file, encoding='utf-8')

    # 컬럼명 정리
    df.columns = [
        "날짜",
        "지점",
        "지점명",
        "평균기온",
        "최저기온",
        "최고기온"
    ]

    # 날짜 변환
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

    selected = df[
        (df["월"] == month) &
        (df["일"] == day)
    ].copy()

    selected = selected.dropna(
        subset=["최고기온", "최저기온"]
    )

    if len(selected) == 0:
        st.warning("해당 날짜의 데이터가 없습니다.")
        st.stop()

    selected = selected.sort_values("연도")

    st.subheader(f"{month}월 {day}일 연도별 기온")

    fig, ax = plt.subplots(figsize=(14, 6))

    years = selected["연도"].values
    highs = selected["최고기온"].values
    lows = selected["최저기온"].values

    # 최고기온 무지개색 선
    rainbow = cm.rainbow(np.linspace(0, 1, len(years)))

    for i in range(len(years)-1):
        ax.plot(
            years[i:i+2],
            highs[i:i+2],
            color=rainbow[i],
            linewidth=2
        )

    # 최고기온 점
    ax.scatter(
        years,
        highs,
        c=np.linspace(0, 1, len(years)),
        cmap="rainbow",
        s=25,
        label="최고기온"
    )

    # 최저기온
    ax.plot(
        years,
        lows,
        color="lightblue",
        linewidth=2.5,
        marker="o",
        markersize=4,
        label="최저기온"
    )

    ax.set_title(
        f"{month}월 {day}일 연도별 최고·최저기온",
        fontsize=16
    )

    ax.set_xlabel("연도")
    ax.set_ylabel("기온(℃)")
    ax.grid(alpha=0.3)

    ax.legend()

    st.pyplot(fig)

    st.dataframe(
        selected[
            ["연도", "최저기온", "최고기온"]
        ].reset_index(drop=True),
        use_container_width=True
    )

else:
    st.info("CSV 파일을 업로드하세요.")
