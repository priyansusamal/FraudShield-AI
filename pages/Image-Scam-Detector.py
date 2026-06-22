import streamlit as st
from PIL import Image
import pytesseract

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Image Scam Detector", layout="wide")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# =========================
# UI
# =========================
st.title("🖼️ AI Image Scam Detector")
st.markdown("Upload screenshots of WhatsApp / SMS / Emails to detect fraud")

# =========================
# SCAM ENGINE
# =========================
def detect_scam(text):

    text = text.lower()

    score = 10
    reasons = []

    if any(w in text for w in ["cbi", "police", "arrest", "investigation", "ed"]):
        score += 40
        reasons.append("Government impersonation detected")

    if any(w in text for w in ["urgent", "immediately", "final warning", "within 1 hour"]):
        score += 25
        reasons.append("Urgency pressure tactics")

    if any(w in text for w in ["otp", "bank", "account", "transfer", "upi"]):
        score += 25
        reasons.append("Financial manipulation attempt")

    if "http" in text or "click" in text:
        score += 20
        reasons.append("Suspicious link detected")

    return min(score, 100), reasons

# =========================
# FILE UPLOAD
# =========================
uploaded_file = st.file_uploader("Upload Screenshot", type=["png", "jpg", "jpeg"])

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    # OCR
    text = pytesseract.image_to_string(image)

    st.subheader("📝 Extracted Text")
    st.write(text)

    # Analysis
    score, reasons = detect_scam(text)

    st.subheader("🧠 Scam Analysis Result")

    st.progress(score / 100)

    if score < 40:
        st.success(f"🟢 LOW RISK ({score}/100)")
    elif score < 70:
        st.warning(f"🟡 MEDIUM RISK ({score}/100)")
    else:
        st.error(f"🔴 HIGH RISK ({score}/100)")

    st.subheader("⚠️ Reasons")

    if reasons:
        for r in reasons:
            st.write("•", r)
    else:
        st.info("No strong scam patterns detected")