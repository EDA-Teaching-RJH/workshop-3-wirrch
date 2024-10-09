import random
import time

inventory = []
playerName = ""

def main():
    input("You wake to the sound of a window smashing.")
    input("Creeping through the dark halls of your flat,")
    input("you hear scurrying of feet against the carpet behind you")
    input("and before you can turn to face your intruder,")
    input("you get knocked to the floor and fall unconscious.")
    input("You wake, alone in the dry heat of the Brazilian streets.")
    gameName = "WELCOME TO BRAZIL"
    for char in gameName:
        print(char, end="")
        time.sleep(0.2)

main()