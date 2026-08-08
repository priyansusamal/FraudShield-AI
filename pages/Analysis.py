import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="FraudShield AI - Analyzer",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Scam Analyzer")


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
# USER INPUT
# =========================

msg = st.text_area(
    "Paste suspicious message",
    height=180
)


# =========================
# ANALYZE
# =========================

if st.button("Analyze"):

    if not msg.strip():

        st.warning("Please enter a message")

    else:

        score, reasons, scam_type = detect(msg)

        # =========================
        # RISK RESULT
        # =========================

        if score < 40:

            st.success(f"🟢 LOW RISK ({score})")

        elif score < 70:

            st.warning(f"🟡 MEDIUM RISK ({score})")

        else:

            st.error(f"🔴 HIGH RISK ({score})")


        # =========================
        # SCAM TYPE
        # =========================

        st.subheader(f"🧠 Scam Type: {scam_type}")


        # =========================
        # DETECTED REASONS
        # =========================

        st.subheader("📋 Detected Reasons")

        if reasons:

            for reason in reasons:
                st.write("•", reason)

        else:

            st.write("No suspicious patterns detected.")