#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    '''tuple smaller than 2?use the 0 for each missing integer'''
    '''managing tuple_a'''
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    elif len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    '''managing tuple_b'''
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)

    new_tuple = (int(tuple_a[0]) + int(tuple_b[0]),
                 int(tuple_a[1]) + int(tuple_b[1]))

    return new_tuple
'''
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
'''
