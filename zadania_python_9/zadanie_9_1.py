class SingleList:
    class Node:
        def __init__(self, d = None, n = None):
            self.data = d
            self.next_element = n

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    
    # ... inne metody ...

    # Zwraca cały węzeł, skraca listę.
    # Dla pustej listy rzuca wyjątek ValueError.
    def remove_tail(self):
        if self.lenght == 0:
            raise ValueError
        else:
            return_value = None

            if self.length == 1:
                return_value = self.tail
                self.head = None
                self.tail = None
            else: 
                prev_tail = self.head

                while prev_tail.next_element != self.tail:
                    prev_tail = prev_tail.next_element
                
                return_value = self.tail
                tail = prev_tail

            self.length = self.length - 1
            return return_value


    # Węzły z listy other są przepinane do listy self na jej koniec.
    # Po zakończeniu operacji lista other ma być pusta.
    def join(self, other):
        self.lenght = self.length + other.length
        self.tail.next = other.head
        self.tail = other.tail

        #czyszczenie listy other
        other.lenght = 0
        other.head = None
        other.tail = None

    # czyszczenie listy
    def clear(self):  
        self.head = None
        self.tail = None
        self.length = 0


"""
POCZĄTEK JOIN
A1 <- self.head
|
A2 <- self.tail
|
None

B1 <- other.head
|
B2 <- other.tail
|
None

KONIEC JOIN
A1 <- self.head
|
A2
|
B1
|
B2 <- self.tail
|
None

None <- other.head=other.tail
"""