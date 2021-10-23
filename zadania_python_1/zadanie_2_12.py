linia = input()

print("wczytana linia: " + linia + "\n")

lista = linia.split()

pierwsze_znaki = ""
for i in lista:
    pierwsze_znaki += i[0]


print("napis z pierwszych znaków: " + pierwsze_znaki + "\n")

ostatnie_znaki = ""
for i in lista:
    ostatnie_znaki += i[len(i)-1]

print("napis z ostatnich znaków: " + ostatnie_znaki + "\n")
