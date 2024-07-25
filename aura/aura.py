#pip install pyaudio

import pyttsx3 #pip install pyttsx3 (voice type)
import datetime # timer
import speech_recognition as sr#pip install speechRecognition (input from mic)
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib #for sending mail


engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("I am AURA. Please tell me how can I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:  # Correctly instantiate sr.Microphone
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

'''def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mailid@gmail.com','password')
    server.sendmail('mailid@gmail.com',to,content)
    server.close()
'''


if __name__ =="__main__":
    speak("AURA here")
    wishMe()
    while True:
        query= takeCommand().lower()
        

        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:
            webbrowser.open("https://github.com/")  

        elif 'play music' in query:
            webbrowser.open("open.spotify.com")  

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir the time is {strTime}")

        elif 'open code' in query:
            codePath= 'C:\\Users\\poorv\\AppData\\Local\\Programs\\Microsoft VS Code'

        elif 'turn off' in query:
            break

        elif 'quit' in query:
            exit

        else:
            print("No query matched")

        '''elif 'email to garima' in query:
            try:
                speak("What should I say??")
                content= takeCommand()
                to= "garimajaiswal157@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("due to some reason email can't send please try again later")
        '''
        

          
