def max_of_three(a,b,c):
    #finds the maximum of three values
    if type(a) == type(b) == type(c):
        if a >= b and a >= c:
            return a
        elif b >= c:
            return b
        else:
            return c
    else:
        return "invalid input, both must match"