def overlapping(a,b):
    # checks if lists a and b have at least one common element
    # uses nested if-loops to satisfy the requirements of the question
    # even though it's not very efficient
    for elem_a in a:
        for elem_b in b:
            if elem_a == elem_b:
                return True
    return False