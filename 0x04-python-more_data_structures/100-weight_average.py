#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    prod_num = 0
    total = 0
    for tup_le in my_list:
        prod_num += (tup_le[0] * tup_le[1])
        total += tup_le[1]

    return (prod_num / total)
