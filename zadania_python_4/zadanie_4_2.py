
# funckja z zadania 3.5
def make_ruler(length):
    value = length
    
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

# funkcja z zadania 3.6
def make_grid(x, y):
    base = ["+---+", "|   |"]

    array_rows = 2*y+1
    result_holder = [""] * array_rows

    base_horizontal = 0

    for i in range(array_rows):
        for j in range(x):
            if j == 0:
                result_holder[i] += (base[base_horizontal])
            else:
                result_holder[i] += (base[base_horizontal])[1:]
 
        base_horizontal = (base_horizontal + 1)%2

    for i in range(array_rows):
        print(result_holder[i])


