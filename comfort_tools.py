import pyjokes
import webbrowser

# Suggestion based on emotion

def comfort_user(emotion):
    responses = {
        "happy": "Yay! Stay joyful and spread the good vibes! 💫 Keep doing what makes you feel alive! You’re shining today — keep that spark glowing! 🌟",
        "sad": "I'm here for you🫂. It's okay to feel down sometimes. Maybe writing it out or listening to music will help. 💖 Remember, storms don’t last forever — brighter days are coming. 🌈",
        "angry": "Take a deep breath. Let’s turn that fire into something creative. Writing or soft music can help cool things down. 🌷🎧 Try to focus on what you can control, and let the rest go. 🕊️",
        "fear": "You are stronger than you feel. You've survived 100% of your bad days so far. Take a deep breath — you're not alone 🌸🦋🌼 Facing fear is the first step to courage — and you’re already doing it! 💪",
        "surprise": "Whoa! That was unexpected 😯 Wanna tell me what happened? I’m all ears! Sometimes surprises bring growth — maybe this one’s a hidden blessing! ✨",
        "neutral": "Feeling neutral is totally valid. Maybe journaling can give you some clarity. 🩷 What’s on your mind today? Small steps lead to big changes — even stillness is part of progress. 🍃"
    }
    return responses.get(emotion.lower(), "Hmm... I'm not sure how to respond, but I'm here for you! 💗")

def play_music():
    webbrowser.open("song1.mp3")  # This will open the file in your default music player

def tell_joke():
    return pyjokes.get_joke()


