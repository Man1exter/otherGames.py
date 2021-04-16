import instaloader
import sys
import pygame
import os
from sgame import seek
import io
from gtts import gTTS
from win32com.client import Dispatch

def panel():
    print("[1] => Info About Application <= ")
    print("[2] => SnakeGame 1s game <= ")
    print("[3] => SecretGame 2s game <= ")
    print("[4] => Info About files/directories <= ")
    print("[5] => Download Image from INSTAGRAM <= ")
    print("[6] => Voice Channel (yours text) <= ")
    print(" ")

def imge():
    print("it is good if you write lowercase => username <=")
    iginit = instaloader.Instaloader()
    who = input("USERNAME FROM INSTAGRAM ===> ")
    iginit.download_profile(who, profile_pic_only = True)
    print(" ")
    print("everything is ready....")


def infoapp():
    pass


def ss11():
    print("My first game with pygame...")
    seek()

def main():
   print("WELCOME ON PANEL ABOUT GAME IN WINDOW")
   print(" ")
   panel()

   way = int(input("Your choice from menu ==> "))

   if way == 1:
       infoapp()
   elif way == 2:
       ss11()
   elif way == 3:
       pass
   elif way == 4:
       pass
   elif way == 5:
       imge()
   elif way == 6:

       print(" ")
       print("Bot say your text..")
       
       with io.BytesIO() as file:
        text = input("Enter your text ==> ")
        gTTS(text=text, lang="en").write_to_fp(file)
        file.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        speak = Dispatch("SAPI.SpVoice").Speak
        speak(text)
        text = input("Enter your text ==> ")

   elif way == 7:
       pass 


   print("  ")

main()