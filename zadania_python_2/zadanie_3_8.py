sekwencja_A = [1, 5, 4, 3, 3 ,7 , 9]
sekwencja_B = [3, 1, 2, 2, 8]

outputSequence1 = sekwencja_A + sekwencja_B
outputSequence1 = list(dict.fromkeys(outputSequence1))

print("lista b): ")
print(*outputSequence1)

outputSequence2 = list(set(sekwencja_A) & set(sekwencja_B))
outputSequence2 = list(dict.fromkeys(outputSequence2))

print("lista a): ")
print(*outputSequence2)
