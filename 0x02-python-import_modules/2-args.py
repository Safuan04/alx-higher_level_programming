#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenght = len(argv) - 1
    if (lenght == 1):
        print("{} argument:".format(lenght))
    elif (lenght == 0):
        print("{} arguments.".format(lenght))
    else:
        print("{} arguments:".format(lenght))
    for i in range(lenght):
        print("{}: {}".format((i + 1), argv[i + 1]))
