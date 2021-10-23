line = input()
lista = line.split()

posortowane_slowa = sorted(lista, key=len)

print("najdłuższy wyraz: " + posortowane_slowa[-1] + "\n")
print("długość najdłuższego wyrazu: " + str(len(posortowane_slowa[-1])))
