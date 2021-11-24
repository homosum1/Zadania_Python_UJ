from points import Point

"""Klasa reprezentująca prostokąt na płaszczyźnie."""
class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    # "[(x1, y1), (x2, y2)]"
    def __str__(self):        
        return "[" + str(self.pt1) + ", " + str(self.pt2) + "]"
    
    # "Rectangle(x1, y1, x2, y2)"
    def __repr__(self):       
        result = "Rectangle(" + str(self.x1) + ", " + str(self.y1) + ", " + str(self.x2) + ", " + str(self.y2) + ")" 
        return result

    # obsługa rect1 == rect2
    def __eq__(self, other):     
        if self.pt1 == other.pt1 and self.pt2 == other.pt2:
            return True
        else:
            return False

    # obsługa rect1 != rect2
    def __ne__(self, other):       
        return not self == other

    # zwraca środek prostokąta
    def center(self):         
        return Point(self.pt2.x/2 , self.pt1.y/2)          

    # pole powierzchni
    def area(self):
        return (self.pt1.length()) * (self.pt2.length())

    # przesunięcie o (x, y)
    def move(self, x, y):     
        self.pt1 = self.pt1  + Point(x,y)
        self.pt2 = self.pt2 + Point(x,y)




Rectangle(1, 1, 2, 2)


# Kod testujący moduł.
# Testuję wyłącznie funkcjonalności, które sam zdefiniowałem
import unittest

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(0,1,1,0)
        self.r2 = Rectangle(0,3,3,0)
        self.r3 = Rectangle(2,4,4,6)

    def test_to_str(self):
        self.assertEqual(str(self.r1), "[(0, 1), (1, 0)]")

    def test_is_equal(self):
        self.assertTrue(self.r1 == self.r1)
        self.assertFalse(self.r1 == self.r2)

    def test_is_different(self):
        self.assertTrue(self.r1 != self.r2)
        self.assertFalse(self.r1 != self.r1)

    def test_rectangle_center(self):
        self.assertEqual(self.r1.center(), Point(0.5,0.5))
        self.assertEqual(self.r2.center(), Point(1.5,1.5))

    def test_rectangle_move(self):
        self.r1.move(1,1)
        self.r2.move(4,4)
        self.assertEqual(self.r1, Rectangle(1,2,2,1))
        self.assertEqual(self.r2, Rectangle(4,7,7,4))

    def test_rectangle_area(self):
        self.assertEqual(self.r1.area(), 1)
        self.assertEqual(self.r2.area(), 9)


if __name__ == '__main__':
        unittest.main()     # uruchamia wszystkie testy
