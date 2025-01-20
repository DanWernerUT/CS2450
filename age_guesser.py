import random

def guessAge():
    print("Hello! Im going to try to guess your age.")
    name = input("What's your name? ")
    minAge = 15
    maxAge = 30
    guessed = False

    while not guessed:
        age_guess = int((maxAge+minAge)/2)
        ui = input(f"Are you at least {age_guess} years old? (y/n): ").strip().lower()
        if ui == "y":
            ui_2 = input(f"Are you {age_guess} years old? (y/n): ").strip().lower()
            if ui_2 == "y":
                print(f"{name}, you are {age_guess} years old!")
                guessed = True
            elif(ui_2):
                minAge = age_guess
                print("Rats")
        elif ui == "n":
            maxAge = age_guess
            print("Rats")
        else:
            print("Please enter 'y' for yes or 'n' for no.")
            
guessAge()
