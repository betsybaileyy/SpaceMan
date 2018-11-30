import random

guess_name = []
correct_guesses = []
wrong_guesses = []
letters_guessed = [correct_guesses, wrong_guesses]

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
"m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
"M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Creating a list of names to choose from at random.
def load_name():
    name_list = ["betsy", "bailey", "margaux", "caesar",
    "katie", "joey", "peyton", "will", "bess", "elliot",
     "anna", "chris", "alan", "phyllis", "justin", "faith",
     "novan", "jasmine"]
    secret_name = random.choice(name_list)
    return secret_name

# Creating a simplified variable that will represent the secret name.
name = load_name()

length_name = len(name)

# Taking the characters from an individual name and separating them into objects in a list.
name_character_list = list(name)

# Here now for purposes of testing code.
print(name)

# Creating dashes to indicate letters in the name that have not been guessed yet.
def name_space():
    for character in name:
        guess_name.append("-")
    print("this name has " + str(len(name)) + " characters in it.")
    print(guess_name)

# Fuction to verify correct guesses and indicate when the name has been guessed.
def is_name_guessed():
    incorrect_guesses = 7

    #  Creating a while loop that will run as long as the user has remaining guesses.
    while incorrect_guesses > 0:
            guess = input("I choose: ")
            letter = guess

    # Preventing the user from entering a non-alphabetical character or a previously guessed one. Adds guessed letter to a complete list of guessed characters.
            if not guess in alphabet:
                print("Please, you can only enter letters of the alphabet. Try again.")
            elif guess in letters_guessed:
                print("That letter has already been guessed. Please enter a new character.")
            else:
                letters_guessed.append(guess)

            # Here we are verifying if the guessed letter is in the secret name and adding it to a list of correctly guessed letters (if correct).
                if guess.lower() in name:
                    print("Yes! " + guess + " is in the word. Good job.")
                    correct_guesses.append(guess)

            # Creating a loop to iterate through each character of the name to either print the name with the correctly guessed letters for user to see
            # as well as indicate the word has been correctly guessed and to stop looping.
                    for i in range(0, length_name):
                        if name[i] == guess:
                            guess_name[i] = guess
                            print(guess_name)

                    if not '-' in guess_name:
                        print("Congratulations! You have completed your mission. Mars will have to wait another day..")
                        print("Treat yourself!!!!!")

            # If the guessed letter is not in the secret name, add it to a list of wrong guesses. Add it to list of incorrectly guessed letters.
                else:
                    wrong_guesses.append(guess)
                    print( guess + " is not in the sercret name")
                    # Removing a guess from remaining guesses.
                    incorrect_guesses -= 1
                    # Indicates to the user that they have lost the game.
                    if incorrect_guesses == 0:
                        print("I hate to tell you this, but you ran out of guesses. The name was " + name + ".")

# A helpful visualization for the user that lists previous guesses.
def user_standing():
    # TO DO: the line below (commented out) keeps crashing file with error - need to better understand scope for a variable like this.
    # print("you have " + str(incorrect_guesses) + " guesses remaining.")
    print("correct guesses:" + str(correct_guesses))
    print("wrong guesses:" + str(wrong_guesses))

# Calling the functions to make Spaceman, The Game, run.
user_standing()
name_space()
is_name_guessed()
