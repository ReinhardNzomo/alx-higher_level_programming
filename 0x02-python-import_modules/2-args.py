#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    len_argv = len(sys.argv) - 1
    if (len_argv == 0):
        print("0 arguments.")
    elif (len_argv == 1):
        print("1 argument:")
    else:
        print("{} arguments:".format(len_argv))
    for x in range(len_argv):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
