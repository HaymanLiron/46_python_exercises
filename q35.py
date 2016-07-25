def speak_ICAO(string):
    # does not have the functionality of linking it to TTS software
    aviation_words = {'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo', 'f': 'foxtrot',
         'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett', 'k': 'kilo', 'l': 'lima',
         'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa', 'q': 'quebec', 'r': 'romeo',
         's': 'sierra', 't': 'tango', 'u': 'uniform', 'v': 'victor', 'w': 'whiskey',
         'x': 'x-ray', 'y': 'yankee', 'z': 'zulu'}
    output = ""
    for _ in string:
        if _.isalpha():
            output += aviation_words[_.lower()] + " "
    return output

print(speak_ICAO("hello"))
