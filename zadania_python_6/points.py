import math as m

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    # zwraca string "(x, y)"
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    # zwraca string "Point(x, y)"
    def __repr__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

    # obsługa point1 == point2
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
            
    # obsługa point1 != point2
    def __ne__(self, other):      
        return not self == other



    # Punkty jako wektory 2D.
    
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y )

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y )
    
    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y


    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):  # długość wektora
        return m.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points



# Kod testujący moduł.
# Testuję wyłącznie funkcjonalności, które sam zdefiniowałem
import unittest

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(1,1)
        self.p2 = Point(3,3)
        self.p3 = Point(4,2)
        self.p4 = Point(5,5)

    def test_to_str(self):
        self.assertEqual(str(self.p1), "(1, 1)")

    def test_add_frac(self):
        self.assertEqual(self.p1 + self.p2, Point(4,4))
        self.assertEqual(self.p3 + self.p3, Point(8,4))

    def test_is_equal(self):
        self.assertTrue(self.p1 == self.p1)
        self.assertFalse(self.p1 == self.p2)

    def test_is_different(self):
        self.assertTrue(self.p1 != self.p2)
        self.assertFalse(self.p1 != self.p1)

    def test_vector_add(self):
        self.assertEqual(self.p1 + self.p2, self.p2 + self.p1)
        self.assertEqual(self.p1 + self.p3, Point(5,3))

    def test_vector_sub(self):
        self.assertEqual(self.p2 - self.p1, Point(2,2))
        self.assertEqual(self.p4 - self.p3, Point(1,3))

    def test_vector_mul(self):
        self.assertEqual(self.p2 * self.p1, self.p1 * self.p2)
        self.assertEqual(self.p1 * self.p2, 6)

    def test_vector_lenght(self):
        self.assertEqual(self.p1.length(), m.sqrt(2))

if __name__ == '__main__':
        unittest.main()     # uruchamia wszystkie testy
    
