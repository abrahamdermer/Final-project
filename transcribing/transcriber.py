import speech_recognition as sr








class Transcriber:

    def __init__(self):
        self.r = sr.Recognizer()

    @staticmethod
    def file_to_text(file):
        text = ''
        return text