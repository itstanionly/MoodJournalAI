def detect_emotion(text):
    text = text.lower()

    # Manual detection of strong emotional phrases (more sensitive)
    sadness_keywords = [
        "i want to die", "i feel empty", "i'm hurt", "i feel weak", "i'm not okay",
        "i'm not happy", "i feel like giving up", "i feel useless", "no one cares",
        "i feel unloved", "i feel powerless", "hopeless", "alone", "abandoned",
        "depressed", "broken", "crying", "lost", "worthless", "powerless", "useless", "lonely", "hurt"
    ]
    anger_keywords = [
        "i'm angry", "i hate", "so frustrating", "annoyed", "furious", "mad",
        "irritated", "rage", "snapped", "pissed off"
    ]
    fear_keywords = [
        "i'm scared", "terrified", "afraid", "anxious", "panic", "nervous",
        "shaking", "worried", "dread", "uneasy"
    ]
    joy_keywords = [
        "i'm happy", "joy", "excited", "grateful", "blessed", "cheerful",
        "content", "amazing", "wonderful", "love"
    ]
    surprise_keywords = [
        "surprised", "shocked", "unexpected", "wow", "amazed", "unbelievable"
    ]
    neutral_keywords = [
        "okay", "fine", "normal", "nothing much", "usual", "same as always"
    ]

    for phrase in sadness_keywords:
        if phrase in text:
            return "sad"

    for phrase in anger_keywords:
        if phrase in text:
            return "angry"

    for phrase in fear_keywords:
        if phrase in text:
            return "fear"

    for phrase in joy_keywords:
        if phrase in text:
            return "happy"

    for phrase in surprise_keywords:
        if phrase in text:
            return "surprise"

    for phrase in neutral_keywords:
        if phrase in text:
            return "neutral"

    # Fallback
    return "neutral"
