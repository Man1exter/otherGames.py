import instaloader
import sys
import pygame
import os
from sgame import seek
from sec import Game
import io
import pyttsx3

import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def panel():
    print("[1] => Info About Application <= ")
    print("[2] => SnakeGame 1s game <= ")
    print("[3] => SecretGame 2s game <= ")
    print("[4] => Info About files/directories <= ")
    print("[5] => Download Image from INSTAGRAM <= ")
    print("[6] => Voice Channel (yours text) <= ")
    print("[7] => PASSSSSSSSSSSSSSSSSSSSSS <= ")
    print("[8] => info about phonenumbers... <= ")
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

def ss12():
    print("SECRET GAME ABOUT RULONICKA BANDICKA..")
    Game()

def voiceBot():
    
       print(" ")
       
       print("Bot say your text..")

       engine = pyttsx3.init()

       text = input("Enter Your Text..... =====> ")

       engine.say(text)

       engine.runAndWait()

       print(" ")

def number_phone_function():
    print(" ")
    print("ATTENTION DONT FORGET => +48... <= OR SOMETHING LIKE THAT...")

    y = input("write phonenumber => ")
    x = phonenumbers.parse(y, None)
    print(x)

    x2 = phonenumbers.is_possible_number(x)
    print("is possible number? =>",x2)

    x3 = phonenumbers.is_valid_number(x)
    print("is valid number? =>",x3)

    #country.. 
    print("from where is use the number? =>",geocoder.description_for_number(x, 'pl'))

    #services..
    print("services of phonenumber? =>",carrier.name_for_number(x, 'pl'))

    #timezone..
    print("timezone =>",timezone.time_zones_for_number(x))

    print(" ")

def main():
   print("WELCOME ON PANEL ABOUT GAME IN WINDOW + other useful function (programs)")
   print(" ")
   panel()

   way = int(input("Your choice from menu ==> "))

   if way == 1:
       infoapp()
   elif way == 2:
       ss11()
   elif way == 3:
       ss12
   elif way == 4:
       pass
   elif way == 5:
       imge()
   elif way == 6:
       voiceBot()
   elif way == 7:
       print(" ")
       pass 
       print(" ")
   elif way == 8:
       number_phone_function()

   print("  ")

main()