import speech_recognition as sr
import pyttsx3

import pywhatkit
import urllib.request

import json
import datetime

import wikipedia

name = 'cortana'
key  = 'AIzaSyBxmHmIdGML0lGQUMjeGTpF4oc1pKkLmbA'

listener = sr.Recognizer()
engine   = pyttsx3.init()

voices   = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def Talk(text):

    engine.say(text)
    engine.runAndWait()

def listen():

    try:

        with sr.Microphone() as source :
            
            print("Escuchando...")

            voice = listener.listen(source)
            rec   = listener.recognize_google(voice)
            rec   = rec.lower()

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

        Talk('Reproduciendo' + music)

        pywhatkit.playonyt(music)

    if 'Cuantos suscrictores tiene' in rec :


        Name_Subs = rec.replace('Cuantos suscrictores tiene', '')

        data = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channel?part=statistics&forUsername=' + Name_Subs.strip() + '&key=' + key).read()

        subs = json.loads(data) ["items"] [0] ["statistics"] ["subscriberCount"]

        Talk(Name_Subs + "tiene {:,d}".format(int(subs)) + " suscriptores!")
    
    if 'hora' in rec:

        hora = datetime().now().strftime('%H:%M %p')

        Talk("Son las " + hora)

    elif 'busca' in rec:

        order = rec.replace('busca', '')

        info = wikipedia.summary(order, 1)

        Talk(info)

    else:

        Talk("Vuelve a intentarlo")

while True:
    
    run()