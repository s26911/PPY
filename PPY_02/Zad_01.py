r = list(range(0, 101, 5))

print(r[::-1]) # od końca

print(r[1::2]) # co drugi

print(r[0:int(len(r)/2)]) # pierwsza połowa

print(sum(r) / len(r)) # średnia arytm.

r.remove(90) # usunąć 90

first = r.pop(0) # zamienić pierwszy i ostatni
last = r.pop()
r.insert(0, last)
r.append(first)

r = tuple(r)  # jako krotka

x = r[1]    # przypisania
y = r[len(r) - 2]


print(r)
