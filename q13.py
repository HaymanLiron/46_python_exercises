def max_in_list(list_of_nums):
    # finds maximum number in list
    if len(list_of_nums) == 0:
        return "no numbers in list"
    maximum = list_of_nums[0]
    for num in list_of_nums:
        if type(num) != int:
            return "invalid input"
        if num > maximum:
            maximum = num
    return maximum

print(max_in_list([16,3,1,10]))