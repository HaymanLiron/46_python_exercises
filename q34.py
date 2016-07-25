def print_dict_formatted(my_dict):
    sorted_keys = sorted(my_dict.keys())
    for key in sorted_keys:
        if key == "\n":
            print("\\n" + " " + str(my_dict[key]))
        else:
            print(key + "  " + str(my_dict[key]))


def char_freq_table(file_name):
    # builds a frequency listing of the characters contained in the file,
    # and prints a sorted and nicely formatted character frequency table to the screen

    f = open(file_name, "r")
    freq_dict = {}
    for line in f.readlines():
        for char in line:
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    print_dict_formatted(freq_dict)
    f.close()

char_freq_table("q32")