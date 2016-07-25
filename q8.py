def is_palindrome(string):
    # check if a string is a palindrome
    # ignore spaces
    string = string.replace(" ", "")
    return True if string == string[::-1] else False