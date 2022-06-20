from ast import Try
from multiprocessing.connection import Listener
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()

name = 'max'

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[6].id)
engine.setProperty('rate',180)

def talk(text):
    engine.say(text)  
    engine.runAndWait()


def listen():
    try:
        
        with sr.Microphone() as source:
            print("escuchando...")
            voice = listener.listen(source)
            rec =  listener.recognize_google(voice)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
    except:
        pass
    return rec

def run():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('reproduciendo ' + music)
        pywhatkit.playonyt(music)
    if 'tiempo' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %P')
        talk("Son las " + hora)
    if 'busca' in rec:
        order = rec.replace ("busca", '')
        info = wikipedia.summary(order, 1)
        talk(info)
    if 'termina' in rec or 'desactivate' in rec or 'gracias' in rec or 'adios' in rec:
        talk("Hasta la proxima")
        exit()
    else:
        print("No entendi, puedes repetir?")

run()

