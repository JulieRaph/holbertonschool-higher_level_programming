#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    for number in my_list:
        if number not in unique:
            unique.append(number)
    for number in unique:
        return sum(unique)
