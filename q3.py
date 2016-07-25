def find_len(string):
    #find the length of a string without using the len() function
    return sum([1 for _ in string])
print(find_len("hello"))