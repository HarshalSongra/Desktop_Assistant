import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import json
import requests
from send_mail import sendmail


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)  
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir ")
    

    speak(" I am Your Personal Assistent, How can i help you ? ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing.....")
            command = r.recognize_google(audio)
            print(f"you said:{command}\n")
    

        except Exception as e:
            print("Say that again...")
            return "None"

        return command.lower()


    
if __name__ == "__main__":
    greetMe() 
    while True:
        command = takeCommand()

        if 'wikipedia' in command:
            speak("Searching for Wikipedia sir, Please Wait.....!")
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            print(results)
            speak("Sir, According to Wikipedia" + results)
        
        elif 'open youtube' in command:
            speak("Opening Sir... ")
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            speak("Opening Sir... ")
            webbrowser.open("google.com")

        elif 'play music' in command:
            music_dir = 'H:\\Multimedia\\songs'
            songs = os.listdir(music_dir)
            randomsong = random.randint(1, 496)
            speak("Playing Sir... ")
            os.startfile(os.path.join(music_dir, songs[randomsong]))
        
        elif 'time' in command:
            curTime = datetime.datetime.now().strftime(" %H : %M : %S ")
            speak(f"Sir, The Current Time is {curTime}")

        elif 'goodbye' in command:
            hour = int(datetime.datetime.now().hour)
            if hour > 20:
                speak("Bye Sir, Good Night...")
            else:
                speak("Good Bye Sir, Have a Good Day...")
                
            exit()
        
        elif 'hey dear ' in command:
            speak("Hello Sir")
        
        elif 'blank_space' in command:
            speak("Yess sir?")
        
        elif 'who are you' in command:
            speak("I am your assistent Sir...")

        elif 'thanks dear' in command:
            speak("welcome Sir, It's my Work")

            
    # NEWS API Key:- 01922e11ddb44bd2b9bf29caa50abc32
        elif 'news' in command:
            r = requests.get('http://newsapi.org/v2/top-headlines?country=in&apiKey=01922e11ddb44bd2b9bf29caa50abc32')
            data = json.loads(r.content)
            for i in range(3):
                print(data['articles'][i]['title'])
                print(data['articles'][i]['url'])
                speak(data['articles'][i]['description'])
                
            speak("sir, All the links are given you can checkout your own ")

        elif "github" in command:
            speak("Opening Github Sir...")
            webbrowser.open("https://github.com/HarshalSongra")


        elif 'send mail' in command:
            try:
                print("Email Sender: ")
                speak("Enter the Email id's sir:")
                email_id = input("Email id's: ")

                speak("What can i say sir? ")
                msg = input("Messege: ")

                speak("wait for a minuit sir..")
                sendmail(to_emails=email_id, text=msg)
            except Exception as e:
                print(e)
                speak("Sorry Sir there is a problem, i can't send email\n")

        else:
            speak("Sorry sir, i can't getting what you want to say, can you please repeat\n")
