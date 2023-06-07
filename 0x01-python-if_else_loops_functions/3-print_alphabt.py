#!/usr/bin/python3
for abcs in range(97, 123):
    if abcs == 101:
        continue
    elif abcs == 113:
        continue
    print("{}".format(chr(abcs)), end="")
