import functools


def find_longest_word(list_of_words):
    # only using higher order functions now
    return functools.reduce(lambda x, y: x if (len(x) > len(y)) else y, list_of_words)
