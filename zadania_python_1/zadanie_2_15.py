
lista = [1 , 21, 32, 43, 66, 89, 91, 101, 54, 234, 193, 201, 4, 34]

result = ""
for i in lista:
    result+= str(i)
    
print(*lista)
print("ciąg liczb z listy: " + result)
