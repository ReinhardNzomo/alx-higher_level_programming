#!/usr/bin/pyhton3
def divisible_by_2(my_list=[]):
    even_list = []
    for x in my_list:
        if x % 2 == 0:
            even_list.append(True)
        else:
            even_list.append(False)
    return (even_list)
