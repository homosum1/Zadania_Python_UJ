line = input()

my_list = line.split()

sorted_by_lenght = sorted(my_list, key=len)
sorted_by_alphabet = sorted(my_list)

print("posortowane wzgledem dlugosci: ")
print(*sorted_by_lenght)
print("posortowane alfabetycznie: ")
print(*sorted_by_alphabet)
