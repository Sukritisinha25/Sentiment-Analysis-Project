import string


def analyze_sentiment_rule_based(text):
    positive_words = {
        "good",
        "great",
        "happy",
        "excellent",
        "amazing",
        "love",
        "best",
        "wonderful",
    }
    negative_words = {
        "bad",
        "sad",
        "terrible",
        "horrible",
        "awful",
        "hate",
        "worst",
        "poor",
    }
    negators = {"not", "never", "no", "hardly"}
    intensifiers = {"very", "extremely", "really", "so"}

    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.lower().split()
    score = 0

    for i in range(len(words)):
        word = words[i]
        weight = 2 if (i > 0 and words[i - 1] in intensifiers) else 1

        if word in positive_words:
            score += -weight if (i > 0 and words[i - 1] in negators) else weight
        elif word in negative_words:
            score += weight if (i > 0 and words[i - 1] in negators) else -weight

    return score
