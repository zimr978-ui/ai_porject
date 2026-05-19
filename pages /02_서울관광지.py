import streamlit as st
import folium
from streamlit_folium import st_folium

# 1. 페이지 설정
st.set_page_config(
    page_title="외국인이 사랑하는 서울 관광지 Top 10",
    page_icon="🗼",
    layout="wide"
)

st.title("📌 외국인 선호 서울 주요 관광지 Top 10")
st.markdown("외국인 관광객들에게 가장 인기 있는 서울의 대표 명소 10곳을 지도에서 확인해보세요!")

# 2. 서울 Top 10 관광지 데이터 (이름, 위도, 경도, 설명)
seoul_attractions = [
    {"name": "경복궁", "lat": 37.5796, "lon": 126.9770, "desc": "조선 시대의 주궁, 한복 체험의 성지"},
    {"name": "N서울타워 (남산타워)", "lat": 37.5512, "lon": 126.9882, "desc": "서울 시내를 한눈에 내려다보는 전망대와 사랑의 자물쇠"},
    {"name": "명동 거리", "lat": 37.5634, "lon": 126.9846, "desc": "K-뷰티, 쇼핑, 그리고 다양한 길거리 음식의 천국"},
    {"name": "북촌 한옥마을", "lat": 37.5829, "lon": 126.9835, "desc": "전통 한옥의 고즈넉한 미를 느낄 수 있는 실제 거주 지역"},
    {"name": "홍대 거리", "lat": 37.5567, "lon": 126.9237, "desc": "젊음과 인디 문화, 버스킹 공연과 K-패션의 중심지"},
    {"name": "인사동 쌈지길", "lat": 37.5743, "lon": 126.9848, "desc": "한국 전통 공예품, 갤러리, 전통 찻집이 모여있는 곳"},
    {"name": "광장시장", "lat": 37.5701, "lon": 126.9996, "desc": "넷플릭스에도 소개된 빈대떡, 마약김밥 등 로컬 푸드 핫플"},
    {"name": "동대문디자인플라자 (DDP)", "lat": 37.5668, "lon": 127.0094, "desc": "자하 하디드가 설계한 미래지향적 건축물과 패션의 중심"},
    {"name": "강남역 거리", "lat": 37.4980, "lon": 127.0276, "desc": "싸이의 강남스타일, 트렌디한 고층 빌딩과 현대적 번화가"},
    {"name": "반포 한강공원", "lat": 37.5114, "lon": 126.9964, "desc": "달빛무지개분수와 '한강에서 라면 먹기' 감성을 즐기는 곳"}
]

# 3. 레이아웃 분할 (좌측: 설명 및 선택, 우측: 지도)
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📍 명소 리스트")
    # 사용자가 리스트에서 선택하면 지도 중심을 이동시킬 수 있도록 선택박스 구현
    selected_place = st.selectbox(
        "자세히 보고 싶은 명소를 선택하세요:",
        ["전체 보기"] + [place["name"] for place in seoul_attractions]
    )
    
    st.write("---")
    # 선택된 명소에 대한 설명 표시
    if selected_place == "전체 보기":
        st.write("지도에 표시된 마커를 클릭하면 상세 설명을 볼 수 있습니다.")
    else:
        for place in seoul_attractions:
            if place["name"] == selected_place:
                st.markdown(f"### **{place['name']}**")
                st.write(place["desc"])

with col2:
    # 지도 초기 중심 설정 (서울 중심부)
    map_center = [37.555, 126.985]
    zoom_level = 12
    
    # 특정 장소가 선택되었다면 그 장소로 지도 중심과 줌인 변경
    if selected_place != "전체 보기":
        for place in seoul_attractions:
            if place["name"] == selected_place:
                map_center = [place["lat"], place["lon"]]
                zoom_level = 14

    # 폴리움 지도 생성
    m = folium.Map(location=map_center, zoom_start=zoom_level)

    # 마커 추가
    for place in seoul_attractions:
        popup_content = f"<strong>{place['name']}</strong><br><br>{place['desc']}"
        folium.Marker(
            location=[place["lat"], place["lon"]],
            popup=folium.Popup(popup_content, max_width=250),
            tooltip=place["name"],
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)

    # 스트림릿에 지도 렌더링
    st_folium(m, width="100%", height=500)
