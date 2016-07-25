# Write a program that maps a list of words into a list of integers
# representing the lengths of the corresponding words.
# Write it in three different ways:
# 1) using a for-loop
# 2) using the higher order function map()
# 3) using list comprehensions.


def word_list_to_int_list_1(list_of_words):
    # method 1
    output = []
    for word in list_of_words:
        output.append(len(word))
    return output


def word_list_to_int_list_2(list_of_words):
    # method 2
    return list(map(len, list_of_words))


def word_list_to_int_list_3(list_of_words):
    return [len(word) for word in list_of_words]



