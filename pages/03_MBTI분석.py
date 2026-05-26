import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="전 세계 MBTI 분포 시각화",
    page_icon="📊",
    layout="centered"
)

# 데이터 로드 함수 (캐싱 처리로 속도 향상)
@st.cache_data
def load_data():
    # 데이터 파일 읽기
    df = pd.read_csv('countriesMBTI_16types.csv')
    return df

try:
    df = load_data()
    
    st.title("🌏 국가별 MBTI 분포 분석기")
    st.write("원하는 국가를 선택하면 16가지 MBTI 유형별 비율을 확인할 수 있습니다.")
    st.markdown("---")

    # 1. 국가 선택 셀렉트박스
    country_list = sorted(df['Country'].unique())
    selected_country = st.selectbox(
        "🔎 분석할 국가를 선택하세요:",
        options=country_list,
        index=country_list.index("South Korea") if "South Korea" in country_list else 0
    )

    # 선택된 국가의 데이터 추출
    country_data = df[df['Country'] == selected_country].iloc[0]
    
    # MBTI 유형과 비율만 분리 (Country 열 제외)
    mbti_types = df.columns[1:]
    percentages = [country_data[mbti] * 100 for mbti in mbti_types]  # 백분율(%)로 변환

    # 데이터프레임으로 변환 후 정렬 (비율이 높은 순서대로 그래프를 그리거나 원본 순서 유지)
    # 여기서는 원본 MBTI 순서를 유지하면서 1등을 찾습니다.
    plot_df = pd.DataFrame({
        'MBTI': mbti_types,
        'Percentage': percentages
    })
    
    # 1등(최댓값) 인덱스 찾기
    max_idx = plot_df['Percentage'].idxmax()
    max_val = plot_df['Percentage'].max()
    max_mbti = plot_df.loc[max_idx, 'MBTI']

    # 2. 색상 지정 알고리즘 (1등은 노란색, 나머지는 하늘색에서 흐려지는 그라데이션)
    # 1등을 제외한 나머지 데이터들의 순위를 매겨 그라데이션 강도를 결정합니다.
    plot_df['Rank'] = plot_df['Percentage'].rank(ascending=False, method='first')
    
    colors = []
    for idx, row in plot_df.iterrows():
        if idx == max_idx:
            # 1등: 밝고 선명한 노란색
            colors.append('#FFD700') 
        else:
            # 나머지: 비율이 높을수록 선명한 하늘색(#2196F3), 낮을수록 흐려지게(투명도 조색)
            # 최댓값 대비 상대적 크기로 투명도(alpha) 결정 (최소 0.15 보장)
            alpha = max(0.15, row['Percentage'] / max_val * 0.9)
            colors.append(f'rgba(33, 150, 243, {alpha})')

    # 3. Plotly 막대그래프 생성
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=plot_df['MBTI'],
        y=plot_df['Percentage'],
        marker_color=colors,
        marker_line_color='rgba(0,0,0,0.1)',
        marker_line_width=1,
        text=[f"{val Gold" if idx == max_idx else f"{val:.1f}%" for idx, val in enumerate(plot_df['Percentage'])],
        textposition='outside',
        hovertemplate="<b>%{x}</b>: %{y:.2f}%<extra></extra>"
    ))

    # 그래프 레이아웃 설정
    fig.update_layout(
        title=dict(
            text=f"📊 <b>{selected_country}</b>의 MBTI 유형별 비율",
            x=0,
            font=dict(size=18)
        ),
        xaxis=dict(title="MBTI 유형", categoryorder='array', categoryarray=mbti_types),
        yaxis=dict(title="비율 (%)", suffix="%", range=[0, max_val * 1.2]), # 텍스트가 잘리지 않도록 여유 공간 확보
        margin=dict(l=40, r=40, t=60, b=40),
        plot_bgcolor='rgba(255,255,255,0.9)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=500
    )

    # 스트림릿에 그래프 출력
    st.plotly_chart(fig, use_container_width=True)

    # 4. 상위 요약 정보 서머리 박스
    st.markdown("### 💡 주요 인사이트")
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"🏆 **가장 많은 유형:** **{max_mbti}** ({max_val:.2f}%)")
    with col2:
        min_idx = plot_df['Percentage'].idxmin()
        st.warning(f"🦄 **가장 희귀한 유형:** **{plot_df.loc[min_idx, 'MBTI']}** ({plot_df.loc[min_idx, 'Percentage']:.2f}%)")

except FileNotFoundError:
    st.error("❌ `countriesMBTI_16types.csv` 파일을 찾을 수 없습니다. 스크립트와 같은 경로에 업로드했는지 확인해주세요.")
except Exception as e:
    st.error(f"오류가 발생했습니다: {e}")
