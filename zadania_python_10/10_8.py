from random import randrange
from types import resolve_bases
from typing import List


class RandomQueue:
    class EmptyQueue(Exception):
        def __init__(self, mess="Queue is empty!"):
            self.message = mess
            super().__init__(self.message)
        
    class FullQueue(Exception):
        def __init__(self, mess="Queue is full!"):
            self.message = mess
            super().__init__(self.message)
    

    def __init__(self, s):
        self.queue_size = s
        self.array = self.queue_size * [None]
        self.queued_elements = 0

        self.head = 0
        self.tail = 0
        self.backup_tail = 0


    def insert(self, element):
        if self.queued_elements < self.queue_size:
            if self.array[self.tail] != None:
                self.tail += 1

            self.array[self.tail] = element
            self.queued_elements += 1
    
            self.backup_tail = self.tail
            self.tail = (self.tail+1) % self.queue_size

        else:
            raise self.FullQueue()

    def remove(self):
        if self.queued_elements > 0:
            
            index = randrange(self.queued_elements)
            index = index+self.head
          
            temp = self.array[index]
            
            if self.tail == self.head:
                self.tail = self.backup_tail

            self.array[index] = self.array[self.tail]
            self.array[self.tail] = None
            
            self.tail = (self.tail-1) % self.queue_size
            self.queued_elements -= 1

            #print("head: " + str(self.head) + " tail: " + str(self.tail) + " backup tail: " + str(self.backup_tail) + " queued elements: " + str(self.queued_elements))

            return temp
        else:
            raise self.EmptyQueue()


    def is_empty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def is_full(self):
        if self.queued_elements == self.queue_size:
            return True
        else:
            return False

    def clear(self):
        self.queued_elements = 0
        self.tail = 0

    def size(self):
        return self.queued_elements
    
    def print(self):
        print("\nvalues:")
        print(self.array)


import unittest

class TestStack(unittest.TestCase):
    
    def test_insert(self):
        rq1 = RandomQueue(10)

        rq1.insert(10)
        self.assertEqual(rq1.size(), 1)

        for i in range (9):
            rq1.insert(i)
        
        self.assertEqual(rq1.size(), 10)
    
    def test_remove(self):
        rq2 = RandomQueue(5)
        
        for i in range (5):
            rq2.insert(i)
        
        rq2.print()
        print("removed: " + str(rq2.remove()))
        self.assertEqual(rq2.size(), 4)
        rq2.print()
        print("removed: " + str(rq2.remove()))
        self.assertEqual(rq2.size(), 3)
        rq2.print()
        rq2.insert(30)
        rq2.print()
        rq2.insert(50)
        rq2.print()
        results = []
        for i in range(4):
            results.append(rq2.remove())

        self.assertEqual(len(results), 4)

    def test_is_empty_full(self):
        rq3 = RandomQueue(3)
        rq3.insert(1)
        rq3.print()
        rq3.remove()
        self.assertTrue(rq3.is_empty())
        self.assertFalse(rq3.is_full())


if __name__ == '__main__':
    unittest.main()