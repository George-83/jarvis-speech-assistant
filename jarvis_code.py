import pyttsx3
import speech_recognition as sr
import os
import sys
import webbrowser


def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


talk("Hello sir, how can I help you?")


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        # Here you can change language, for example "language=ru-RU"
        # But in this case, also, you should change language for keywords in commands
        my_command = r.recognize_google(audio, language="en-GB").lower()
        print("You said: " + my_command + "\n")
    except sr.UnknownValueError:
        talk("Sorry, I did not understand you")
        my_command = command()

    return my_command


# This function defines commands and keywords
# You can change them depending on your needs
def do_something(my_command):
    if "open moscow times" in my_command:
        URL = "https://www.moscowtimes.ru/news"
        webbrowser.open(URL)
        talk("Ready")
    elif "finish" in my_command:
        talk("Ok, I have closed the program")
        sys.exit()


while True:
    do_something(command())
