#!/usr/bin/envpython3
# Created By:Deepak
# Date: 10/16/2026
# This program is based on a random number guessing game,
# which asks the user to input a number.
import random


def main():

    # Get a random number between 0 and 9
    correct_number = random.randint(0, 9)

    # Get a guessed number from the user
    guessed = int(input("Guess a random number in the range of 0-9: "))

    # Check if the number is the same as the correct number

    if guessed == correct_number:

        # If correct then tell the user they guessed correctly
        print("You Guessed Correct!")

    if guessed != correct_number:

        # If not correct then tell the user they guessed incorrectly
        print("You Guessed Incorrect! The correct answer was", correct_number)


if __name__ == "__main__":
    main()
