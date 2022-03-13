import webbrowser as web
import googlesearch as gs
import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import *
import wikipedia
import pyjokes

#import requests
from GoogleNews import GoogleNews
import os

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            # if 'hello' in command:
            #     command = command.replace('hello', '')
            #     print(command)
    except Exception as e:  # speech is unintelligible
        talk(e)
        print("Could not understand audio")
    return command


def run_inform():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'current time' in command:
        time = datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'today news' in command:
        googlenews=GoogleNews(lang='en',region='IN')
        time1 = date.today()
        googlenews.set_lang('en')
        googlenews.set_time_range(time1,time1)
        googlenews.get_news(command)
        googlenews.search(command)
        googlenews.get_page(1)
        #googlenews.set_encode('utf-8')
        text=googlenews.get_texts()
        print(text)
        talk(text)

    elif 'open google chrome' in command:
        talk('opening google chrome')
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

    elif 'open adobe' in command:
        talk('opening adobe reader')
        os.startfile('C:\Program Files (x86)\Adobe\Reader 10.0\Reader\AcroRd32.exe')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif'current location'in command:
        talk('your locatin is opening')
        web.open('https://www.google.com/maps/place/Wagholi,+Pune,+Maharashtra+412207/@18.5739731,73.9443482,13z/data=!3m1!4b1!4m5!3m4!1s0x3bc2c3819fdef877:0xd4193e985f354be0!8m2!3d18.5807719!4d73.9787063')

    elif 'search' in command:
        pe =command.replace('search', '')
        gs.search(pe)
        talk("searching"+command)
        web.open_new_tab(pe)
    else:
        talk('Please say the command again.')


while True:
    run_inform()