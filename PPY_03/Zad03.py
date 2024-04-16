import random

tab = []
for i in range(10):
    tab.append(random.randint(0, 100))

x = None
for i in tab:
    if i % 2 == 0 and (i < x or x is None):
        x = i

if x != 1:
    print(tab)
    print('Najmiejsza parzysta liczba to {}'.format(x))
else:
    print(tab)
    print('W tablicy nie ma zadnych parzystych liczb')
