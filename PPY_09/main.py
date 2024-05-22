import datetime


class Data:
    def __init__(self, dzien, miesiac, rok):
        if int(dzien) < 1 or int(dzien) > 31 or int(miesiac) < 1 or int(miesiac) > 12 or int(rok) < 0:
            raise Exception(f"Wprowadzono nieprawidlowa date: {dzien}.{miesiac}.{rok}")
        self.dzien = dzien
        self.miesiac = miesiac
        self.rok = rok

    def __lt__(self, other):
        s = datetime.date(self.rok, self.miesiac, self.dzien)
        o = datetime.date(other.rok, other.miesiac, other.dzien)
        return s < o

    def __eq__(self, other):
        return self.rok == other.rok and self.miesiac == other.miesiac and self.dzien == other.dzien

    def __str__(self):
        return f"{self.dzien}.{self.miesiac}.{self.rok}"

d1 = Data(1, 2, 2020)
d2 = Data(1, 2, 2021)
d3 = Data(10, 2, 2022)

print(d1 > d2)


class Notatka:
    counter = -1

    def __init__(self, data, tekst):
        self.id = Notatka.counter
        Notatka.counter = Notatka.counter + 1
        self.data = data
        self.tekst = tekst

    def __str__(self):
        return f"#{self.id} {self.data} {self.tekst}"

    def set_id(self, id):
        self.id = id


n = Notatka(d1, "crazy")


class Terminarz:
    def __init__(self):
        self.notatki = []

    def dodaj_notatke(self, data, tekst):
        self.notatki.append(Notatka(data, tekst))

    def wyswietl_notatki_sorted(self):
        sort = sorted(self.notatki, key=lambda x: x.data)
        for n in sort:
            print(n)

    def wyswietl_notatki(self):
        for n in self.notatki:
            print(n)

    def usun_notatke(self, id):
        self.notatki.pop(id)
        for i, n in enumerate(self.notatki):
            n.set_id(i)

    def zapisz(self, file_name):
        with open(file_name, "w") as f:
            for n in self.notatki:
                f.write(str(n) + "\n")



t = Terminarz()
t.dodaj_notatke(d1, "crazy? i was crazy once")
t.dodaj_notatke(d2, "they locked me in the room")
t.dodaj_notatke(d1, "a rubber room")
t.dodaj_notatke(d3, "a rubber room with rats")
t.dodaj_notatke(Data(12, 1, 2023), "and rats make me crazy")
t.wyswietl_notatki()
print()
print()
t.usun_notatke(1)
t.wyswietl_notatki()
t.zapisz("file1.txt")

t.dodaj_notatke(Data(input("Podaj dzien: "), input("Podaj miesiac: "), input("Podaj rok: ")), input("Wpisz tekst: "))
t.zapisz("file2.txt")
