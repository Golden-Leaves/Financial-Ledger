#It's a bit broken 😅, I've only learned to functions, I asked some of my friends to fix the ValueError and they told me to add "try:" and the "Except ValueError part"
#The rest I made myself😅 
import random

def number_generator():
    print("The numbers should only be from 1-99.")
    while True:
        try:
            lower = int(input("What do you want the lower bound to be: "))
            upper = int(input("What do you want the upper bound to be: "))
            if lower < 1 or upper > 99 or lower > upper:
                print("Input invalid, please enter an appropriate number.")
            else:
                break
        except ValueError:
            print("Input invalid, please enter numeric values.")
    Number = random.randint(lower, upper)
    return Number

def player_guess(number_guess):
    print("Please enter a Number from 1-99")
    while True:
        Guess = int(input("Which Number do you think is correct: "))
        if Guess > number_guess:
            print(f"{Guess} is larger than the Number")
        elif Guess > number_guess:
            print(f"{Guess} is larger than Number")
        elif Guess > 99 or Guess < 1:
            print("Please type in an appropriate Number")
        elif Guess == number_guess:
            print(f"You've won! {number_guess} was the correct answer.")
            break
        return Guess
        
Number = number_generator()
player_guess(Number)