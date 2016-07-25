def generate_n_chars(n, c):
    # function that takes in integer n and character c
    # and returns c n times
    if not (type(n) == int and type(c) == str):
        return "invalid input"
    else:
        output = ""
        for i in range(n):
            output += c
        return output
