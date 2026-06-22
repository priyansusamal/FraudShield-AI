import streamlit as st
import speech_recognition as sr

st.title("🎙️ Voice Scam Detection")

st.markdown("Upload or record a suspicious call for analysis")

audio_file = st.file_uploader("Upload Audio File", type=["wav", "mp3"])

def transcribe(audio_path):

    r = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio)
        return text
    except:
        return "Could not transcribe audio"

def simple_scam_check(text):

    text = text.lower()
    score = 10

    if "cbi" in text or "police" in text:
        score += 40

    if "urgent" in text or "immediately" in text:
        score += 25

    if "otp" in text or "bank" in text:
        score += 25

    return min(score, 100)

if audio_file:

    st.audio(audio_file)

    with open("temp_audio.wav", "wb") as f:
        f.write(audio_file.read())

    text = transcribe("temp_audio.wav")

    st.subheader("📝 Transcribed Text")
    st.write(text)

    score = simple_scam_check(text)

    st.subheader("🧠 Risk Score")

    st.progress(score / 100)

    if score > 70:
        st.error("HIGH RISK VOICE SCAM 🔴")
    elif score > 40:
        st.warning("SUSPICIOUS CALL 🟡")
    else:
        st.success("LIKELY SAFE 🟢")