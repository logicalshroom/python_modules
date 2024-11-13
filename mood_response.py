def mood_response(mood):
    if mood.lower() == "happy":
        print(f"I'm glad you're feeling {mood} today! Keep doing great!")
    elif mood.lower() == "sad":
        print(f"I'm sorry you're feeling {mood} today. I hope you feel less {mood} soon.")
    elif mood.lower() == "excited":
        print(f"I'm glad you're feeling {mood}! Stay energized!")
    else:
        print(f"I'm sorry, I didn't understand your response.")