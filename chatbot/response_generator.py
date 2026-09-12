import json
import os
import random
from utils.config import DATA_DIR, CRISIS_KEYWORDS, CRISIS_MESSAGE

class ResponseGenerator:
    def __init__(self):
        self.responses_path = os.path.join(DATA_DIR, "responses.json")
        self.responses = self._load_responses()

    def _load_responses(self):
        if os.path.exists(self.responses_path):
            with open(self.responses_path, 'r') as f:
                return json.load(f)
        return {"general": ["I'm here for you.", "Tell me more about how you're feeling."]}

    def generate(self, text, intent, sentiment_label):
        # Check crisis
        if any(kw in text.lower() for kw in CRISIS_KEYWORDS):
            return CRISIS_MESSAGE
        
        # Select response based on intent
        options = self.responses.get(intent, self.responses.get("general"))
        
        # Basic empathy adjustment
        response = random.choice(options)
        if sentiment_label == "NEGATIVE":
            response = "I hear you. " + response
            
        return response
