import random

guess_name = []

correct_guesses = []
wrong_guesses = []
letters_guessed = [correct_guesses, wrong_guesses]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
"m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
"M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def load_name():
    name_list = ["Betsy", "Bailey", "Margaux", "Caesar",
    "Katie", "Joey", "Peyton", "Will", "Bess", "Elliot",
     "Anna", "Chris", "Alan", "Phyllis", "Justin", "Faith",
     "Novan", "Jasmine"]
    secret_name = random.choice(name_list)
    return secret_name

name = load_name()

name_character_list = list(name)

print(name)

def word_space():
    for character in name:
        guess_name.append("-")
    print("this word has " + str(len(name)) + " characters in it.")
    print(guess_name)

    # word_space = "-" * (len(name))
    # word_space = []
    # return list(word_space)


def is_word_guessed():
    incorrect_guesses = 10
    while incorrect_guesses > 0:
            guess = input("I choose: ")
            letter = guess

            if not guess in alphabet:
                print("Please, you can only enter letters of the alphabet. Try again.")
            elif guess in letters_guessed:
                print("That letter has already been guessed. Please enter a new character.")
            else:
                letters_guessed.append(guess)
            # word_space = word_space()
                if guess.lower() in name:

                    print("Yes! " + guess + " is in the word. Good job.")

                    correct_guesses.append(guess)
                    # guessed_value = name_character_list.index(word_space)
                    # word_space[name.index(letter)] = letter
                    # new_progress = ""

                    for i in range(0, len(name)):
                        if name[i] == guess:
                            guess_name[i] = guess
                            print(guess_name)
                        if not '-' in guess_name:
                            print("Congratulations! You have completed your mission. Treat yourself.")
                    #         new_progress += wordspace()
                    #
                    # new_progress = wordspace()



    	    # for dashes in word_space:
    	    #     print(word_space)
            #
            #     dashes(name.index(letter))
                else:
                    wrong_guesses.append(guess)
                    print( guess + " is not in the sercret name")
                    incorrect_guesses -= 1
                    if incorrect_guesses == 0:
                        print("I hate to tell you this, but you ran out of guesses. The name was " + name + ".")

def user_standing():
    # print("you have " + str(incorrect_guesses) + " guesses remaining.")
    print("correct guesses:" + str(correct_guesses))
    print("wrong guesses:" + str(wrong_guesses))


user_standing()
word_space()
is_word_guessed()




    # secret_word = load_word()
# spaceman(load_word())
