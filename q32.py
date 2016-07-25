# Write a version of a palindrome recogniser that accepts a file name from the user,
# reads each line, and prints the line to the screen if it is a palindrome.


def is_palindrome(string):
    # checks for a palindrome, with punctuation, capitalization, and spacing ignored
    string = string.lower()
    for punctuation in [" ", ".", ",", "'", "?"]:
        string = string.replace(punctuation, "")
    return True if string == string[::-1] else False


f = open("q32", "r")
for line in f.readlines():
    line = line.strip("\n")
    if is_palindrome(line):
        print(line)

f.close()
