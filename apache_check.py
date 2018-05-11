#!/usr/bin/python
import sys
import time
import datetime

text = 'failed'

print('Starting to monitor apache-status.txt in current directory')

while True:

    file = open('apache-status.txt', 'r')
    content = file.read()
    file.close()

    if content == "test":

        print('\nFile hasn\'t updated, something is wrong!\nCheck the other process fetching the status!')
        exit(1)

    else:
        if text in content:
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

            print('\n[' + st + '] Apache entered a failed state!')

            file = open('apache-status.txt', 'w')
            file.write("test")
            file.close()

        else:
            sys.stdout.write('.')
            sys.stdout.flush()

            file = open('apache-status.txt', 'w')
            file.write("test")
            file.close()

    time.sleep(60)
