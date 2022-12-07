#!/usr/bi/python3
'''def search_replace(my_list, search, replace):
    if not my_list:
        return None
    copy = []
    copy = [val if val != search else replace for val in my_list]
    return (copy)'''


def search_replace(my_list, search, replace):
    copy = []
    for a in range(len(my_list)):
        if my_list[a] != search:
            copy.append(my_list[a])
        else:
            copy.append(replace)
    return copy
