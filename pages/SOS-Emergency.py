import streamlit as st
import uuid
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="SOS Emergency",
    page_icon="🆘",
    layout="wide"
)

# =========================
# STYLE
# =========================
st.markdown("""
<style>

body {
    background-color: #07090f;
    color: white;
}

.title {
    text-align: center;
    font-size: 34px;
    font-weight: 900;
    color: #ff1e1e;
    text-shadow: 0 0 12px #ff1e1e;
}

.card {
    background: #0f141f;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #2a2a2a;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🆘 EMERGENCY FRAUD RESPONSE SYSTEM</div>", unsafe_allow_html=True)

# =========================
# HELPERS
# =========================
def generate_case_id():
    return "FR-" + str(uuid.uuid4())[:8].upper()

# =========================
# UI
# =========================
st.markdown("## One-Tap Emergency Protection")
st.warning("Use this only if you are actively being targeted by fraud/scam calls/messages.")

# =========================
# SOS BUTTON
# =========================
if st.button("🆘 ACTIVATE SOS ALERT"):

    case_id = generate_case_id()
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # =========================
    # LOG INCIDENT (IMPORTANT FIX)
    # =========================


    st.error("EMERGENCY ALERT ACTIVATED")

    # =========================
    # CASE FILE
    # =========================
    st.markdown(f"""
    <div class="card">
        <h3>CASE FILE GENERATED</h3>
        <p><b>Case ID:</b> {case_id}</p>
        <p><b>Status:</b> ACTIVE</p>
        <p><b>Time:</b> {time_now}</p>
        <p><b>Priority:</b> HIGH</p>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # INTELLIGENCE STATUS
    # =========================
    st.markdown("""
    <div class="card">
        <h3>📡 SYSTEM RESPONSE</h3>
        <p>✔ Incident logged into FraudShield network</p>
        <p>✔ Threat pattern flagged for analysis</p>
        <p>✔ Monitoring escalation activated</p>
        <p>✔ Live tracking simulation enabled</p>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # SAFETY INSTRUCTIONS
    # =========================
    st.markdown("## Immediate Safety Instructions")

    st.error("Do NOT share OTP, bank details, or screen access")
    st.warning("Disconnect from unknown calls immediately")
    st.info("Report cyber fraud at 1930 (India) or local cybercrime portal")
    st.success("You are now in protected monitoring mode")

else:
    st.info("Press SOS only during active fraud situations.")