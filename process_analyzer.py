#!/usr/bin/python3

file = open('process-list.txt', 'r')
content = file.readlines()
user_invoked = 0
active = []
counts = []

for i, line in enumerate(content):
    if line.__contains__("      \_ "):
        user_invoked += 1
    if line.__contains__('.sh'):
        # line.split('\_', 1)
        active.append(line[13:23])

items = list(set(active))
items.sort()

for count in items:
    counts.append(active.count(count))


print('Parsing process-list.txt in current directory... done.')
print('Analysing process list... done.\n')
print('Total number of processes: ' + str(i))
print('User-invoked processes :' + str(user_invoked) + '\n')
print('Active scripts (*.sh):\n')
for i, element in enumerate(items):
    print('    ' + str(counts[i]) + 'x ' + items[i])
