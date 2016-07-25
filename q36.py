def only_alpha(word):
    output = ""
    for _ in word:
        if _.isalpha():
            output += _
    return output

def find_hapax(file_name):
    # read entire book, and have a dictionary, where key is word
    # and value is number of times it appears
    # once you have the dictionary, any key which has value 1
    # is a hapax legomonon

    words_dict = {}
    f = open(file_name, "r")
    for line in f.readlines():

        for word in line.lower().replace('-',' ').split():
            word = only_alpha(word)
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

    hapax_list = []
    for key in words_dict.keys():
        if words_dict[key] == 1:
            hapax_list.append(key)
    return hapax_list