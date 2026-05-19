import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Seoul Top 10",
    page_icon="📍",
    layout="wide"
)

st.title("🇰🇷 Foreigners' Favorite Places in Seoul")
st.write("Top 10 popular places in Seoul displayed with Folium map.")

places = [
    ["Gyeongbokgung Palace", 37.5796, 126.9770],
    ["Myeongdong", 37.5637, 126.9827],
    ["N Seoul Tower", 37.5512, 126.9882],
    ["Bukchon Hanok Village", 37.5826, 126.9830],
    ["Hongdae Street", 37.5563, 126.9220],
    ["Lotte World Tower", 37.5125, 127.1025],
    ["Gwangjang Market", 37.5704, 126.9996],
    ["DDP", 37.5665, 127.0092],
    ["Han River Park", 37.5289, 126.9326],
    ["Insadong", 37.5743, 126.9856]
]

m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

for place in places:
    folium.Marker(
        location=[place[1], place[2]],
        popup=place[0],
        tooltip=place[0]
    ).add_to(m)

st_folium(m, width=1200, height=600)

st.subheader("📌 Top 10 List")

for i, place in enumerate(places, start=1):
    st.write(f"{i}. {place[0]}")
