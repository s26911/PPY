import random

# Zad01
i = 5
tab1 = [[j for j in range(1, i + 1)] for i in range(1, i)]
# print(tab1)

# Zad02
napis = 'abcdef'
samogl = 'aiueo'
tab2 = [c for c in napis if c in samogl]
print(tab2)

# Zad03
n = 3
tab3 = [[random.randint(0, 100) for _ in range(n)] for _ in range(n)]
tab3t = [[tab3[i][j] for i in range(n)] for j in range(n)]
cross = [tab3t[i][i] for i in range(n)]


# print(tab3)
# print(tab3t)
# print(cross)

# Zad04
def fun(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_range(n):
    i = 0
    j = 2
    while i < n:
        if fun(j):
            yield j
            i += 1
        j += 1


tab4 = [i for i in prime_range(5)]
print(tab4)
