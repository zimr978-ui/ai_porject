import streamlit as st
import folium
from streamlit_folium import st_folium

# 1. 페이지 설정
st.set_page_config(
    page_title="서울 외국인 인기 관광지 Top 10",
    page_icon="🗺️",
    layout="wide"
)

# 2. 타이틀 및 앱 소개
st.title("🇰🇷 외국인이 가장 사랑하는 서울 관광지 Top 10")
st.write("스트림릿과 폴리움(Folium) 지도를 활용하여 외국인 관광객에게 가장 인기 있는 서울의 명소 10곳을 소개합니다.")

# 3. 데이터 정의 (관광지 이름, 위도, 경도, 설명)
tourist_spots = [
    {"name": "경복궁", "lat": 37.5796, "lon": 126.9770, "desc": "한국의 대표적인 조선시대 법궁, 한복 체험 명소"},
    {"name": "N서울타워 (남산타워)", "lat": 37.5512, "lon": 126.9882, "desc": "서울 시내를 한눈에 내려다볼 수 있는 야경 명소 및 사랑의 자물쇠"},
    {"name": "명동 쇼핑거리", "lat": 37.5621, "lon": 126.9850, "desc": "K-뷰티, 길거리 음식, 쇼핑의 중심지"},
    {"name": "북촌한옥마을", "lat": 37.5829, "lon": 126.9835, "desc": "실제 주민들이 거주하는 전통 한옥 양식의 보존 구역"},
    {"name": "인사동", "lat": 37.5744, "lon": 126.9875, "desc": "한국 랜드마크 굿즈, 전통 찻집, 골동품과 화랑이 가득한 곳"},
    {"name": "동대문디자인플라자 (DDP)", "lat": 37.5665, "lon": 127.0092, "desc": "자하 하디드가 설계한 세계 최대 규모의 3차원 비정형 건축물"},
    {"name": "홍대 거리", "lat": 37.5568, "lon": 126.9239, "desc": "젊음과 인디 문화, 버스킹, 이색 카페와 밤문화의 중심지"},
    {"name": "롯데월드타워 & 몰", "lat": 37.5126, "lon": 127.1025, "desc": "세계 5위 높이의 초고층 빌딩과 서울스카이 전망대"},
    {"name": "강남역 & 코엑스 (별마당도서관)", "lat": 37.5119, "lon": 127.0589, "desc": "강남 스타일의 상징이자 인스타 명소인 거대 오픈 도서관"},
    {"name": "광장시장", "lat": 37.5701, "lon": 127.0010, "desc": "넷플릭스에도 소개된 빈대떡, 마약김밥 등 한국 길거리 음식의 천국"}
]

# 4. 화면 레이아웃 분할 (왼쪽: 지도, 오른쪽: 상세 정보 카드)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🗺️ 서울 관광 지도")
    
    # 서울 중심부 좌표로 기본 지도 생성
    m = folium.Map(location=[37.555, 126.985], zoom_start=12)
    
    # 마커 추가
    for idx, spot in enumerate(tourist_spots, 1):
        popup_content = f"<b>{idx}. {spot['name']}</b><br><span style='color:gray;'>{spot['desc']}</span>"
        folium.Marker(
            location=[spot['lat'], spot['lon']],
            popup=folium.Popup(popup_content, max_width=300),
            tooltip=f"{idx}. {spot['name']}",
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)
    
    # 스트림릿 앱에 Folium 지도 렌더링
    st_folium(m, width="100%", height=550)

with col2:
    st.subheader("📌 명소 리스트")
    # 오른쪽에 깔끔하게 리스트 형태로 정보 제공
    for idx, spot in enumerate(tourist_spots, 1):
        with st.expander(f"{idx}. {spot['name']}"):
            st.write(f"**설명:** {spot['desc']}")
            st.write(f"**좌표:** 위도 {spot['lat']}, 경도 {spot['lon']}")

# 푸터
st.caption("Data source: 가상 트렌드 및 한국관광공사 외국인 선호도 종합 | Made with Streamlit🎈")
