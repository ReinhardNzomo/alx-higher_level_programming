#!/usr/bi/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return None
    return (value if value != search else replace for value in my_list)
