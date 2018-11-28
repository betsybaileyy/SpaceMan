import random

letters_guessed = []
correct_guesses = []

name_list = ["Betsy", "Bailey", "Margaux", "Caesar", "Katie", "Joey", "Peyton", "Will", "Bess", "Elliot", "Anna", "Chris"]
secret_name = random.choice(name_list)

guesses = 10
word_space= "-" * len(secret_name)

while guesses > 0
    print("guess a letter!")
    guess = input("I choose: ")

    if guess in secret_name:



def letter_input():
    letter_guess = imp
