#!/usr/bin/python3
def no_c(my_string):
    for x in my_string:
        if (x == "c" or x == "C"):
            index_x = my_string.rfind(x)
            my_string = (my_string[:index_x] + my_string[(index_x + 1):])
    return (my_string)
    """
    new_string = ""
    for x in range(len(my_string)):
        if (my_string[x] != "c" and my_string[x] != "C"):
            new_string += my_string[x]
    return new_string
    """
