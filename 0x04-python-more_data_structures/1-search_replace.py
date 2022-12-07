#!/usr/bi/python3
def search_replace(my_list, search, replace):
    copy = [val if val != search else replace for val in my_list]
    return (copy)
