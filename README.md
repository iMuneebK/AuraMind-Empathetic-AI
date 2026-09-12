# Mental Health Support Chatbot 💙

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-orange)

A voice-enabled, AI-driven mental health support chatbot designed to provide a compassionate and responsive conversational experience. It leverages NLP for intent classification and real-time sentiment analysis to adapt its responses.

## ⚠️ Important Disclaimer
**This chatbot is NOT a substitute for professional mental health diagnosis, treatment, or therapy.** 
It is a project created for portfolio and educational purposes. If you or someone you know is in crisis, please contact emergency services or a crisis hotline immediately (e.g., dial 988 for the Suicide & Crisis Lifeline in the US).

## 🔒 Privacy & Ethics
- **Data Privacy**: All conversations and emotion logs (`emotion_log.json`) are stored strictly locally. No user data is sent to external servers or used for training.
- **Ethical AI**: Built with explicit crisis detection algorithms to immediately halt generic responses and provide emergency hotline information when severe distress is detected.

## Features
- **Real-time Sentiment Analysis**: Uses HuggingFace transformers (`distilbert-base`) to gauge emotional tone and adapt empathy levels.
- **Intent Classification**: Custom rule-based and keyword-driven classification to detect topics like anxiety, depression, grief, and stress.
- **Voice Interactions**: Integrated `SpeechRecognition` for voice input and `pyttsx3` for text-to-speech output.
- **Emotion Tracking**: Logs historical emotional sentiment to map mood trends across sessions.
- **Crisis Detection**: Flags high-risk keywords to instantly provide helpline resources.

## Installation & Usage
```bash
# Clone the repository
git clone https://github.com/yourusername/mental-health-chatbot.git
cd mental-health-chatbot

# Install dependencies (requires PyAudio for voice features)
pip install -r requirements.txt

# Run the Streamlit web interface
streamlit run app.py
```
