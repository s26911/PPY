x = int(input('Wprowadz liczbe: '))
czyParzysta = x % 2 == 0

x = int(input('Wprowadz liczbe: '))
while (x % 2 == 0) != czyParzysta:
    czyParzysta = (x % 2 == 0)
    x = int(input('Wprowadz liczbe: '))

