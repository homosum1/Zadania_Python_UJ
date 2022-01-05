

class Queue:
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

    def size(self):
        return self.queued_elements
    
    def empty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def print(self):
        print(self.array)
        print("tail: " + str(self.tail) + " head: " + str(self.head))
        

    def put(self, element):
        if self.queued_elements < self.queue_size:
            self.array[self.tail] = element
            
            self.queued_elements += 1

           
            self.tail = (self.tail+1) % self.queue_size
            
            #print("actual tail: " + str(self.tail))
        else:
            raise self.FullQueue()

    def get(self):
        if self.queued_elements > 0:
            temp = self.array[self.head]
            self.array[self.head] = None

            self.head = (self.head+1) % self.queue_size
            self.queued_elements -= 1
            return temp
        else:
            raise self.EmptyQueue()


import unittest

class TestStack(unittest.TestCase):
    
    def test_put(self):
        q1 = Queue(10)
        q1.put(5)
        self.assertEqual(q1.size(), 1)
        self.assertEqual(q1.get(), 5)

        for i in range(5):
            q1.put(i)

        self.assertEqual(q1.size(), 5)

        for i in range(4):
            q1.put(i)

        self.assertEqual(q1.size(), 9)

        q1.get()
        q1.get()

        for i in range(3):
            q1.put(i)

        self.assertEqual(q1.size(), 10)


    def test_get(self):
        q2 = Queue(5)

        for i in range(5):
            q2.put(i)

        q2.print()

        self.assertEqual(q2.get(), 0)
        self.assertEqual(q2.get(), 1)
        self.assertEqual(q2.get(), 2)
        
        q2.print()

        for i in range(15,18):
            q2.put(i)

        q2.print()
        self.assertEqual(q2.size(), 5)

        q2.get()
        self.assertEqual(q2.get(), 4)
        
    def test_exception_rise(self):
        q3 = Queue(1)
        # self.assertRaises(Queue.EmptyQueue, q3.get())
       

if __name__ == '__main__':
    unittest.main()