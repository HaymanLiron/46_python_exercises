def only_brackets(string):
    output = ""
    for _ in string:
        if _ in ["[", "]", "{", "}", "(", ")"]:
            output += _
    return output


def is_balanced(string):
    # method is to start from the right and if it is a RHS bracket, check if LHS neighbour matches
    # if so, pop both
    # otherwise move to next character
    # if you've gone through whole string and made no changes, it means it is not balanced
    # if string is empty, it means it is balanced
    string = only_brackets(string)
    changed = True
    while changed and len(string) > 0:
        changed = False
        i = len(string) - 1
        while i > 0 and not changed:
            if string[i] in ["]", "}", ")"]:
                if string[i-1: i+1] in ["[]", "{}", "()"]:
                    string = string[:i-1] + string[i+1:]
                    changed = True
            i -= 1
    if len(string) == 0:
        return "Balanced"
    else:
        return "Not balanced"

