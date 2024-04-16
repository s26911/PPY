# Zad01
# Napisać funkcję, która drukuje planszę w sposób estetyczny, np. tak jak poniżej
import random

my_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def print_board(board=my_board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end='')
            if j != 2:
                print(' | ', end='')
        if i != 2:
            print('\n----------')
    print('\n')


print_board()


# Zad02
# Napisać funkcję, która w pole o *jakiś* współrzędnych wstawia *jakiś* znak

def insert(row, col, board=my_board):
    if 1 <= row <= 3 and 1 <= col <= 3:
        board[row - 1][col - 1] = 'X'


insert(1, 1)
insert(2, 2)
insert(3, 3)
print_board()


# Zad03
# Napisać funkcję, która wczytuje od użytkownika i zwraca wspórzędne ruchu
# (wczytywać tak długo, aż poda prawidłowe pole - w zakresie planszy i puste)
def user_input(board=my_board):
    while True:
        s = input('Please insert row and column separated with space: ')
        s = s.replace(' ', '')
        if 1 <= int(s[0]) <= 3 and 1 <= int(s[1]) <= 3:
            if my_board[int(s[0]) - 1][int(s[1]) - 1] != ' ':
                print('This cell is already taken!')
            else:
                return int(s[0]), int(s[1])
        else:
            print('Invalid arduments try again: ', end='')


user_input()


# Zad04
# Napisać funkcję, która sprawdza, czy któryś wiersz zawiera tylko *jakiś* znak.
# Funkcja zwraca wartość logiczną.
def if_full_row(board=my_board):
    for row in range(3):
        if board[row][0] != ' ' and board[row][0] == board[row][1] \
                and board[row][1] == board[row][2]:
            return True, board[row][0]
    return False, 0


print(if_full_row())


# Zad05
# Napisać funkcję, która sprawdza, czy któraś kolumna zawiera tylko *jakiś* znak.
# Funkcja zwraca wartość logiczną.
def if_full_col(board=my_board):
    for col in range(3):
        if board[0][col] != ' ' and board[0][col] == board[1][col] \
                and board[1][col] == board[2][col]:
            return True, board[0][col]
    return False, 0


print(if_full_col())


# Zad06
# Napisać funkcję, która sprawdza, czy któraś przekątną zawiera tylko jakiś znak.
# Funkcja zwraca wartość logiczną.
def if_full_cross(board=my_board):
    if board[0][0] != ' ' and ((board[0][0] == board[1][1] and board[1][1] == board[2][2]) or
                               (board[0][2] == board[1][1] and board[1][1] == board[2][0])):
        return True, board[1][1]
    return False, 0


print(if_full_cross())


# Zad07
# Napisać funkcję, która zwraca losowy (ale zgodny z zasadami gry ruch)
def computer_move(board=my_board):
    while True:
        row = random.randint(1, 3)
        col = random.randint(1, 3)
        if board[row - 1][col - 1] == ' ':
            insert(row-1, col-1, 'O')
            return


# Zad08
# Napisać funkcję, która sprawdza, czy gra się skończyła.
# Funkcja zwraca wartość logiczną oraz wynik rozgrywki.
def check_if_end(board=my_board):
    if if_full_row()[0]:
        print(if_full_row()[1], ' WINS!')
        return True
    elif if_full_col()[0]:
        print(if_full_col()[1], ' WINS!')
        return True
    elif if_full_cross()[0]:
        print(if_full_cross()[1], ' WINS!')
        return True
    return False


def play(board=my_board):
    while not check_if_end():
        print_board()
        uin = user_input()
        insert(uin[0], uin[1])
        computer_move()

# play()