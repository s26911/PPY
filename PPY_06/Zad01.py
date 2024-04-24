#### Zadanie 1
# * (1a) Zdefiniować klasę Książka, która będzie miała pola tytuł, autor,
# rok wydania, liczba stron. Zaimplementować metodę \_\_init\_\_,
# która przypisze wartości początkowe polom. Zdefiniować dwa obiekty
# klasy książka. Wydrukować wartości pól. Zmienić tytuł drugiej książki i
# ponownie wydrukować

# * (1b) Zdefiniować metodę cytowanie, która wydrukuje dane książki w estetyczny sposób

# * (1c) Nadpisać metodę \_\_len\_\_ tak, aby zwracała liczbę stron książki

# * (1d) Zdefiniować klasę Ebook, dziedziczącą z klasy ksiązka,
# która będzie miała dodatkowo pole format (np. epub). Nadpisać metodę
# cytowanie, tak, aby uwzględniała format. Zdefiniować obiekt klasy ebook
# i wywołać metodę cytowanie

class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania, liczba_stron):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.liczba_stron = liczba_stron

    def cytowanie(self):
        print("Tytul: {tytul}\nAutor: {autor}\nRok wydania: {rok}\nLiczba stron: {liczba}"
              .format(tytul=self.tytul, autor=self.autor, rok=self.rok_wydania, liczba=self.liczba_stron))

    def __len__(self):
        return self.liczba_stron

class Ebook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, liczba_stron, format):
        super().__init__(tytul, autor, rok_wydania, liczba_stron)
        self.format = format

    def cytowanie(self):
        print(f"Tytul: {self.tytul}\nAutor: {self.autor}\nRok wydania: {self.rok_wydania}\n"
              f"Liczba stron: {self.liczba_stron}\nFormat: {self.format}")


k1 = Ksiazka("...", "...", 2002, 200)
k2 = Ksiazka("ABC", "DEF", 2020, 100)

print("K1:")
print(k1.tytul)
print(k1.autor)
print(k1.rok_wydania)
print(k1.liczba_stron)

print("K2:")
print(k2.tytul)
print(k2.autor)
print(k2.rok_wydania)
print(k2.liczba_stron)

print("K2 zmieniony tytul:")
k2.tytul = "K2"
print(k2.tytul)

print("\nCytowanie:")
k1.cytowanie()

print("\nLEN:")
print(len(k1))

e = Ebook("OPASJDPOAJSFPASJF", "ASDASIPFPOFJ", 12390, 1223, "EPUB")
print("\nCYTOWANIE EBOOK:")
e.cytowanie()

