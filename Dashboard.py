import streamlit as st
import folium
from streamlit_folium import st_folium
from pyvis.network import Network
import tempfile
import os
import random

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="FraudShield OS",
    page_icon="🛡️",
    layout="wide"
)

# =========================
# UI STYLE
# =========================
st.markdown("""
<style>

body {
    background-color: #0a0a0a;
    color: white;
}

h1 {
    text-align: center;
    color: #ff1e1e;
    text-shadow: 0 0 10px #ff1e1e;
}

.metric-box {
    background: #0f0f0f;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #222;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

st.title("🛡️ FRAUDSHIELD OS — CYBER INTELLIGENCE CENTER")

# =========================
# FAKE LIVE METRICS (STATIC SIMULATION)
# =========================
total_incidents = random.randint(1500, 5000)
high_risk = random.randint(200, 800)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"<div class='metric-box'><h3>Total Incidents</h3><h2>{total_incidents}</h2></div>",
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"<div class='metric-box'><h3>High Risk Alerts</h3><h2>{high_risk}</h2></div>",
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        "<div class='metric-box'><h3>System Status</h3><h2>ACTIVE</h2></div>",
        unsafe_allow_html=True
    )

st.divider()

# =========================
# FRAUD HOTSPOTS MAP
# =========================
st.subheader("🌍 Fraud Hotspots Intelligence")

fraud_map = folium.Map(location=[22.5, 78.9], zoom_start=5)

hotspots = {
    "Delhi": [28.61, 77.20],
    "Mumbai": [19.07, 72.87],
    "Bangalore": [12.97, 77.59],
    "Hyderabad": [17.38, 78.48]
}

for city, coords in hotspots.items():
    folium.Marker(
        coords,
        popup=f"{city} - Fraud Activity Zone",
        icon=folium.Icon(color="red")
    ).add_to(fraud_map)

st_folium(fraud_map, width=1200, height=500)

st.divider()

# =========================
# FRAUD NETWORK GRAPH
# =========================
st.subheader("🕸️ Fraud Network Intelligence")

def generate_graph():

    net = Network(
        height="600px",
        width="100%",
        bgcolor="#0a0a0a",
        font_color="white",
        directed=True
    )

    nodes = [
        ("Scammer_A", "#ff1e1e"),
        ("Victim_A", "#00ff88"),
        ("Victim_B", "#00ff88"),
        ("Bank_X", "#ffcc00")
    ]

    for n, c in nodes:
        net.add_node(n, color=c, size=25)

    edges = [
        ("Scammer_A", "Victim_A"),
        ("Scammer_A", "Victim_B"),
        ("Victim_A", "Bank_X")
    ]

    for e in edges:
        net.add_edge(e[0], e[1])

    file_path = os.path.join(tempfile.gettempdir(), "fraud_graph.html")
    net.save_graph(file_path)

    return file_path


if st.button("Generate Network Graph"):
    file_path = generate_graph()

    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    st.components.v1.html(html, height=600)

st.divider()

# =========================
# LIVE STATUS FEED (STATIC)
# =========================
st.subheader("📡 Live Fraud Intelligence Feed")

alerts = [
    "Delhi: Digital Arrest Scam Activity Rising",
    "Mumbai: Fake Banking SMS Campaign Detected",
    "Bangalore: OTP Theft Attempts Increasing",
    "Hyderabad: Investment Fraud Cluster Active"
]

for a in alerts:
    st.warning(a)

st.success("🛡️ SYSTEM MONITORING ACTIVE — FRAUDSHIELD OS ONLINE")

st.markdown("""
## 🛡️ LIVE GLOBAL THREAT STATUS

🟡 OTP scams increasing in metro cities  
🔴 Digital arrest scams detected in circulation  
🟠 Phishing campaigns active in banking sector  

---
""")