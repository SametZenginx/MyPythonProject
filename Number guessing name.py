# Number guessing game
from random import choice
import time
print("Hello")
list = range(1,10)
number = choice(list)
print("I take a number(between 0 to 10). Can you know??\nType 'q' to exit.")
while True:
    a = input("Try it: ")
    a = a.lower()
    if a == "q":
        print("Exiting...")
        break
    else:
        a = int(a)
        if a == number:
            print("You knew the number. Congratulations...")
            break
        elif a < number:
            time.sleep(0.50)
            print("Increase your guessed number.")
            time.sleep(1)
            continue
        elif a > number:
            time.sleep(0.50)
            print("Decrease your guessed number.")
            time.sleep(1)
            continue
        else:
            print("please enter a valid value.")
