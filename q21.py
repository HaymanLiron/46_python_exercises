def char_freq(string):
    # builds a frequency listing of characters in a string
    freq_dict = {}
    for _ in string:
        if _ in freq_dict:
            freq_dict[_] += 1
        else:
            freq_dict[_] = 1
    return freq_dict

