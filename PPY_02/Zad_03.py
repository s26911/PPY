import random

list = []
for i in range(0,100):
    list.append(random.randint(0,10))

print(list)

dict = {}
for i in range(11):
    dict[i] = list.count(i)

print(dict)


