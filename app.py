import streamlit as st
from emotion_detection import detect_emotion
from comfort_tools import comfort_user
import random

st.set_page_config(page_title="MoodJournal AI 💬", page_icon="🎤")
st.title("🎤 MoodJournal AI")
st.subheader("💖 Speak, Reflect, and Heal")

# --- HTML + JavaScript for Browser-Based Microphone Input ---
st.markdown("""
    <script>
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = "en-US";

    function startDictation() {
        recognition.start();
        recognition.onresult = function(e) {
            document.getElementById('speechResult').value = e.results[0][0].transcript;
            recognition.stop();
        };
        recognition.onerror = function(e) {
            recognition.stop();
        }
    }
    </script>

    <input type="text" id="speechResult" name="speechResult" placeholder="Click below and speak" style="width: 300px; padding: 8px"/>
    <br><br>
    <button onclick="startDictation()" style="padding:10px;">🎙️ Start Voice Recording</button>
""", unsafe_allow_html=True)

# Capture the text from browser mic
spoken_text = st.text_input("Your spoken mood will appear here:")

if spoken_text:
    emotion = detect_emotion(spoken_text)
    st.success(f"Detected Emotion: **{emotion.upper()}**")
    st.info(comfort_user(emotion))

    if emotion in ["sad", "angry"]:
        st.markdown("### 🌸 Playing a soft Hindi song to comfort you:")

        # Randomly choose one of the three songs
        music_files = ["song1.mp3", "song.mp3", "mood.mp3"]
        selected_song = random.choice(music_files)

        try:
            audio_file = open(selected_song, "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
        except FileNotFoundError:
            st.error("❌ Music file not found. Please check file names.")

# --- Optional Journal Section ---
st.markdown("---")
if st.checkbox("📝 I want to write in my journal"):
    journal_text = st.text_area("Write your thoughts here...", height=200)
    if st.button("📂 Save Journal Entry"):
        with open("journal_entries.txt", "a", encoding="utf-8") as f:
            from datetime import datetime
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            f.write(f"\n\n---\nDate: {now}\nMood: {emotion.upper()}\nEntry:\n{journal_text}\n")
        st.success("✅ Journal entry saved!")



