import speech_recognition as sr


filename = "wie_fuehlen_sie_sich_heute.wav"

speech_engine = sr.Recognizer()


with sr.AudioFile(filename) as f:
    data = speech_engine.record(f)
    text = speech_engine.recognize_google(data, language="de-DE")
    print(text)

