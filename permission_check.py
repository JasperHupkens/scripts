#!/usr/bin/python

import sys
import os

if len(sys.argv) == 1:
    print("Oops, no variable entered.\n Use as follows: ./permission_check.py <full path directory>")
    exit(1)

watson = 1000
test = 1001

filename_1 = sys.argv[1] + '/test1.txt'
permission_1 = 0o755

filename_2 = sys.argv[1] + '/test2.txt'
permission_2 = 0o611

filename_3 = sys.argv[1] + '/test3.txt'
permission_3 = 0o667

filename_4 = sys.argv[1] + '/test4.txt'
permission_4 = 0o655

filename_5 = sys.argv[1] + '/test5.txt'
permission_5 = 0o633

if os.path.exists(sys.argv[1]):

    print('Ok, path exists!')

    # Check file 1
    if os.path.exists(filename_1):
        print('Ok, file 1 exists!')

        if os.stat(filename_1).st_uid == watson and os.stat(filename_1).st_gid == test:
            print('Ownership OK!')
        else:
            os.chown(filename_1, watson, test)
            print('Ownership changed!')

        if oct(os.stat(filename_1).st_mode) == '0100755':
            print('Permission OK!')
        else:
            os.chmod(filename_1, permission_1)
            print('Permissions changed!')

    else:
        os.mknod(filename_1, permission_1)
        os.chown(filename_1, watson, watson)

        print('File 1 created!')

    # Check file 2
    if os.path.exists(filename_2):

        print('Ok, file 2 exists!')

        if os.stat(filename_2).st_uid == test and os.stat(filename_2).st_gid == watson:
            print('Ownership OK!')
        else:
            os.chown(filename_2, test, watson)
            print('Ownership changed!')

        if oct(os.stat(filename_2).st_mode) == '0100611':
            print('Permission OK!')
        else:
            os.chmod(filename_2, permission_2)
            print('Permissions changed!')

    else:
        os.mknod(filename_2, permission_2)
        os.chown(filename_2, watson, watson)

        print('File 2 created!')

    # Check file 3
    if os.path.exists(filename_3):

        print('Ok, file 3 exists!')

        if os.stat(filename_3).st_uid == watson and os.stat(filename_3).st_gid == watson:
            print('Ownership OK!')
        else:
            os.chown(filename_3, watson, watson)
            print('Ownership changed!')

        if oct(os.stat(filename_3).st_mode) == '0100667':
            print('Permission OK!')
        else:
            os.chmod(filename_1, permission_1)
            print('Permissions changed!')

    else:
        os.mknod(filename_3, permission_3)
        os.chown(filename_3, watson, watson)

        print('File 3 created!')

    # Check file 4
    if os.path.exists(filename_4):

        print('Ok, file 4 exists!')

        if os.stat(filename_4).st_uid == watson and os.stat(filename_4).st_gid == watson:
            print('Ownership OK!')
        else:
            os.chown(filename_4, watson, watson)
            print('Ownership changed!')

        if oct(os.stat(filename_4).st_mode) == '0100655':
            print('Permission OK!')
        else:
            os.chmod(filename_4, permission_4)
            print('Permissions changed!')

    else:
        os.mknod(filename_4, permission_4)
        os.chown(filename_4, watson, watson)

        print('File 4 created!')

    # Check file 5
    if os.path.exists(filename_5):

        print('Ok, file 5 exists!')

        if os.stat(filename_5).st_uid == test and os.stat(filename_5).st_gid == test:
            print('Ownership OK!')
        else:
            os.chown(filename_5, test, test)
            print('Ownership changed!')

        if oct(os.stat(filename_5).st_mode) == '0100633':
            print('Permission OK!')
        else:
            os.chmod(filename_5, permission_5)
            print('Permissions changed!')

    else:
        os.mknod(filename_5, permission_5)
        os.chown(filename_5, watson, watson)

        print('File 5 created!')
else:

    print('Directory doens\'t exist try another one')
