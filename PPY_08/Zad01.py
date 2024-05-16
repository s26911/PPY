from zakupy import towar, listaZakupow


lista1 = [(towar.Towar("jablko", 2), 2), (towar.Towar("orang", 1), 1)]
lista2 = [(towar.Towar("ban", 2), 2), (towar.Towar("kiui", 3), 2)]

lista_zakupow1 = listaZakupow.ListaZakupow(lista1)
lista_zakupow2 = listaZakupow.ListaZakupow()
for i in lista2:
    lista_zakupow2.dodaj_towar(i[0], i[1])

print(lista_zakupow1.sumaryczna_cena)
print(lista_zakupow2.sumaryczna_cena)
