ceny = {'a' : 2.5, 'b' : 7, 'c' : 10}
lista_zakupow = {}

produkt = input('Podaj produkt do dodania na liste')
ilosc = input('Podaj ilosc')

lista_zakupow[produkt] = float(ilosc)

print(set(lista_zakupow.keys()).intersection(ceny.keys()))

suma = 0
t = set(ceny.keys())
for i in lista_zakupow.keys():
    x = ceny.get(i)
    if x is not None:
        suma += x * lista_zakupow.get(i)

print(suma)
