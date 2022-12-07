#!/usr/bi/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return None
    copy = []
    copy = [val if val != search else replace for val in my_list]
    return (copy)
