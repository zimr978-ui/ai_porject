import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(
    page_title="전 세계 MBTI 데이터 분석기",
    page_icon="📊",
    layout="centered"
)

# 데이터 로드 함수 (캐싱 처리)
@st.cache_data
def load_data():
    df = pd.read_csv('countriesMBTI_16types.csv')
    return df

try:
    df = load_data()
    # 첫 번째 열(Country)을 제외한 모든 MBTI 컬럼 가져오기
    mbti_types = list(df.columns[1:])

    st.title("🌏 전 세계 MBTI 대시보드")
    st.write("국가별 MBTI 순위와 MBTI별 상위 국가 리스트를 직관적으로 확인하세요.")
    st.markdown("---")

    # 상단 기능 선택 라디오 버튼
    analysis_mode = st.radio(
        "📊 분석 모드를 선택하세요:",
        options=["국가별 MBTI 분포 보기", "MBTI별 상위 10개국 보기"],
        horizontal=True
    )

    # -------------------------------------------------------------------------
    # MODE 1: 국가별 MBTI 분포 보기 (1등부터 내림차순 정렬)
    # -------------------------------------------------------------------------
    if analysis_mode == "국가별 MBTI 분포 보기":
        country_list = sorted(df['Country'].unique())
        
        # 기본 선택값을 South Korea로 설정 시도
        default_idx = 0
        if "South Korea" in country_list:
            default_idx = country_list.index("South Korea")
            
        selected_country = st.selectbox(
            "🔎 분석할 국가를 선택하세요:",
            options=country_list,
            index=default_idx
        )

        # 해당 국가 데이터 추출
        country_data = df[df['Country'] == selected_country].iloc[0]
        percentages = []
        for mbti in mbti_types:
            percentages.append(float(country_data[mbti]) * 100)

        # 데이터프레임 생성 및 비율 기준 내림차순 정렬
        plot_df = pd.DataFrame({
            'MBTI': mbti_types,
            'Percentage': percentages
        })
        plot_df = plot_df.sort_values(by='Percentage', ascending=False).reset_index(drop=True)
        
        max_val = plot_df['Percentage'].max()
        max_mbti = plot_df.loc[0, 'MBTI']

        # 색상 및 텍스트 레이블 배열 생성 (구조를 완전히 분리하여 SyntaxError 원천 차단)
        colors = []
        text_labels = []
        
        for idx, row in plot_df.iterrows():
            val = row['Percentage']
            if idx == 0:
                colors.append('#FFD700')  # 1등: 골드 노란색
                text_labels.append(f"🥇 {val:.1f}%")
            else:
                # 1등 대비 상대적 크기로 투명도(alpha) 계산하여 그라데이션 적용
                alpha = max(0.2, (val / max_val) * 0.9)
                colors.append(f'rgba(46, 125, 50, {alpha})')  # 초록색 그라데이션
                text_labels.append(f"{val:.1f}%")

        # Plotly 막대그래프 구현
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=plot_df['MBTI'],
            y=plot_df['Percentage'],
            marker_color=colors,
            marker_line_color='rgba(0,0,0,0.1)',
            marker_line_width=1,
            text=text_labels,
            textposition='outside',
            hovertemplate="<b>%{x}</b>: %{y:.2f}%<extra></extra>"
        ))

        fig.update_layout(
            title=dict(text=f"📊 <b>{selected_country}</b>의 MBTI 비율 순위 (높은 순)", font=dict(size=18)),
            xaxis=dict(title="MBTI 유형", type='category', automargin=True, fixedrange=True),
            yaxis=dict(title="비율 (%)", suffix="%", range=[0, max_val * 1.2], automargin=True, fixedrange=True),
            margin=dict(l=50, r=50, t=70, b=50),
            plot_bgcolor='rgba(255,255,255,0.9)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=520
        )
        st.plotly_chart(fig, use_container_width=True)

        st.info(f"🏆 **{selected_country}**에서 가장 흔한 MBTI 유형은 **{max_mbti}** ({max_val:.2f}%) 입니다.")

    # -------------------------------------------------------------------------
    # MODE 2: MBTI별 상위 10개국 보기 (1등부터 내림차순 정렬)
    # -------------------------------------------------------------------------
    else:
        # MBTI 선택 박스는 알파벳 정렬로 제공
        sorted_mbti_list = sorted(mbti_types)
        default_mbti_idx = 0
        if "INFP" in sorted_mbti_list:
            default_mbti_idx = sorted_mbti_list.index("INFP")
            
        selected_mbti = st.selectbox(
            "🔮 궁금한 MBTI 유형을 선택하세요:",
            options=sorted_mbti_list,
            index=default_mbti_idx
        )

        # 선택한 MBTI 데이터 추출 및 백분율 변환
        mbti_df = df[['Country', selected_mbti]].copy()
        mbti_df['Converted_Pct'] = mbti_df[selected_mbti] * 100
        
        # 높은 순 정렬 후 상위 10개국 추출
        top10_df = mbti_df.sort_values(by='Converted_Pct', ascending=False).head(10).reset_index(drop=True)
        max_val = top10_df['Converted_Pct'].max()

        # 색상 및 텍스트 레이블 배열 생성
        colors = []
        text_labels = []
        
        for idx, row in top10_df.iterrows():
            val = row['Converted_Pct']
            if idx == 0:
                colors.append('#FFD700')  # 1등 국가: 골드 노란색
                text_labels.append(f"🥇 {val:.1f}%")
            else:
                alpha = max(0.2, (val / max_val) * 0.9)
                colors.append(f'rgba(46, 125, 50, {alpha})')  # 초록색 그라데이션
                text_labels.append(f"{val:.1f}%")

        # Plotly 막대그래프 구현
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=top10_df['Country'],
            y=top10_df['Converted_Pct'],
            marker_color=colors,
            marker_line_color='rgba(0,0,0,0.1)',
            marker_line_width=1,
            text=text_labels,
            textposition='outside',
            hovertemplate="<b>%{x}</b>: %{y:.2f}%<extra></extra>"
        ))

        fig.update_layout(
            title=dict(text=f"👑 전 세계 <b>{selected_mbti}</b> 비율 상위 10개국", font=dict(size=18)),
            xaxis=dict(title="국가", type='category', automargin=True, fixedrange=True),
            yaxis=dict(title="비율 (%)", suffix="%", range=[0, max_val * 1.2], automargin=True, fixedrange=True),
            margin=dict(l=50, r=50, t=70, b=50),
            plot_bgcolor='rgba(255,255,255,0.9)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=520
        )
        st.plotly_chart(fig, use_container_width=True)

        top_country = top10_df.loc[0, 'Country']
        st.success(f"👑 지구상에서 **{selected_mbti}** 성향 비율이 가장 높은 국자는 **{top_country}** ({max_val:.2f}%) 입니다.")

except FileNotFoundError:
    st.error("❌ `countriesMBTI_16types.csv` 파일을 찾을 수 없습니다. 파일이 스크립트와 동일한 위치에 있는지 확인하세요.")
except Exception as e:
    st.error(f"앱 실행 중 오류가 발생했습니다: {e}")
