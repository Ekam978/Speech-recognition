from tkinter import *
import speech_recognition as sr
import pyttsx3
from datetime import datetime

root= Tk()
root.geometry("500x500")

texttospeech = pyttsx3.init()
def speak(audio):
    texttospeech.say(audio)
    texttospeech.runAndWait()

def r_audio():
    speak("Hi! How can I help you..?")
    speech_recognisor = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        voice_data = ''
        try:
            voice_data = speech_recognisor.recognize_google(audio,language='en-in')
        except sr.UnknownValueError:
            print('I did not understand that. Please repeat once ogain.')
            speak("I did not understand that. Please repeat once ogain.")
    print(voice_data)
    respond(voice_data)

def respond(voice_data):
    voice_data = voice_data.lower()
    if "name" in voice_data:
        speak("My name is Javis")
        print("My name is Javis")
    if "time" in voice_data:
        speak("Current time is ")
        now = datetime.now()
        current_time = naow.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
r_audio()
root.mainloop()