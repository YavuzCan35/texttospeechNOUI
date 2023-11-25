import gtts
import time
from playsound import playsound
import os

def konus(st):
    tts = gtts.gTTS ( st, lang="tr", slow=False, lang_check=False )
    tts.save ( f"audio.mp3" )
    audio_file = os.path.dirname ( __file__ ) + fr'/audio.mp3'
    playsound ( f"audio.mp3",True )
    os.remove ( audio_file )
while True:
    a=0
    a=str(input('Söylenecekler: '))
    konus(a)
