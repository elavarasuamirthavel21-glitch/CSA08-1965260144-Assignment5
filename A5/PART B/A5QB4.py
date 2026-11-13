import sqlite3

POSITIVE = {"good", "clean", "fast", "helpful", "improved"}
NEGATIVE = {"bad", "dirty", "slow", "rude", "smoke", "broken"}
NEGATORS = {"not", "never", "no"}


def score(text):
    words = text.lower().replace(".", " ").replace(",", " ").split()
    total = 0

    for i, word in enumerate(words):
        value = 1 if word in POSITIVE else -1 if word in NEGATIVE else 0

        if i > 0 and words[i-1] in NEGATORS:
            value = -value

        total += value

    return total


def label(text):
    s = score(text)

    if s > 0:
        return "positive"
    elif s < 0:
        return "negative"
    return "neutral"


def summarise(text):
    sentences = text.split(".")
    words = text.lower().split()

    important = POSITIVE | NEGATIVE
    frequency = {}

    for word in words:
        if word in important:
            frequency[word] = frequency.get(word, 0) + 1

    if not frequency:
        return sentences[0]

    best = max(
        sentences,
        key=lambda s: sum(
            frequency.get(w, 0) for w in s.lower().split()
        )
    )

    return best.strip()


complaint = "Roads are clean. Smoke is bad. The service is helpful."

print("Sentiment:", label(complaint))
print("Summary:", summarise(complaint))


# Database Indexing
con = sqlite3.connect(":memory:")

con.execute("""
CREATE TABLE readings (
    station TEXT,
    day TEXT,
    pm25 REAL
)
""")

con.execute(
    "CREATE INDEX idx_station_day ON readings(station, day)"
)

print("Database index created successfully")

con.close()
