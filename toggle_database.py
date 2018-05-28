#!/usr/bin/python3

import sys
import os

file = sys.argv[1] + sys.argv[2] + '.sqlite'
database = sys.argv[2] + '.sqlite'

if sys.argv[2] == 'production' or sys.argv[2] == 'testing':
    pass
else:
    print("Invalid target!")
    exit(1)

if os.path.exists(file):
    print('Target ' + sys.argv[2] + ' is valid')
    print('Checking existence of directory...done.')
    print('Checking existence of target file...done.')
else:
    if os.path.exists(sys.argv[1]):
        print('Directory does not exist!')
        exit(1)
    else:
        print('File does not exists!')

print('Checking existence of symlink...done.')

if os.path.islink(sys.argv[1] + 'db.sqlite'):
    os.unlink(sys.argv[1] + 'db.sqlite')
    print('Removing symlink...done.')

print('Symlinking '+ sys.argv[2] + '.sqlite as db.sqlite... done.')

os.symlink(file, sys.argv[1] + 'db.sqlite')

if os.path.islink(sys.argv[1] + 'db.sqlite'):
    print('Validating end result... done.')
else:
    print('End result could not be validated!')
    exit(1)
