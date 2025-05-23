import random
from art import logo

def check_answer(u_gues, actual_answer):
    if u_gues == chosen_number:
        print(f"You got it! The answer was {actual_answer}")
    elif u_gues < chosen_number:
        print("To low.")
    elif u_gues > chosen_number:
        print("To high.")

def set_difficulty():
    difficulty = input("Chose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return easy_level
    else:
        return hard_level

chosen_number = random.randint(1, 100)
easy_level = 10
hard_level = 5

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thingking of a number between  1 and 100.")

    level = set_difficulty()

    guess = 0
    while guess != chosen_number:
        print(f"You have {level} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        check_answer(u_gues=guess, actual_answer=chosen_number)

        if guess != chosen_number:
            print("Guess again.")

        if level != chosen_number:
            level -= 1
            if level == 0:
                print("You've run out of guesses. ")
                return

game()