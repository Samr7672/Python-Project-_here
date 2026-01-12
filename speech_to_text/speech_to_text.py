import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime


def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to your Voice.....")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("Recognizing your voice....")
            data=recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print("I Don't Understand...")
sptext()            