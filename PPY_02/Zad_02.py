import random

tab1 = []
tab2 = []

for i in range(0, 5):
    tab1.append(random.randint(0, 10))
for i in range(0, 10):
    tab2.append(random.randint(0, 10))

print(set(tab1).union(set(tab2)))
print(set(tab2).difference(tab1))

