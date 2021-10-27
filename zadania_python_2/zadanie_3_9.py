
nestedList = [[3,4,1], [0, 3, 4, 5, 6], [1, 1, 1, 1], [3, 5, 4]]

columns = len(nestedList)
myList = []


for list in nestedList:
    sum = 0
    for j in list:      
        sum+= j

    myList.append(sum)


print("po dodaniu: ")
print(*myList)
