#!/usr/bin/python3
import sys
if len(sys.argv) == 2:
    print("1 argument:")
    print("1: " + sys.argv[1])
elif len(sys.argv) == 1:
    print("0 arguments.")
else:
    print(len(sys.argv) - 1 , "arguments:")
    for i in range(1,len(sys.argv)):
        print(str(i) + ": " + str(sys.argv[i]))

