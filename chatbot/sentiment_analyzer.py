from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        # We use a tiny pipeline for fast inference
        self.analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    def analyze(self, text):
        result = self.analyzer(text)[0]
        return result['label'], result['score']
