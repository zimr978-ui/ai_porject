# 서울 인기 관광지 TOP10 지도 앱 (Folium + Streamlit)

## app.py

```python
import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Seoul Top 10 🇰🇷",
    page_icon="📍",
    layout="wide"
)

st.title("🇰🇷 외국인들이 좋아하는 서울 TOP 10")
st.write("Folium 지도로 서울 인기 관광지를 표시한 스트림릿 앱")

# 서울 인기 장소 데이터
places = [
    {
        "name": "경복궁",
        "lat": 37.5796,
        "lon": 126.9770,
        "desc": "조선 시대의 대표 궁궐"
    },
    {
        "name": "명동",
        "lat": 37.5637,
        "lon": 126.9827,
        "desc": "쇼핑과 길거리 음식의 성지"
    },
    {
        "name": "남산서울타워",
        "lat": 37.5512,
        "lon": 126.9882,
        "desc": "서울 야경 명소"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.5826,
        "lon": 126.9830,
        "desc": "전통 한옥 감성"
    },
    {
        "name": "홍대거리",
        "lat": 37.5563,
        "lon": 126.9220,
        "desc": "젊은 감성과 버스킹 거리"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.5125,
        "lon": 127.1025,
        "desc": "서울 초고층 랜드마크"
    },
    {
        "name": "광장시장",
        "lat": 37.5704,
        "lon": 126.9996,
        "desc": "한국 길거리 음식 체험"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.5665,
        "lon": 127.0092,
        "desc": "미래적인 건축 디자인"
    },
    {
        "name": "한강공원",
        "lat": 37.5289,
        "lon": 126.9326,
        "desc": "치킨과 라면 먹기 좋은 곳"
    },
    {
        "name": "인사동",
        "lat": 37.5743,
        "lon": 126.9856,
        "desc": "전통 문화와 기념품 거리"
    }
]

# 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

# 마커 추가
for place in places:
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=f"<b>{place['name']}</b><br>{place['desc']}",
        tooltip=place["name"],
        icon=folium.Icon(color="red", icon="star")
    ).add_to(m)

# 지도 출력
st_folium(m, width=1200, height=600)

st.subheader("📌 장소 리스트")

for idx, place in enumerate(places, start=1):
    st.write(f"{idx}. {place['name']} - {place['desc']}")
```

---

# requirements.txt

```txt
streamlit
folium
streamlit-folium
```

---

# 파일 구조

```txt
프로젝트폴더/
 ├─ app.py
 └─ requirements.txt
```

---

# Streamlit Cloud 배포 방법

1. GitHub 저장소 생성
2. `app.py` 업로드
3. `requirements.txt` 업로드
4. Streamlit Cloud에서 GitHub 연결
5. Deploy 누르면 바로 실행됨
