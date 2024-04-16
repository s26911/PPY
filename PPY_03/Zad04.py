import random

rowNum = 10
colNum = 10

tab = []
for i in range(colNum):
    row = []
    for y in range(rowNum):
        row.append(random.randint(0, 100))
    tab.append(row)

for i in tab:
    for y in i:
        print(str(y) + '\t', end='')
    print()

print('MAX:')
for i in range(colNum):
    max = -1
    for y in range(rowNum):
        if tab[y][i] > max:
            max = tab[y][i]

    print(str(max) + '\t', end='')
    
print()
