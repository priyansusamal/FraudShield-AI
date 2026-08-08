import streamlit as st
import os
from google import genai

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="FraudShield AI - Analyzer",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Scam Analyzer + AI Intelligence")

# =========================
# GEMINI CLIENT
# =========================
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=API_KEY)
except Exception:
    API_KEY = None
    client = None

if not client:
    st.warning("⚠️ Gemini API key not found. AI disabled.")

# =========================
# RULE-BASED DETECTION
# =========================
def detect(text):
    text = text.lower()
    score = 10
    reasons = []
    scam_type = "Unknown"

    if any(w in text for w in ["cbi", "ed", "police", "arrest", "investigation"]):
        score += 40
        reasons.append("Government impersonation detected")
        scam_type = "Digital Arrest Scam"

    if any(w in text for w in ["otp", "bank", "account", "transfer"]):
        score += 25
        reasons.append("Financial information risk")
        scam_type = "Banking / OTP Fraud"

    if any(w in text for w in ["urgent", "immediately", "final warning"]):
        score += 20
        reasons.append("Urgency pressure tactic")

    if "http" in text or "click" in text:
        score += 20
        reasons.append("Suspicious link detected")
        scam_type = "Phishing Attack"

    return min(score, 100), reasons, scam_type

# =========================
# AI EXPLANATION
# =========================
def get_ai_explanation(text):

    if not client:
        return "⚠️ AI unavailable (missing API key)."

    try:
        prompt = f"""
You are a cybercrime analyst.

Analyze this message:

{text}

Return:
1. Risk summary
2. Why it is suspicious
3. Scam techniques used
4. Safety advice
"""

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"⚠️ AI error: {str(e)}"

# =========================
# UI
# =========================
msg = st.text_area("Paste suspicious message", height=180)

if st.button("Analyze"):

    if not msg.strip():
        st.warning("Please enter a message")

    else:
        score, reasons, scam_type = detect(msg)

        # =========================
        # RESULT UI
        # =========================
        if score < 40:
            st.success(f"🟢 LOW RISK ({score})")
        elif score < 70:
            st.warning(f"🟡 MEDIUM RISK ({score})")
        else:
            st.error(f"🔴 HIGH RISK ({score})")

        st.subheader(f"🧠 Scam Type: {scam_type}")

        st.subheader("📋 Detected Reasons")
        for r in reasons:
            st.write("•", r)

        # =========================
        # AI SECTION
        # =========================
        st.subheader("🤖 AI Investigation Report (Gemini)")

        with st.spinner("Analyzing with AI..."):
            explanation = get_ai_explanation(msg)

        st.markdown(explanation)