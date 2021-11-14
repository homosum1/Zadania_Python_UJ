# zakładam poprawność danych wejściowych, to znaczy left i right nie wychodzą poza zakres listy oraz left < right

def iterative_reverse(L, left, right):    
    iteration_range = (right - left) // 2
    if left == 0:
        iteration_range += 1
    
    for i in range(iteration_range):
        buf2 = L[left]
        L[left] = L[right]
        L[right] = buf2

        left += 1
        right -= 1

def recursive_reverse(L, left, right):
    buf = L[left]
    L[left] = L[right]
    L[right] = buf

    if left < right:
        return recursive_reverse(L, left + 1, right - 1)
    else:
        return


print("\niterative example: (0 - 5)")

L = [0,1,2,3,4,5]
print(L)
iterative_reverse(L, 0, 5)
print(L)

print("\nexample 2: (0 - 4)")

K = [0,1,2,3,4,5]
print(K)
iterative_reverse(K, 0, 4)
print(K)


print("\nrecursive example: (1 - 5)\n")

W = [0,1,2,3,4,5]
print(W)
recursive_reverse(W, 1, 5)
print(W)
