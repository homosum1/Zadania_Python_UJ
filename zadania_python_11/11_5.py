"""
Sortowanie przez zliczanie / CountingSort

etapy sortowania:

1. znajdujemy największy element sortowanej list (zapisujemy go jako max )

2. Inicjalizujemy listę elements_cnt o długości max + 1 zerami. 
   Lista ta wykorzystywana jest do przechowywania ilości wystąpień elementów 
   o danej wartości w następujący sposób: 
   
   list[13] ++    ->  oznacza zliczenie wystąpienia elementu o wartości 13

3. Zliczamy ilość wystąpień każdej wartości przechowywanej w liśce do posortowania. 
   Ilości wystąpień umieszczamy w liście elements_cnt.

4. Sumujemy ilość wystąpień wartości o danej wielkości 
   z ilością wartości wszystkich mniejszych od niej elementów np:

   było:
	
   a[0] =  1    a[1]  = 0     a[2]   =   3    a[3]   =   1

   będzie:

   a[0] =  1    a[1]  = 1     a[2]   =   4    a[3]   =   5


    W wyniku tej operacji dostajemy informację o tym ile elementów poprzedza element 
    którego wartość reprezentowana jest przez indeks listy.

    Przechodzimy przez sortowaną listę array pobierając z niej wartości, 
    na podstawie tych wartości odszukujemy ilość elementów, 
    które znajdują się przed nią (informacja ta znajduje się w naszej liście 
    elements_cnt). Na podstawie ilości elementów poprzedzających tą 
    wartość jesteśmy w stanie oszacować na jakim indeksie w sekwencji wynikowej
    umieścić sortowaną wartość.
"""

def sort(data):
    size = len(data)

    result = []
    elements_cnt = []

    max = data[0]

    #znalezienie największego elementu list data + wypełnienie listy wyników
    result.append(0)
    for i in range(1,size):
        result.append(0)

        if data[i] > max:
            max = data[i]

    # inicjalizacja listy elements_cnt zerami
    for i in range(0,max+1):
        elements_cnt.append(0)

    # przechowywanie ilości wystąpień każdego elementu
    for i in range(size):
        elements_cnt[data[i]] += 1
        
    # przechowywanie sumy wartości z tablicy elements_cnt
    for i in range(1, max+1):
        elements_cnt[i] += elements_cnt[i -1]

    # wyszukanie indeksu elementu listy w tablicy elements_cnt, i wstawienie
    # elementów do wynikowej listy
    for i in reversed(range(size)):
        #print("i: " + str(i) + "  data[i]: " + str(data[i]) + " elements_cnt[]:" + str(elements_cnt[data[i]] - 1))
        result[elements_cnt[data[i]] - 1] = data[i]
        elements_cnt[data[i]] -= 1
  
    # przekopiowanie wyników do zadanego wektora
    return result


lst = [9,8,7,6,5,4,3,2,1]
print(sort(lst))