def words_to_list_of_lengths(list_of_words):
    # maps a list of words into a list of integers representing the lengths of the corresponding words
    output = []
    for word in list_of_words:
        output.append(len(word))
    return output
