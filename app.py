import streamlit as st
from emotion_detection import detect_emotion
from comfort_tools import comfort_user, tell_joke
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

    if emotion in ["happy", "excited", "neutral"]:
        if st.button("🤣 Tell me a joke!"):
            st.success(tell_joke())

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
        # --- MoodBot Chat Section ---
st.markdown("---")
st.subheader("💬 Talk to MoodBot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_msg = st.text_input("Type your thoughts here:")

def mood_bot_response(msg):
    msg = msg.lower()
    if any(word in msg for word in ["sad", "hurt", "down"]):
        return "I'm really sorry you're feeling this way. Remember, you're not alone 🌈"
    elif any(word in msg for word in ["angry", "mad"]):
        return "It's okay to feel angry sometimes. Let's calm down together. Want to try music or journaling?"
    elif any(word in msg for word in ["happy", "joy", "good"]):
        return "Yay! I'm so glad you're happy 😄 Keep spreading those vibes!"
    elif "joke" in msg:
        return tell_joke()
    elif "love" in msg:
        return "Love can be beautiful and tough at the same time 💕 I'm here to listen."
    elif any(word in msg for word in ["music", "song"]):
        play_music()
        return "🎵 Playing music for you..."
    elif any(word in msg for word in ["weird", "crazy"]):
        st.markdown("""
            <script>
            let flash = true;
            setInterval(() => {
                document.body.style.backgroundColor = flash ? "#ffe4e1" : "#ffffff";
                flash = !flash;
            }, 300);
            </script>
        """, unsafe_allow_html=True)
        return "Uh oh... going into CHAOTIC MODE! 🔴🟣🟡"
    else:
        return "Hmm, tell me more... I'm here for you 💖"

if user_msg:
    bot_reply = mood_bot_response(user_msg)
    st.session_state.chat_history.append(("You", user_msg))
    st.session_state.chat_history.append(("MoodBot", bot_reply))

# Show the conversation
for speaker, msg in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {msg}")




