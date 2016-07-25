def add_line_numbers(text_file, new_file):
    f = open(text_file, "r")
    g = open(new_file, "w")
    line_counter = 1
    for line in f.readlines():
        line_to_add = str(line_counter) + " " + line
        g.write(line_to_add)
        line_counter += 1
    f.close()
    g.close()


