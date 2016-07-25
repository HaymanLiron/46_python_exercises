def find_longest_word(list_of_words):
    if len(list_of_words) == 0:
        return "no words in list"
    else:
        longest_length = len(list_of_words[0])
        for word in list_of_words:
            if type(word) != str:
                return "invalid parameters"
            if len(word) > longest_length:
                longest_length = len(word)
        return longest_length
