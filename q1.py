def find_max(a,b):
    #finds the maximum of two values
    if type(a) == type(b):
        return a if (a > b) else b
    else:
        return "invalid input, both must match"