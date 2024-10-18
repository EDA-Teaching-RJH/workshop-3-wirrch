import random
import time

inventory = []
player_name = ""

def main():
    while player_name == "":
        player_name = input("Enter player name: ")

    

    print("Good...")
    print(f"{player_name} arises in a dark cavern,")
    print(f"The Earth's heart trembles, {player_name} collapses onto the uneven cave floor.")
    print(f"Echos of the rumble dissapear into the stone surroundings.")
    print(f"Blinded in pitch blackness, {player_name} feels the floor for equipment...")

#def chapter1():


def obtainItem(item_name, amount):
    print(f"{amount} {item_name} aquired!")
    inventory.append

def death():
    print(f"You have lead {player_name} to their death.")
    print("Perhaps it was inevitable.")
    input("Press [ENTER] to send a new victim...")
    main()

main()