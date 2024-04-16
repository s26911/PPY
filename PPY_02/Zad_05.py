k1 = {'autor': 'a0', 'tytul': 't0', 'rok': 0}
k2 = {'autor': 'a1', 'tytul': 't1', 'rok': 1}
k3 = {'autor': 'a0', 'tytul': 't2', 'rok': 2}

l = [k1, k2, k3]
print(l)
print()

for i in l:
    if i.get('autor') == 'a0':
        print(i)

