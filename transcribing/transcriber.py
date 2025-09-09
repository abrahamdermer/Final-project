import speech_recognition as sr








class Transcriber:

    def __init__(self):
        self.r = sr.Recognizer()

    
    def file_to_text(self,file,id):
        print(file)
        # audio = self.r.record(file)
        # with open(f"{id}.wav", "wb") as f:
        #     f.write(audio.get_wav_data())
        text = ''
        return text