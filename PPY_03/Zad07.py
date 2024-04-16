h = int(input('Podaj wysokosc: '))

maxWidth = 1 + (h - 1) * 2
for i in range(1, h + 1):
    chars = 'a' * ((i - 1) * 2 + 1)
    space = ' ' * int((maxWidth - len(chars) / 2))
    print(space + chars + space)
