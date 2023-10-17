import random as rnd

def run():
    MinVal = int(input("Enter minimum value: "))
    MaxVal = int(input("Enter maximum value: "))
    RandoNum = rnd.randrange(MinVal, MaxVal)
    guessed = False
    while not guessed:
        Guess = input(f"Guess the number I'm thinking of between {MinVal} and {MaxVal}")