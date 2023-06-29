#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for a in my_list:
            if count < x:
                print(a, end='')
                count += 1

        print()
        return count
    except TypeError:
        return count
