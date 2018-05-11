#!/usr/bin/python
import os
import sys

if len(sys.argv) == 1:
    print("Please give a directory name as an argument!")
    exit(0)

elif len(sys.argv) > 2:
    print("Too many arguments provided, please enter only a single directory name!")
    exit(1)

argument = sys.argv[1].split("/")

if argument == "/":
    position = -2
else:
    position = -1

os.mkdir("./" + argument[position] + "-links")

output = os.listdir(sys.argv[1])

for item in output:
    os.symlink(sys.argv[1] + item, "./" + argument[-1] + "-links/" + item)

results = os.listdir("./" + argument[-1] + "-links")
results.sort()

for result in results:

    #print("./" + argument[-2] + "-links/" + result + " -> " + sys.argv[1] + "/" + result)
    print("./%s-links/%s -> %s/%s") %(argument[-2], result, sys.argv[1], result)
