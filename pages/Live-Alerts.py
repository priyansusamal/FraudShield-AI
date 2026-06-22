import streamlit as st

st.title("📡 Live Fraud Alerts")

alerts = [
    "Delhi: Digital Arrest Scam Active",
    "Mumbai: Fake Banking SMS Wave",
    "Bangalore: OTP Fraud Ring",
    "Hyderabad: Investment Scam Surge"
]

for a in alerts:
    st.warning(a)

st.success("System Monitoring Active 🛡️")