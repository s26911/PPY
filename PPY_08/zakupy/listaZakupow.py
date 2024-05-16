from zakupy.exceptions import BelowZero


class ListaZakupow:
    def __init__(self, lista=None):
        if lista is None:
            self.lista = []
            self.sumaryczna_cena = 0
        else:
            self.lista = lista
            self.sumaryczna_cena = 0
            for i, j in lista:
                self.sumaryczna_cena = self.sumaryczna_cena + i.cena_jednostkowa * j

    def dodaj_towar(self, towar, ilosc):
        if towar.cena_jednostkowa < 0 or ilosc < 0:
            raise BelowZero(towar.cena_jednostkowa if towar.cena_jednostkowa < 0 else ilosc)
        self.sumaryczna_cena = self.sumaryczna_cena + towar.cena_jednostkowa * ilosc
        self.lista.append([towar, ilosc])
