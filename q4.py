def is_vowel(char):
    # Write a function that takes a character (i.e. a string of length 1)
    # and returns True if it is a vowel, False otherwise

    #make sure it is a single letter
    if len(char) == 1 and char.isalpha():
        return True if char.lower() in ['a','e','i','o','u'] else False
    else:
        return "invalid input"


