def average_word_length(file_name):
    # read entire book, and calculate average word length
    word_counter = 0
    letter_counter = 0
    f = open(file_name, "r")
    for line in f.readlines():
        for word in line.replace('-',' ').split():
            word_counter += 1
            letter_counter += len(word)
    return 1.0 * letter_counter / word_counter

