def sum_numbers(numbers):
    # sum numbers in a list without using sum function
    answer = 0
    for num in numbers:
        if type(num) == int:
            answer += num
    return answer


def multiply_numbers(numbers):
    # multiply numbers in a list
    answer = 1
    for num in numbers:
        if type(num) == int:
            answer *= num
    return answer
