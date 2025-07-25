import os
import webbrowser as wb
from typing import Union

# Basic app info - displayed in title (see line 13)
title = "Interest Calculator"
versn = 1.0
authr = "John Fiore"
repos = "https://github.com/john-fiore/Interest-Calculator"

clear = lambda: os.system('cls')

combo = Union[int, float]

def init():
    os.system('color 0A') # sets terminal colors. 0 = Black BG, A = Lime Green FG.
    os.system(f'title {title} (v{versn}) - by {authr}')

def calculate(principle: combo, rate: combo, time: combo):
    clear()

    ratedec = round(rate / 100, 2)
    interest = round(principle * ratedec * time, 2)
    
    clear()
    print(f"Total Interest of ${interest}")
    print()
    input("Press Enter to continue...")
    main()


def printHowto():
    clear()
    print("===========================")
    print("=     How to use the      =")
    print("=   Interest Calculator   =")
    print("===========================")
    print("= FORMULA: I = PRT        =")
    print("===========================")
    print("= P = Starting Amount     =")
    print("= R = Percentage          =")
    print("= T = Amount of Time      =")
    print("===========================")
    input("Press Enter to Continue...")
    main()
        

def main():
    clear()
    print("===========================")
    print("=   Interest Calculator   =")
    print("===========================")
    print("= 1. Start                =")
    print("= 2. How to use           =")
    print("= 3. Github               =")
    print("===========================")
    choice = input("> ")

    if choice == "1":
        clear()
        p = float(input("P: "))
        r = float(input("R: "))
        t = float(input("T: "))
        calculate(p, r, t)
    elif choice == "2":
        printHowto()
    elif choice == "3":
        wb.open(repos)
    else:
        print("Error: invalid option!")
        input()
        return
if __name__ == "__main__":
    init()
    main()
