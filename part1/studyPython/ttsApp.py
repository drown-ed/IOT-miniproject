# TTS (Text To Speech)
# pip install gTTs
# pip install playsound

from gtts import gTTS
from playsound import playsound

text = '안녕하세요, 오유리나입니다.'
tts = gTTS(text=text, lang='ko', slow = False)
tts.save('part1/studyPython/output/hi.mp3')
print('완료!')
playsound('part1/studyPython/output/hi.mp3')
