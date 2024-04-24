#### Zadanie 2 (kółko i krzyżyk raz jeszce)
# * (2a) Zdefiniować klasę PlanszaTicTacToe, która będzie miała pole rozmiar oraz pole plansza.
# Zdefiniować metodę \_\_init\_\_, która jako argument przyjmuje rozmiar planszy i tworzy pustą
# planszę (lista list zawierających ' ' o rozmiarze rozmiar x rozmiar)

# * (2b) Dla klasy PlanszaTicTacToe napisać metody drukuj (estetyczny wydruk planszy)
# oraz wstaw(x, y, znak) - metoda wstawia znak w pole o współrzędnych x, y

# * (2c) Zdefiniować klasę GraTicTacToe, która ma pola: plansza, aktualny zawodnik i wynik.
# Metoda \_\_init\_\_ przyjmuje jako argumenty rozmiar planszy i znak rozpoczynającego zawodnika
# (x lub o) i ustawia odpowiednie wartości pól (wykorzystać obiekt klasy PlanszaTicTacToe).
# _Dobra praktyką jest inicjalizacja wszystkich pól klasy w metodzie init_

# * (bonus) zaimpelemntować rozgrywkę korzystając z kodu z zajęć 4

class PlanszaTicTacToe:
    def __init__(self, rozmiar):
        self.rozmiar = rozmiar
        self.plansza = [['.' for _ in range(rozmiar)] for _ in range(rozmiar)]

    def drukuj(self):
        for i in range(self.rozmiar):
            for j in range(self.rozmiar):
                print(self.plansza[i][j], end='')
                if j != self.plansza.__len__() - 1:
                    print(' | ', end='')
            if i != self.plansza.__len__() - 1:
                print('\n----------')
        print('\n')

    def wstaw(self, row, col):
        if 1 <= row <= self.rozmiar and 1 <= col <= self.rozmiar:
            self.plansza[row - 1][col - 1] = 'X'

    def jest_puste(self, x, y):
        if self.plansza[int(x) - 1][int(y) - 1] != ' ':
            return True
        else:
            return False


p = PlanszaTicTacToe(3)
p.drukuj()
p.wstaw(2, 3)
p.drukuj()


class GraTicTacToe:
    def __init__(self, rozmiar_planszy, znak):
        self.plansza = PlanszaTicTacToe(rozmiar_planszy)
        self.znak = znak

    def user_input(self, x, y):
        while True:
            s = input('Please insert row and column separated with space: ')
            s = s.replace(' ', '')
            if 1 <= int(s[0]) <= self.plansza.rozmiar and 1 <= int(s[1]) <= self.plansza.rozmiar:
                if not self.plansza.jest_puste(x, y):
                    print('This cell is already taken!')
                else:
                    return int(s[0]), int(s[1])
            else:
                print('Invalid arduments try again: ', end='')

    def if_full_row(self):
        for row in range(self.plansza.rozmiar):
            x = self.plansza[row][0]
            for col in range(1, self.plansza.rozmiar):
                if self.plansza[row][col] == x:
                    if col == self.plansza.rozmiar - 1:
                        return True, self.znak
                    x = self.plansza[row][col]
                else:
                    break

        return False, 0
    # def check_if_end(self):
    #     if self.if_full_row()[0]:
    #         print(self.if_full_row()[1], ' WINS!')
    #         return True
    #     elif if_full_col()[0]:
    #         print(if_full_col()[1], ' WINS!')
    #         return True
    #     elif if_full_cross()[0]:
    #         print(if_full_cross()[1], ' WINS!')
    #         return True
    #     return False
    # def play(self):


gra = GraTicTacToe(4, 'm')
print(gra.user_input(1, 1))
