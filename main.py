import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
def listen_to_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    return r.recognize_google(audio)
def speak(text):
    engine.say(text)
    engine.runAndWait()
while True:
    text = listen_to_voice()
    if "hola" in text:
        speak("Hola, ¿en qué puedo ayudarte?")
    elif "adios" in text:
        speak("Hasta luego")
        break
    else:
        speak("No entiendo lo que dices")
