def filter_long_words(list_of_words, n):
    # takes in a list_of_words and returns all words in list longer than n characters
    output = []
    for word in list_of_words:
        if len(word) > n:
            output.append(word)
    return output
