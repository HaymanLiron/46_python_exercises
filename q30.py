import functools


def translate(string):
    english_to_swedish = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new":"nytt", "year":"år"}
    translated = list(map(lambda x: english_to_swedish[x], string.split(" ")))
    output = ""
    for word in translated:
        output += word + " "
    return output



