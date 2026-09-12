import os

APP_NAME = "Mental Health Support Chatbot"
VOICE_RATE = 150
VOICE_VOLUME = 0.9

CRISIS_KEYWORDS = ["suicide", "kill myself", "want to die", "end it all"]
CRISIS_MESSAGE = "I am so sorry you're feeling this way. Please know that you are not alone and help is available. Please reach out to the National Suicide Prevention Lifeline at 988 or text HOME to 741741."

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
