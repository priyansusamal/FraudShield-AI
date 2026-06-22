import streamlit as st
import random
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Analytics", layout="wide")

st.title("📊 Fraud Intelligence Analytics")

# =========================
# FAKE ANALYTICS DATA (SELF-CONTAINED)
# =========================
def generate_fake_data():
    sources = ["Analyzer AI", "Bank Monitor", "Cyber Unit", "OSINT Bot"]
    messages = [
        "OTP scam pattern detected",
        "Suspicious banking transaction flagged",
        "Digital arrest scam activity reported",
        "Phishing link spreading via SMS",
        "Fake KYC verification scam detected"
    ]

    return {
        "source": random.choice(sources),
        "message": random.choice(messages),
        "risk": random.randint(10, 100),
        "time": datetime.now().strftime("%H:%M:%S")
    }

# =========================
# SESSION STORAGE
# =========================
if "analytics_data" not in st.session_state:
    st.session_state.analytics_data = [
        generate_fake_data() for _ in range(8)
    ]

# =========================
# ADD NEW DATA BUTTON
# =========================
if st.button("🔄 Generate New Data"):
    st.session_state.analytics_data.append(generate_fake_data())

data = st.session_state.analytics_data

# =========================
# SAFE RISK HANDLER
# =========================
def safe_risk(value):
    try:
        return int(value)
    except:
        return 0

# =========================
# METRICS
# =========================
total = len(data)
high = len([d for d in data if safe_risk(d.get("risk", 0)) > 70])

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Incidents", total)

with col2:
    st.metric("High Risk Cases", high)

st.divider()

# =========================
# RECENT ACTIVITY
# =========================
st.subheader("📡 Recent Activity")

for d in reversed(data[-10:]):

    source = d.get("source", "Unknown")
    message = d.get("message", "No message")
    risk = safe_risk(d.get("risk", 0))
    time = d.get("time", "N/A")

    if risk > 70:
        st.error(f"🔴 {source} → Risk {risk} | {time}")
    elif risk > 40:
        st.warning(f"🟡 {source} → Risk {risk} | {time}")
    else:
        st.success(f"🟢 {source} → Risk {risk} | {time}")

    st.write(message)
    st.divider()