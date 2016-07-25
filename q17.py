def is_palindrome(string):
    # checks for a palindrome, with punctuation, capitalization, and spacing ignored
    string = string.lower()
    for punctuation in [" ", ".", ",", "'", "?"]:
        string = string.replace(punctuation, "")
    print(string)
    return True if string == string[::-1] else False