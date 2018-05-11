#!/usr/bin/python3
import os

dirs = os.listdir(".")
scripts = []

for item in dirs:
    if item.endswith(".py") or item.endswith(".sh"):
        scripts.append(item)

while True:
    print("Please select one of the following scripts:")

    for i, script in enumerate(scripts):
        print(str(i) + " " + script)
        last_number = i + 1

    text = input('Please enter the number of the script you want to execute, if you want to quit enter stop: ')

    if text == 'stop':
        print("Thank you for using this script, we hope next time will be soon.")
        break
    else:

        text2 = input('Do you have any arguments to pass (please separate with a space)? If not, please leave blank: ')

        if text2 == "":

            os.system("./" + scripts[int(text)])
            print("\n")
        else:
            os.system("./" + scripts[int(text)] + " " + text2)
            print("\n")
