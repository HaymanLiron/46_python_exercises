# game of Lingo
# hidden word, 5 charcters long
# after each guess, a player receives 2 clues:
# 1. characters that are fully correct (right character in right position) - marked by square brackets
# 2. characters that appear in the word but are in the wrong position - marked by round brackets
import random

WORD_LENGTH = 5


def choose_word():
    word_list = ["tiger", "snake", "zebra", "mouse", "sheep", "whale", "panda"]
    return word_list[random.randint(0, len(word_list) - 1)]


def get_valid_guess():
    # validates the user guess, not checking for types of characters input, but yes checking that length is correct
    guess_valid = False
    while not guess_valid:
        guess = input("What is your next guess? Remember word is " + str(WORD_LENGTH) + " characters long!")
        if len(guess) != WORD_LENGTH:
            print("Input is not the right length!")
        else:
            guess_valid = True
    return guess


def user_guess(actual_word):
    # get guess from user
    guess = get_valid_guess()
    if guess == actual_word:
        return "Correct!"
    output = ""
    for i in range(len(guess)):
        if guess[i] == actual_word[i]:
            output += "[" + guess[i] + "]"
        elif guess[i] in actual_word:
            output += "(" + guess[i] + ")"
        else:
            output += guess[i]
    return output


def play_game():
    # choose a word
    actual_word = choose_word()
    guessed = False
    # keep on taking guesses until the user guesses the word
    while not guessed:
        outcome = user_guess(actual_word)
        print(outcome)
        if outcome == "Correct!":
            guessed = True
    return None


def main():
    play_game()


if __name__ == '__main__':
    main()



