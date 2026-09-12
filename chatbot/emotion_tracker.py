import json
import os
from datetime import datetime

class EmotionTracker:
    def __init__(self, log_file="emotion_log.json"):
        self.log_file = log_file
        self.history = self._load_history()

    def _load_history(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, "r") as f:
                return json.load(f)
        return []

    def log_emotion(self, sentiment_label, score):
        self.history.append({
            "timestamp": datetime.now().isoformat(),
            "emotion": sentiment_label,
            "intensity": score
        })
        self._save_history()

    def _save_history(self):
        with open(self.log_file, "w") as f:
            json.dump(self.history, f, indent=4)
