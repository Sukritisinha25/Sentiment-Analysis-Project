# Sentiment Analysis Project (Rule-Based & ML-Based)

A Python-based Sentiment Analysis tool that analyzes user-input text and classifies it as Positive, Negative, or Neutral.  
The project demonstrates both rule-based NLP techniques and a machine learning–ready structure, making it suitable for beginners transitioning into applied NLP and AI.

## Features

- Rule-based sentiment analysis using predefined positive and negative word lists
- Score-based sentiment classification (Positive / Negative / Neutral)
- Handles mixed sentiments and emphasis (e.g., "really good")
- Command-line interface (CLI)
- Modular project structure (easy to extend to ML or deep learning)
- Beginner-friendly and interview-ready project

## Project Structure

sentiment-analysis-project/
│
├── app.py # Main application (entry point)
├── rule_based.py # Rule-based sentiment logic
├── ml_based.py # Placeholder for ML-based approach
├── pycache/ # Python cache files
└── README.md # Project documentation

## How It Works

1. The user enters a sentence.
2. The text is tokenized and analyzed.
3. Each word contributes to a sentiment score:
   - Positive words → +1
   - Negative words → -1
   - Intensifiers (e.g., "really") increase weight
4. Final sentiment is decided based on total score.

## How to Run the Project

### Prerequisites
- Python 3.8 or above
- VS Code / Terminal

### Steps

```bash
git clone https://github.com/<your-username>/sentiment-analysis-project.git
cd sentiment-analysis-project
python app.py
