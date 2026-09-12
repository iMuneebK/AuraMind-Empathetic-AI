import pyttsx3

class SpeechOutput:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
