line = input()
list = line.split()
dlugosc_wyrazow = 0
for i in list:
    print("i = " + i)
    print("i length = " + str(len(i)) + "\n")
    dlugosc_wyrazow += len(i)

print("łączna długość wyrazów: " + str(dlugosc_wyrazow) + "\n")
