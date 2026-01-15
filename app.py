from rule_based import analyze_sentiment_rule_based


def main():
    print("\n--- Sentiment Analysis Tool ---")
    user_input = input("Please enter a sentence to analyze: ")

    # Call the function from rule_based.py
    score = analyze_sentiment_rule_based(user_input)

    # Determine the emoji and label based on score
    if score > 0:
        result = f"Positive 😊 (Score: {score})"
    elif score < 0:
        result = f"Negative ☹️ (Score: {score})"
    else:
        result = f"Neutral 😐 (Score: {score})"

    print(f"\nAnalysis Result: {result}\n")


if __name__ == "__main__":
    main()
