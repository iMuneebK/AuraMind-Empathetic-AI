import streamlit as st
from chatbot.intent_classifier import IntentClassifier
from chatbot.sentiment_analyzer import SentimentAnalyzer
from chatbot.response_generator import ResponseGenerator
from chatbot.emotion_tracker import EmotionTracker
from voice.speech_output import SpeechOutput
import os

st.set_page_config(page_title="Mental Health Companion", layout="wide")

st.title("🌱 Mental Health Support Chatbot")
st.markdown("A compassionate companion to listen and support you. Please remember, this AI is not a substitute for professional help.")

if 'history' not in st.session_state:
    st.session_state['history'] = []

# Initialize modules
@st.cache_resource
def load_models():
    return IntentClassifier(), SentimentAnalyzer(), ResponseGenerator(), EmotionTracker()

classifier, analyzer, generator, tracker = load_models()
speech = SpeechOutput()

st.sidebar.title("Settings")
voice_enabled = st.sidebar.checkbox("Enable Voice Response")

user_input = st.text_input("How are you feeling today?")

if st.button("Send") and user_input:
    # Processing
    intent = classifier.classify(user_input)
    sentiment, score = analyzer.analyze(user_input)
    response = generator.generate(user_input, intent, sentiment)
    
    # Log emotion
    tracker.log_emotion(sentiment, score)
    
    st.session_state['history'].append({"user": user_input, "bot": response})
    
    if voice_enabled:
        speech.speak(response)

# Display chat history
for msg in reversed(st.session_state['history']):
    st.chat_message("user").write(msg["user"])
    st.chat_message("assistant").write(msg["bot"])

st.sidebar.markdown("---")
st.sidebar.warning("Crisis Support: If you are in immediate danger, please call 988 or 911.")
