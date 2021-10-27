
napis_wielowierszowy = "Oto napis wielowierszowy z elementami\nw różnych liniach oddzielonych spacjami i znakami nowej linii"

napis_wielowierszowy.replace('\\', '')

lista_elementow = napis_wielowierszowy.split()
liczba_wyrazow = len(lista_elementow)
print("napis ma : " + str(liczba_wyrazow) + " wyrazow\n")
