# * (1a) W folderze projektu ręcznie utworzyć plik test.txt, zawierający kilka napisów.
#        Wczytwać plik i wyświetlić zawartość.
# * (1b) Do pliku test2.txt przepisać te wiersze, które mają długość dłuższą niż 5.
#        Każdy wiesz powinien być zapisany w nowej linii. Wykorzystać funkcję split oraz list comprehension.
# * (1c) Utworzyć listę list 10x10, zawierającą liczby rzeczywiste z zakresu (0, 1) (wykorzystać random.uniform).
#        Zapisać utworzoną tablicę do pliku, każda lista w nowej linijce, elementy listy rozdzielone spacjami,
#        liczby z dokładnością do dwóch cyfr po kropce dziesiętnej. Bez spacji na końcu linijki,
#        bez entera na końcu pliku.
# * (1d) wczytaj z pliku pierwszy wiersz i umieść wczytane liczby na liście (jako liczby, nie napisy)
import random

# 1a
print("1A")
lines = ""
with open("test.txt", "r") as f:
    lines = f.read()
    for line in lines.split(sep="\n"):
        print(line)
print(lines)

# 1b
print("\n1B")
with open("test2.txt", "w") as f2:
    long_Lines = [[j for j in i] for i in lines.split(sep="\n")]
    for i in long_Lines:
        if len(i) > 5:
            # print("".join(i))
            f2.write("".join(i) + "\n")

# 1c
print("\n1C")
lista = [[random.uniform(0, 1) for _ in range(10)] for _ in range(10)]
with open("test3.txt", "w") as f3:
    for i in range(10):
        line = lista.pop(0)
        for j in range(10):
            f3.write(f"%.2f" % line.pop(0))
            if j != 9:
                f3.write(" ")
        if i != 9:
            f3.write("\n")

# 1d
print("\n1D")
with open("test3.txt", "r") as f4:
    line = f4.readline()
    lista_liczb = [float(i) for i in line.split(" ")]

    for i in lista_liczb:
        print(i)
