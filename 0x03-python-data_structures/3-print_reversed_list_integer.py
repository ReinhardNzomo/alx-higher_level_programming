#!/usr/bin/python
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        for x in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[x]))
