import time 
import random
def generate_numbers():
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
    return number1, number2
def addition(number1,number2):
    Question_answer = number1 + number2
    timer = 0
    while True:
        print(f"What's {number1} + {number2} ?")
        player_answer = int(input())
        if player_answer == Question_answer:
            print("Correct!")
            return player_answer
        else:
            print("Incorrect!")
        while True:
         timer += 1
         time.sleep(1)
         print(f"Elapsed time: {timer}", end = "\r")
number1, number2 = generate_numbers()
addition(number1, number2)

    