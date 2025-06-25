import pyjokes
import webbrowser

# Suggestion based on emotion
def comfort_user(emotion):
    responses = {
        "happy": "Yay! Stay joyful and spread the good vibes! 💫",
        "sad": "I'm here for you🫂. Want to write about it in your journal or listen to some music?",
        "angry": "Take a deep breath. Music or writing might help you calm down🌷🎧.",
        "fear": "You're safe now. Maybe a relaxing song will help🌸🦋🌼.",
        "surprise": "Whoa! That was unexpected 😯 Tell me more!",
        "neutral": "Feeling neutral is okay too. Try writing something to reflect🩷."
    }
    return responses.get(emotion.lower(), "Hmm... I'm not sure how to respond, but I'm here for you! 💗")

def play_music():
    webbrowser.open("song1.mp3")  # This will open the file in your default music player

def tell_joke():
    return pyjokes.get_joke()

