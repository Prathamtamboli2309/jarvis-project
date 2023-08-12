from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia as googles #pip install wikipedia
import webbrowser
import os
import pyaudio
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("hello what can do for you.")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        speak("Say that again please...")
        return "None"
    return query

   

if __name__ == "__main__":
    wishMe()
    cmd=True
    while cmd:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = googles.wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play song' in query:
            music_dir = 'D:\\python\\song'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'open  coder' in query:
            turboc='C:\\Users\\Public\\Desktop\\code.exe'    
            os.startfile(turboc)  

        elif 'close  coder' in query:
            os.system("taskkill /f /im code.exe") 

        elif 'open notepad' in query:
             
            speak("tell me what to write....")
            writes = takeCommand()
  
  
            filename="my.text"
    
            with open(filename,'w') as file:
                file.write(writes)
   
            path_1="F:\\jarvis\\"+filename
            path_2="F:\\notepad-files\\"+filename
    
            os.rename(path_1,path_2)

            os.startfile(path_2)   

        elif 'open vs code' in query:
            vscode = 'C:\\Users\\pratham\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'      
            os.startfile(vscode)

        elif 'close vs code' in query:
            os.system("taskkill /f /im code.exe")    

        elif 'open vlc' in query:
            vlc = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"    
            os.startfile(vlc)

        elif 'close vlc' in query:
            os.system("taskkill /f /im vlc.exe")

        elif 'close jarvis' in query:
            cmd=False
        