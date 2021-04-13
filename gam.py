import instaloader

def panel():
    print("[1] => Info About Application <= ")
    print("[2] => SnakeGame 1s game <= ")
    print("[3] => SecretGame 2s game <= ")
    print("[4] => Info About files/directories <= ")
    print("[5] => Download Image from INSTAGRAM <= ")
    print(" ")

def imge():
    iginit = instaloader.Instaloader()
    who = input("USERNAME FROM INSTAGRAM")
    iginit.download_profile(who, profile_pic_only = True)

def main():
   print("WELCOME ON PANEL ABOUT GAME IN WINDOW")
   print(" ")
   panel()

   way = int(input("Your choice from menu ==> "))

   if way == 1:
       pass
   elif way == 2:
       pass
   elif way == 3:
       pass
   elif way == 4:
       pass
   elif way == 5:
       imge()

   print("  ")

main()