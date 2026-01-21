#!/usr/bin/python3

def max_integer(list=[]):
    if len(list) == 0:
        return None
    max_value = list[0]
    for num in list:
        if num > max_value:
            max_value = num
    return max_value
