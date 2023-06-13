#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    biggest_value = my_list[0]

    for integer in my_list:
        if integer > biggest_value:
            biggest_value = integer
    return biggest_value
