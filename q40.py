# anagram game
import random


def list_to_str(my_list):
    output = ""
    for _ in my_list:
        output += _
    return output


def get_words_from_dict():
    # randomly pick a word w from list
    words_list = []
    f = open("words.txt", "r")
    for word in f.readlines():
        words_list.append(word.replace("\n", ""))
    return words_list


def choose_word(words_list):
    desired_word_length = int(input("What is the maximum length you want?"))

    random_word = words_list[random.randint(0, len(words_list) - 1)]
    while len(random_word) > desired_word_length:
        random_word = words_list[random.randint(0, len(words_list) - 1)]
    word_to_guess = random_word
    random_word = list(random_word)
    return random_word


def permute_word(random_word):
    # randomly permute w
    for i in range(len(random_word)):
        swap_with = random.randint(i, len(random_word) - 1)
        random_word[i], random_word[swap_with] = random_word[swap_with], random_word[i]
    word = ""
    for _ in random_word:
        word += _
    return word


def guess_word(word_to_guess):
    # guess original word
    guessed_word = False
    while not guessed_word:
        guess = input("Please guess word: ")
        if guess == word_to_guess:
            guessed_word = True
            print("Congratulations, you guessed the word!")
        else:
            print("Incorrect, please guess again")


def play_game():
    # get the word list from the text file
    words_list = get_words_from_dict()
    # choose a random word from the list
    random_word = choose_word(words_list)
    # store this word
    word_to_guess = list_to_str(random_word)
    # permute the word into an anagram
    permuted_word = permute_word(random_word)
    # present anagram to user
    print("The anagram is " + permuted_word)
    # get the user to guess the word
    guess_word(word_to_guess)


play_game()


