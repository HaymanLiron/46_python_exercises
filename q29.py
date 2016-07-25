def filter_long_words(list_of_words, n):
    return list(filter(lambda x: len(x) > n, list_of_words))
