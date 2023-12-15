import pyttsx3
from gtts import gTTS
from io import BytesIO
import pygame

engine = pyttsx3.init()

pygame.mixer.init()

def speak(text):
    mp3_fp = BytesIO()
    tts = gTTS(text=text, lang='pt')      
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    pygame.mixer.music.load(mp3_fp)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

print("Escreva o que você quer dizer e aperte enter para que o audio seja reproduzido:")
while True:
    Input = input()
    speak(Input)
    