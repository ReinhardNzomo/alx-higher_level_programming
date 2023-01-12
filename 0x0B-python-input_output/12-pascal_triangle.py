#!/usr/bin/python3

"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    list_of_tri = [[1]]

    for i in range(n - 1):
        temp_list = [0] + list_of_tri[-1] + [0]
        row = []
        for j in range(len(list_of_tri[-1]) + 1):
            row.append(temp_list[j] + temp_list[j + 1])
        list_of_tri.append(row)

    return list_of_tri
