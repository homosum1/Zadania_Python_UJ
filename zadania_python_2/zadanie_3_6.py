x = 9
y = 5

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
