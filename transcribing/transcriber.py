import speech_recognition as sr








class Transcriber:

    def __init__(self):
        self.r = sr.Recognizer()

    
    def file_to_text(self,file,id):
        with open('downloaded_audio.wav', 'wb') as f:
            f.write(file)
        with sr.AudioFile("downloaded_audio.wav") as source:
            audio = self.r.record(source)
        text = self.r.recognize_google(audio)
        return text