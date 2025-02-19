import pyttsx3
import tkinter
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good Evening!")
    speak("My name is jonny how may i help you")

def takeCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Could not understand audio, please speak again.")
        return "None"
    
    return query

if __name__=="__main__":
    speak("Hello")
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open Youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open Instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open Google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music='G:\\music'
            songs=os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music, songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif 'open vs code' in query:
            path="C:\\Users\\laves\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
