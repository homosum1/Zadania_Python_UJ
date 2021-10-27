# śrendik jest tutaj użyty poprawnie do rozdzielenia poleceń
L = [3, 5, 4] ; L = L.sort()

# mamy tutaj nadmiarową wartość 3, gdyby dać x, y = 1, 2 to x miałoby wartość
# 1 a y miałoby wartość 2
x, y = 1, 2, 3

# w pythonie inicjalizacja talibcy wymaga użycia nawiasów
# zamiast X = 1, 2, 3 piszemy X = [1, 2, 3]
X = 1, 2, 3
X[1] = 4

X = [1, 2, 3]
# wychodzimy poza zakres tablicy X odwołując się do jej 4 elemtnu
X[3] = 4

X = "abc" ; X.append("d")

L = list(map(pow, range(8)))
