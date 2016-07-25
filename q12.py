def histogram(list_of_ints):
    # draws a histogram with each row having * of length of corresponding integer
    # assumes valid input
    for num in list_of_ints:
        for i in range(num):
            print("*", end="")
        print("")  # creates a new line
