import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(
    page_title="서울 관광지 TOP10",
    page_icon="🇰🇷",
    layout="centered"
)

st.title("🇰🇷 외국인들이 좋아하는 서울 관광지 TOP10")
st.write("서울 인기 관광지를 지도에서 확인해보세요!")

# 관광지 데이터
places = {
    "경복궁": {
        "lat": 37.5796,
        "lon": 126.9770,
        "station": "🚉 경복궁역 3호선",
        "fun": [
            "한복 입고 사진 찍기",
            "궁궐 내부 관람하기",
            "국립민속박물관 가기",
            "서촌 카페거리 산책"
        ]
    },

    "명동": {
        "lat": 37.5637,
        "lon": 126.9827,
        "station": "🚉 명동역 4호선",
        "fun": [
            "길거리 음식 먹기",
            "화장품 쇼핑하기",
            "야간 거리 구경하기",
            "대형 쇼핑몰 방문"
        ]
    },

    "남산서울타워": {
        "lat": 37.5512,
        "lon": 126.9882,
        "station": "🚉 명동역 4호선",
        "fun": [
            "서울 야경 감상",
            "케이블카 타기",
            "사랑의 자물쇠 보기",
            "남산 산책하기"
        ]
    },

    "북촌한옥마을": {
        "lat": 37.5826,
        "lon": 126.9830,
        "station": "🚉 안국역 3호선",
        "fun": [
            "전통 한옥 구경",
            "감성 사진 찍기",
            "한옥 카페 가기",
            "골목 산책하기"
        ]
    },

    "홍대거리": {
        "lat": 37.5563,
        "lon": 126.9220,
        "station": "🚉 홍대입구역 2호선",
        "fun": [
            "버스킹 공연 보기",
            "빈티지 쇼핑하기",
            "감성 카페 가기",
            "코인노래방 가기"
        ]
    },

    "롯데월드타워": {
        "lat": 37.5125,
        "lon": 127.1025,
        "station": "🚉 잠실역 2호선",
        "fun": [
            "서울스카이 전망대",
            "롯데월드 즐기기",
            "백화점 쇼핑하기",
            "석촌호수 산책"
        ]
    },

    "광장시장": {
        "lat": 37.5704,
        "lon": 126.9996,
        "station": "🚉 종로5가역 1호선",
        "fun": [
            "육회 먹기",
            "빈대떡 먹기",
            "시장 음식 투어",
            "전통시장 구경"
        ]
    },

    "DDP": {
        "lat": 37.5665,
        "lon": 127.0092,
        "station": "🚉 동대문역사문화공원역",
        "fun": [
            "전시회 관람하기",
            "야간 조명 보기",
            "사진 찍기",
            "패션몰 쇼핑"
        ]
    },

    "한강공원": {
        "lat": 37.5289,
        "lon": 126.9326,
        "station": "🚉 여의나루역 5호선",
        "fun": [
            "치킨 먹기",
            "한강 라면 먹기",
            "자전거 타기",
            "피크닉 즐기기"
        ]
    },

    "인사동": {
        "lat": 37.5743,
        "lon": 126.9856,
        "station": "🚉 안국역 3호선",
        "fun": [
            "전통 기념품 쇼핑",
            "전통차 마시기",
            "골목 구경하기",
            "길거리 공연 보기"
        ]
    }
}

# 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11
)

# 파란색 마커 추가
for name, info in places.items():

    popup_text = f"""
    <b style='font-size:16px;'>{name}</b><br>
    {info['station']}
    """

    folium.Marker(
        location=[info["lat"], info["lon"]],
        popup=popup_text,
        tooltip=name,
        icon=folium.Icon(
            color="blue",
            icon="info-sign"
        )
    ).add_to(m)

# 지도 크기 60% 정도로 축소
st_folium(
    m,
    width=650,
    height=400
)

st.divider()

# 관광지 선택
selected_place = st.selectbox(
    "📍 관광지를 선택하세요",
    list(places.keys())
)

data = places[selected_place]

# 선택 정보 출력
st.subheader(f"✨ {selected_place}")

st.markdown(f"""
## {data['station']}

### 🎡 놀거리
- {data['fun'][0]}
- {data['fun'][1]}
- {data['fun'][2]}
- {data['fun'][3]}
""")
