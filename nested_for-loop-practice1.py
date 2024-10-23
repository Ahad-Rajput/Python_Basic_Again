list = [5, 2, 5, 2, 2]

for x in list:
    output = ''
    for y in range(x):
        output += 'x'
    print(output)

list = [5, 2, 5, 2, 2]

for x in list:
    print('')
    for y in range(x):
        print('x', end='')