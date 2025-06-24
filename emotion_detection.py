def detect_emotion(text):
    text = text.lower()

    if any(word in text for word in ["sad", "tired", "cry", "depressed", "lonely", "alone", "upset"]):
        return "sad"
    elif any(word in text for word in ["angry", "irritated", "mad", "annoyed", "frustrated"]):
        return "angry"
    elif any(word in text for word in ["happy", "excited", "great", "awesome", "joyful", "grateful"]):
        return "happy"
    else:
        return "neutral"
