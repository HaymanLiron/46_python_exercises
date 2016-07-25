# semordnilap finder
# reverses a word and then checks if that new word appears elsewhere in the dictionary

def semordnilap_finder():
    f = open("q33", "r")
    words = f.readline().split(",")  # assume words are split with commas
    output = []
    while len(words) > 1:
        if words[0][::-1] in words:
            output.append(words[0] + " " + words[0][::-1])
            words.remove(words[0][::-1])
            words.pop(0)
        else:
            words.pop(0)
    return output



