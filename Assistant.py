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
# from ecapture import ecapture as ec


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)  
    engine.runAndWait()

# Greets the user According to the current time.
def greetMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir ")
    

    speak(" I am Your Personal Assistent, How can i help you ? ")

# takes command as your voice and returns text.
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
        # command = takeCommand()
        command = "romantic songs on youtube "
        
        # Search about a person on wikipedia
        if 'wikipedia' in command:
            speak("Searching for Wikipedia sir, Please Wait.....!")
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            print(results)
            speak("Sir, According to Wikipedia" + results)
        
        elif 'open youtube' in command:
            speak("Opening Youtube Sir... ")
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            speak("Opening Google Sir... ")
            webbrowser.open("google.com")

        elif 'play music' in command:
            music_dir = 'H:\\Multimedia\\songs'
            songs = os.listdir(music_dir)
            randomsong = random.randint(1, 496)
            speak("Enjoy The Music Dear Sir... ")
            os.startfile(os.path.join(music_dir, songs[randomsong]))

        # informs the current time
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

        # shows the top 3 news
        # NEWS API Key:- 01922e11ddb44bd2b9bf29caa50abc32
        elif 'news' in command:
            r = requests.get('http://newsapi.org/v2/top-headlines?country=in&apiKey=01922e11ddb44bd2b9bf29caa50abc32')
            data = json.loads(r.content)
            for i in range(3):
                print(data['articles'][i]['title'])
                print(data['articles'][i]['url'])
                speak(data['articles'][i]['description'])
                
            speak("sir, All the links are given you can checkout your own ")

        # send mail to your given emails and message
        elif 'send mail' in command:
            try:
                print("Email Sender: ")
                speak("Enter The Email id's sir")
                emailids = input("Email id's: ")
                emailids = emailids.split(", ")


                speak("What should i say sir?")
                msg = input("Message: ")
                # You can also use the takecommand() function to send msg from your own voice.
                # message = takeCommand()

                sendmail(to_emails = emailids, text = msg)
                print("Succesfull...")
                speak("Your Email is Sent Sir...")

            except Exception as e:
                print(e)
                speak("Sorry Sir there is a problem, i can't send email\n")

        # Search Place module
        elif "where is" in command:
            query = command.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        # Stop listening for a given time
        elif 'wait' in command or 'stop' in command:
            speak("Sure sir, For how much time ?") 
            value = int(input("Time: ")) 
            time.sleep(value)
        # search on youtube
        elif " on youtube" in command:
            search_command = command.split("on")[0]
            url = f"https://www.youtube.com/results?search_query={search_command}"
            webbrowser.get().open(url)

            speak(f"Showing Reasults for {search_command}") 
            time.sleep(10)   
        # opening your github account
        elif "open github" in command:
            speak("Opening Github Sir")
            webbrowser.open("https://github.com/HarshalSongra")
            
        

        elif 'hey dear ' in command:
            speak("Hello Sir, How are u ?")
        
        elif 'who are you' in command:
            speak("I am your assistent Sir...")

        elif 'thanks dear' in command:
            speak("welcome Sir, It's my Work")

        #elif "camera" in query or "take a photo" in command:
            #ec.delay_imcapture(0, False, False, 2)

        else:
            speak("Sorry sir, i can't getting what you want to say, can you please repeat\n")
