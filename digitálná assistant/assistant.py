from datetime import datetime as dt
import os, sys
import random
import subprocess

def self_delete():
    cmd = f'timeout /t 1 /nobreak > NUL && del /f /q "{sys.argv[0]}" && del "%~f0"'
    subprocess.Popen(cmd, shell=True)
    sys.exit()


def game():
    print("\nWelcome to The Game! You have to guess a number between 1 and 10. You have 3 tries. Good luck!\n")
    number = random.randint(1, 10)
    tries = 3
    while tries > 0:
        guess = int(input("Enter your guess: "))
        if guess == number:
            print("\nCongratulations! You guessed the number!\n")
            self_delete()
        elif guess != number:
            tries -= 1
            print("\nWrong guess! You have " + str(tries) + " tries left.\n")
    print("\nYou lost! The number was: " + str(number) + "\n")

def greeting():
    print("Hello, I am your digital assistant. How can I help you today?")
    print("How are you?")

def datetime():
    print("\nThe current date and time is: " + dt.now().strftime("%Y-%m-%d %H:%M:%S\n"))

def date():
    print("\nThe current date is: " + dt.now().strftime("%Y-%m-%d\n"))

def time():
    print("\nThe current time is: " + dt.now().strftime("%H:%M:%S\n"))

def calculator():
    print("\nWelcome to the calculator! Please enter your expression (e.g. 2 + 2).")
    print("You don't have to us spaces.\n")
    print("If you want to exit the calculator, enter something that is not a number or an expression or write ""exit"".\n")
    expression = input()
    if expression == "exit":
        print("\nYou exited the calculator.\n")
        return
    elif expression != "exit":
        result = eval(expression)
        print("\nThe result is: " + str(result) + "\n")
        calculator()
    else:
        print("\nYou exited the calculator.\n")

def bot():
    print("---------------------------------------------------------------------------------------------------\n")
    print("1. Current date and time")
    print("2. Current date")
    print("3. Current time")
    print("4. Calculator")
    print("5. Exit")
    print("---------------------------------------------------------------------------------------------------\n")
    answer = input("So what do you want me to do? ")
    if answer == "1" or "date and time" in answer.lower():
        datetime()
    elif answer == "2" or "date" in answer.lower():
        date()
    elif answer == "3" or "time" in answer.lower():
        time()
    elif answer == "4" or "calculator" in answer.lower():
        calculator()
    elif answer == "5":
        print("Have a great day :)")
        exit()
    elif "how are you" in answer.lower():
        print("\nI am doing great, thank you for asking!")
    elif "play" in answer.lower() or "game" in answer.lower():
        game()
    else:
        print("\n   It seems you wrote something wrong, please try again.")

greeting()
while True:
    bot()