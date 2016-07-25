# anagram game
import random
# randomly pick a word w from list
words_list = []
f = open("words.txt", "r")
for word in f.readlines():
    words_list.append(word.replace("\n", ""))

random_word = words_list[random.randint(0, len(words_list) - 1)]
word_to_guess = random_word
random_word = list(random_word)


# randomly permute w
for i in range(len(random_word)):
    swap_with = random.randint(i, len(random_word) - 1)
    random_word[i], random_word[swap_with] = random_word[swap_with], random_word[i]

word = ""
for _ in random_word:
    word += _

# present anagram to user
print("The anagram is " + word)

# guess original word
guessed_word = False
while not guessed_word:
    guess = input("Please guess word: ")
    if guess == random_word:
        guessed_word = True
        print("Congratulations, you guessed the word!")
    else:
        print("Incorrect, please guess again")