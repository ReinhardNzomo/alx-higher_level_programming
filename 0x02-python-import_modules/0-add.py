#!/usr/bin/python3
if __name__ == '__main__':
    from add_0 import add
    add = __import__('add_0').add
    a, b = 1, 2
    print('{} + {} = {}'.format(a, b, add(a, b)))
