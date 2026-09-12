import json
import os
from utils.config import DATA_DIR

class IntentClassifier:
    def __init__(self):
        self.intents_path = os.path.join(DATA_DIR, "intents.json")
        self.intents = self._load_intents()

    def _load_intents(self):
        if os.path.exists(self.intents_path):
            with open(self.intents_path, 'r') as f:
                return json.load(f)
        return {}

    def classify(self, text):
        text = text.lower()
        for intent, keywords in self.intents.items():
            if any(keyword in text for keyword in keywords):
                return intent
        return "general"
