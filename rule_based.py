import string


def analyze_sentiment_rule_based(text):
    # Word Banks
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
    negators = {"not", "never", "no", "hardly", "barely"}
    intensifiers = {"very", "extremely", "really", "so", "total", "incredibly"}

    # Cleaning
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.lower().split()
    score = 0

    for i in range(len(words)):
        word = words[i]

        # Check for intensifier from the previous word
        weight = 2 if (i > 0 and words[i - 1] in intensifiers) else 1

        if word in positive_words:
            # Check for negation
            if i > 0 and words[i - 1] in negators:
                score -= weight
            else:
                score += weight

        elif word in negative_words:
            # Check for negation
            if i > 0 and words[i - 1] in negators:
                score += weight
            else:
                score -= weight

    return score
