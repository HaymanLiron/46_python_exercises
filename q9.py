def is_member(val, list_of_vals):
    # mimic the functionality of the in operator without using it
    # check if val is in list_of_vals
    for elem in list_of_vals:
        if val == elem:
            return True
    return False