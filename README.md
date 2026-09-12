# 🧠 AuraMind — Voice-Enabled Conversational AI for Mental Health Support

[![Python 3.10](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg)](https://huggingface.co/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-red.svg)](https://streamlit.io/)

> **Developer Notes**: Built to explore adaptive tone synthesis, real-time emotion classification, and safety crisis protocols in conversational agents.

---

## 📌 Architecture & Design

AuraMind is an empathetic voice-enabled AI companion. It tracks session emotional valence, adapts empathy levels dynamically, and surfaces crisis safety helplines whenever risk keywords are detected.

```mermaid
graph TD
    User[Voice / Text Input] --> STT[Speech-to-Text Parser]
    STT --> Safety[Crisis Safety Keyword Filter]
    Safety -- Risk Detected --> Crisis[Surfaces Helpline 988 Info]
    Safety -- Safe --> Emotion[HuggingFace Sentiment Analyzer]
    Emotion --> Intent[NLP Intent Classifier]
    Intent --> Generator[Adaptive Empathy Response Generator]
    Generator --> Tracker[Mood Analytics Engine]
    Generator --> TTS[Text-to-Speech Output]
```

## 🛡️ Safety & Ethical Guidelines
This project is an academic AI research prototype designed for conversational support. It includes hardcoded crisis safety filters and emergency helpline notifications.
