import random
import time
import os

# Clear console (just got this from google lol)
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

inventory = []
player_name = ""
#Attributes (In order LtR): Strength, Dexterity, Intelligence, Wisdom
player_attributes = []

def main():
    print("Welcome.")
    change_player_name()
    clear()
    
    while True:
        print(f"{player_name}.")
        choice = input("Would you like to change this name? (Yes / No): ") # Call .lower() method
        
        if choice == "yes":
            change_player_name()
        elif choice == "no":
            break
        else:
            clear()
            print("I need a yes or no...")
    
    print(f"Good.")
    print(f"Now choose {player_name}'s skills:")
    print(f"")

def change_player_name():
    global player_name
    player_name = ""
    while player_name == "":
         player_name = input("Enter your character's name: ")

def chapter1():
    print(f"{player_name} arises in a dark cavern,")
    print(f"The Earth's heart trembles, {player_name} collapses onto the uneven cave floor.")
    print(f"Echos of the rumble dissapear into the stone surroundings.")
    print(f"Blinded in pitch blackness, {player_name} feels the floor for equipment...")

def obtainItem(item_name, amount):
    print(f"{amount} {item_name} aquired!")
    inventory.append(f"{item_name}:{amount}")

def death():
    print(f"You have lead {player_name} to their death.")
    print("Perhaps it was inevitable.")
    input("Press [ENTER] to send a new victim...")
    main()

main()