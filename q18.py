def is_pangram(string):
    # checks if string contains all letters of alphabet at least once
    # capitalization is not important
    string = string.lower()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z']
    for _ in string:
        if _ in letters:
            letters.remove(_)
    return False if letters else True