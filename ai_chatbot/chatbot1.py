import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

# Function to convert Speech to Text
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust for background noise
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Not Understanding")
            return ""

# Function to convert Text to Speech
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # voices[0].id is male, voices[1].is female
    engine.setProperty('voice', voices[1].id) 
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150) # Adjust speaking speed
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    # Initial activation command
    if "hey peter" in sptext().lower():
        while True:
            data1 = sptext().lower()

            if "your name" in data1:
                name = "my name is samr"
                speechtx(name)

            elif "old are you" in data1:
                age = "i am twenty years old"
                speechtx(age)

            elif 'now time' in data1:
                # Fetches current system time
                time_now = datetime.datetime.now().strftime("%I:%M %p")
                speechtx(time_now)

            elif "open youtube" in data1:
                webbrowser.open("https://www.youtube.com/")

            elif "webpage" in data1:
                webbrowser.open("https://www.github.com/")

            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                speechtx(joke_1)

            elif "play song" in data1:
                # Path to your local music folder
                path = r"C:\Users\rebik\Music"
                listsong = os.listdir(path)
                os.startfile(os.path.join(path, listsong[0]))

            elif "exit" in data1:
                speechtx("thank you")
                break

            time.sleep(5) # Pause before next command
    else:
        print("Assistant not activated.")