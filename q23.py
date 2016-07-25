import re


def correct(string):
    # 1) two or more occurrences of the space character is compressed into one, and
    # 2) inserts an extra space after a period if the period is directly followed by a letter.
    # E.g. correct("This   is  very funny  and    cool.Indeed!") returns "This is very funny and cool. Indeed!"
    string = re.sub('\s+', ' ', string)
    string = re.sub('\.', '. ', string)
    return string




