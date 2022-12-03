#!/usr/bin/python
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        my_list.reverse()
        for x in range(len(my_list)):
            print("{}".format(my_list[x]))
