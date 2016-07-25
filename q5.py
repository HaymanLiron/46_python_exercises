def translate(string):
    #double every consonant and place an occurrence of "o" in between
    output = ""
    for _ in string:
        if _.isalpha() and _ not in ['a', 'e', 'i', 'o' ,'u']:
            output += _ + 'o' + _
        else:
            output += _
    return output

