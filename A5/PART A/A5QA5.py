POSITIVE = ["good", "clean", "helpful", "improved"]
NEGATIVE = ["bad", "dirty", "slow", "smoke"]

def sentiment(text):
    words = text.lower().split()
    score = 0

    for i, word in enumerate(words):
        value = 1 if word in POSITIVE else -1 if word in NEGATIVE else 0

        if i > 0 and words[i-1] in ["not", "never", "no"]:
            value = -value

        score += value

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    return "Neutral"


def chatbot(question):
    if "pm2.5" in question.lower():
        return "PM2.5 data is available in the database."
    else:
        return "Sorry, I cannot understand."


text = "The road is clean but smoke is bad"

print("Sentiment:", sentiment(text))
print("Chatbot:", chatbot("What is the PM2.5 level?"))
