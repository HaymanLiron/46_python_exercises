# write your own functions for map(), filter() and reduce()


def my_own_map(my_list):
    # higher order code example:
    # return list(map(lambda x: x*x, list_of_num))
    def applied_function(x):
        return x
    output = []
    for _ in my_list:
        output.append(applied_function(_))
    return output


def my_own_filter(my_list):
    # higher order code example:
    # return list(filter(lambda x: x%2, list_of_num))
    def filter_function(x):
        return x % 2
    output = []
    for _ in my_list:
        if filter_function(_):
            output.append(_)
    return output


def my_own_reduce(my_list):
    # higher order code example:
    # import functools
    # return list(reduce(lambda x, y: x if (x > y) else y, list_of_num))
    def filter_function(x, y):
        return x if (x > y) else y
    while len(my_list) > 1:
        my_list[1] = filter_function(my_list[0], my_list[1])
        my_list.pop(0)
    return my_list[0]

