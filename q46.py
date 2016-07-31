# using a dictionary, break a word into two smaller words by taking alternate letters
# and if both of those smaller words are real words,
# print them both out


def break_up_word(word):
    if len(word) > 1:
        return word[::2], word[1::2]
    return word, ""


def find_alternades():
    f = open("q43.txt", "r")
    word_list = []
    for _ in f.readlines():
        word_list.append(_[:-1])
    for word in word_list:
        word_1, word_2 = break_up_word(word)
        if word_1 in word_list and word_2 in word_list:
            print("\"{}\": makes \"{}\" and \"{}\".".format(word, word_1, word_2))
    f.close()


find_alternades()