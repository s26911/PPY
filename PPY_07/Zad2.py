# * (2a) Mamy planszę do gry w kółko i krzyżyk, która jest listą list, zawierających puste napisy '' o
#        rozmiarze nxn. Zdefiniować n i utworzyć planszę korzystając z list comprehension.
# * (2b) Należy wczytać od użytkownika dwie liczby całkowite, które będą oznaczały współrzędne pola do wstawienia
#        nowego znaku. Wczytywać pętlą while, aż użytkownik poda liczby całkowite. Wykorzystać blok
#        try - except i wyjątek ValueError
# * (2c) Zdefiniować własny wyjątek, który będzie obsługiwał sytuację, gdy wczytane liczby są poza zakresem planszy.
#        Wyjątek powinien posiadać docstring i drukować odpowiedni komunitat, zawierający wprowadzone liczby i wymagany
#        zakres liczb. Wykorzystać ten wyjątek w pętli while wczytującej liczby.

# 2a
print("2A")
n = 3
plansza = [[" " for j in range(n)] for i in range(n)]
print(plansza)

# 2b
print("\n2B")
x = -1
y = -1
while True:
    try:
        x = input("Podaj pierwsza liczbe: ")
        if int(x) > n or int(x) < 1:
            raise ValueError
        else:
            break
    except:
        print("Sprobuj ponownie")

while True:
    try:
        y = input("Podaj pierwsza liczbe: ")
        if int(y) > n or int(y) < 1:
            raise ValueError
        else:
            break
    except:
        print("Sprobuj ponownie")

# 2c
print("\n2C")
class MyException(Exception):
    """Podano liczbe spoza zakresu planszy"""
    def __init__(self, input, plansza_size):
        self.input = input
        self.plansza_size = plansza_size
        message = f"Liczba {input} znajduje sie poza zakresem planszy. Dopuszczalne wartosci to od 0 do {plansza_size}"
        super().__init__(message)

x = -1
y = -1
while True:
    try:
        x = input("Podaj pierwsza liczbe: ")
        if int(x) > n or int(x) < 1:
            raise MyException(x, n)
        else:
            break
    except Exception as e:
        print(e)

while True:
    try:
        y = input("Podaj pierwsza liczbe: ")
        if int(y) > n or int(y) < 1:
            raise MyException(y, n)
        else:
            break
    except Exception as e:
        print(e)
