#!/usr/bin/python
import os

file_list = []
content = {'name': , 'content':}

if not os.path.exists('./aggregated'):
    os.makedirs("./aggregated")

print('Parsing experiment result files in current directory...done')
print('Creating directory \"aggregated\"...done\n')
print('IP addresses encountered:')

for root, dirs, filenames in os.walk('./testdir'):
    for file in filenames:
        if file.endswith('.txt'):
            a,b = file.split('_')

            if a not in file_list:
                file_list.append(a)

file_list.sort()

for root, dirs, filenames in os.walk('./testdir'):
    for i, item in enumerate(file_list):


for i, item in enumerate(file_list):
    print('   - ' + file_list[i])

print(' ')

for i, item in enumerate(file_list):
    print('Writing combined dataset to \"aggregated/' + file_list[i] + '.txt\"')

    write = open('./aggregated/' + file_list[i] + '.txt', 'w')
    write.write('Parsing experiment result files in current directory...done\n')
    write.write('Creating directory \"aggregate\"...done\n\n')
    write.write('IP addresses encountered:\n')
    write.close()

print(' ')
print('Aggregation completed!')
