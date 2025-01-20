import random

def guessAge():
    print("Hello! Im going to try to guess your age.")
    name = input("What's your name? ")
    minAge = 15
    maxAge = 30
    guessed = False
    
    while not guessed:
        age_guess = random.randint(minAge, maxAge)
        ui = input(f"Are you {age_guess} years old? (y/n): ").strip().lower()
        if ui == "y":
            print(f"{name}, you are {age_guess} years old!")
            guessed = True
        elif ui == "n":
            print("Rats")
        else:
            print("Please enter 'y' for yes or 'n' for no.")

guessAge()

