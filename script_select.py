#!/usr/bin/python3
import os

dirs = os.listdir(".")
scripts = []
i = 1
# stop = "stop"


for item in dirs:
    if item.endswith(".py"):
        scripts.append(item)

while True:
    print("Please select one of the following scripts:")

    for i, script in enumerate(scripts):
        print(str(i) + " " + script)
        last_number = i + 1

    # choice = input('Please enter the number of the script you want to execute, if you want to quit enter ' + str(last_number) + ': ')
    blabla = input('Please enter the number of the script you want to execute, if you want to quit enter stop: ')

    print(blabla)

    if blabla == 'stop':
        print("Thank you for using this script, we hope next time will be soon.")
        break
    else:
        os.system("./" + scripts[int(blabla)])
        print("\n")
