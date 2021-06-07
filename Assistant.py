import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import json
import requests
from send_mail import sendmail
import time
import subprocess
from weatherModule import WeatherService


MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october", "november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)  
    engine.runAndWait()


def greetMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir ")


def run():
    greetMe()
    speak("Glad to see you back,")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening.....")
        r.pause_threshold = 0.7
        audio = r.listen(source)
        print("Listening over")

        try:
            print("Recognizing.....")
            command = r.recognize_google(audio, language="en-IN")
            print(f"you said: {command}\n")
    

        except Exception as e:
            print("Didn't get it, Say that again...")
            return "none"

        return command.lower()

def get_date(date):
    date = date.lower()
    today = datetime.date.today()

    if date.count('today') > 0:
        return today

    day = -1
    day_of_week = -1
    month = -1
    year = today.year


if __name__ == "__main__":
    run()
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
            music_dir = 'G:\\Multimedia\\songs'
            songs = os.listdir(music_dir)
            randomsong = random.randint(1, 496)
            speak("Playing Sir... ")
            os.startfile(os.path.join(music_dir, songs[randomsong]))

        elif 'time' in command:
            curTime = datetime.datetime.now().strftime(" %H : %M : %S ")
            speak(f"Sir, The Current Time is {curTime}")
            # time.sleep(20)

        elif 'date' in command:
            get_date()

        elif 'goodbye' in command:
            hour = int(datetime.datetime.now().hour)
            if hour > 20:
                speak("Bye Sir, Good Night...")
            else:
                speak("Good Bye Sir, Have a Good Day...")

            exit()

        # NEWS API Key:- 01922e11ddb44bd2b9bf29caa50abc32
        elif 'news' in command:
            r = requests.get('http://newsapi.org/v2/top-headlines?country=in&apiKey={API key}')
            data = json.loads(r.content)
            for i in range(3):
                print(data['articles'][i]['title'])
                print(data['articles'][i]['url'])
                speak(data['articles'][i]['description'])

            speak("sir, All the links are given you can checkout your own ")

        elif "github" in command:
            speak("Opening your Github profile Sir...")
            webbrowser.open("https://github.com/HarshalSongra")

        elif 'send mail' in command:
            try:
                print("Email Sender: ")
                speak("Enter the Email id's sir:")
                email_id = input("Email id's: ")

                speak("What can i say sir? ")
                msg = input("Messege: ")

                speak("wait for a minute sir..")
                sendmail(to_emails=email_id, text=msg)

                speak(f"The email to <{email_id}> with message: {msg} has been sent successfully sir.")
                print(f"The email to <{email_id}> with message: {msg} has been sent successfully sir.")

                time.sleep(10)
            except Exception as e:
                print(e)
                speak("Sorry Sir there is a problem, i can't send email\n")

        # Weather
        elif "weather" in command:
            speak("Enter the City name ")
            print("City name : ")
            city_name = takeCommand()
            if city_name == 'none':
                speak("City doesnt recognized")
                continue

            wm = WeatherService()
            result = wm.get_weather_data(city_name)

            if result == 'none':
                print("There is a problem, i cant tell the information")
                speak("There is a problem, i cant tell the information")
            else:
                print(result)
                speak(result)



        # Find location
        elif "locate " in command:
            location = command.split("locate ")[1]
            url = f"https://www.google.com/maps/place/{location}"
            speak(f"Searching {location} ..")
            webbrowser.get().open(url)
            time.sleep(8)

        elif "wait" in command or "stop" in command:
            speak("Stop listening for how much time sir ?")
            t = int(input("Time: "))
            speak(f"Stopped listening for {t} seconds")
            time.sleep(t)


        # command = play Romantic video on youtube.
        elif " youtube" in command and 'search' not in command:
            song = command.split("play ")[1]
            song = song.split(" on")[0]
            url = f"https://www.youtube.com/results?search_query={song}"
            webbrowser.get().open(url)
            speak(f"Showing results for {song}")
            time.sleep(8)


        elif 'search' in command:

            query = command.replace("search", "")
            webbrowser.open(query)
            time.sleep(15)

        elif "restart" in command:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in command or "sleep" in command:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "shut down" in command:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(10)
            subprocess.call(["shutdown", "/l"])

        # Random commands
        elif "Good Morning" in command:
            speak("A warm" + command)
            speak("How are you Mister")

        elif 'hey dear ' in command:
            speak("Hello Sir")

        elif "i love you" in command:
            speak("Stay in your limits...")

        elif 'alexa' in command:
            greetMe()
            speak("Yes sir, what can i do?")

        elif 'how are you' in command:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in command or "good" in command:
            speak("It's good to know that your fine")

        elif 'who are you' in command:
            speak("I am your assistant Sir...")

        elif 'thanks dear' in command:
            speak("welcome Sir, It's my Work")

        elif "shut up" in command:
            speak("okayyy sir...")
            time.sleep(10)

        elif 'none' in command:
            print("Sorry sir, I am unable to recognize, try to speak clear")
            speak("Sorry sir, I am unable to recognize, try to speak clear")
