import functools


def max_in_list(list_of_nums):
    # get the maximum number in a list using the reduce function
    return functools.reduce(lambda x, y: x if (x > y) else y, list_of_nums)
