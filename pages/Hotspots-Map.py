import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("🌍 Fraud Hotspots Map")

def map_data():
    m = folium.Map(location=[22.5, 78.9], zoom_start=5)

    locations = [
        (28.61, 77.20, "Delhi"),
        (19.07, 72.87, "Mumbai"),
        (12.97, 77.59, "Bangalore"),
        (17.38, 78.48, "Hyderabad")
    ]

    for lat, lon, name in locations:
        folium.CircleMarker(
            [lat, lon],
            radius=10,
            popup=name,
            color="red",
            fill=True
        ).add_to(m)

    return m

st_folium(map_data(), width=1100, height=600)