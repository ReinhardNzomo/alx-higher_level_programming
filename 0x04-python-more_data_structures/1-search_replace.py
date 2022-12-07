#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = list(map(lambda x: replace if x == search else x, my_list))
    return (copy)
    '''return [val if val != search else replace for val in my_list]'''
