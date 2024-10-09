import random
def main():
    randnumber = random.randint(1, 10)
    userGuess(randnumber)

def userGuess(randnum):
    guess = int(input("Guess my number between 1 and 10: "))

    if guess > randnum:
        print("Too high")
    elif guess < randnum:
        print("Too low")
    else:
        print("Nice one")
        return
    
    userGuess(randnum)

main()