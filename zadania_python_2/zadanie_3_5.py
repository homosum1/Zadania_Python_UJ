value = input("podaj długość linijki: ")

base_lenght = 4;

rurel = "|"
measure = ""

for i in range(int(value)+1):
    distance = "." * len(str(i)) + "."
    base_sequence = distance + "|"
    if i != int(value):
        rurel += base_sequence
    measure += (str(i)+ "  ")


print(rurel)
print(measure)
