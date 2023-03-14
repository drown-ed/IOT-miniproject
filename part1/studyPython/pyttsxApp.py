# pip install pyttsx3

import pyttsx3

tts = pyttsx3.init()
tts.say('Hi~')
tts.runAndWait()