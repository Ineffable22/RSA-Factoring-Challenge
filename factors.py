#!/usr/bin/python3
from sys import argv
with open(argv[1], "r") as fo:
    txt = fo.read()

i = 0
while txt[i]:
    b = 2
    line = 0
    while txt[i] != '\n' and txt[i] != '\0':
        line = int(txt[i]) + (line * 10)
        i += 1

    while b != line:
        if line % b == 0:
            print("{}={}*{}".format(int(line), int(line // b), b))
            break
        b += 1
    i += 1
    if i >= len(txt):
        break
