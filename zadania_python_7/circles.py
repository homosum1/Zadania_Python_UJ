from points import Point
import math

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    # "Circle(x, y, radius)"
    def __repr__(self):    
        return "Circle(" + str(self.pt.x)  + ", " + str(self.pt.y) + ", " + str(self.radius) + ")"
    
    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    # pole powierzchni
    def area(self):
        return math.pi*pow(self.radius,2)

    # przesuniecie o (x, y)
    def move(self, x, y):
        pt = self.pt + Point(x,y)
        return Circle(pt.x, pt.y, self.radius)

    # najmniejszy okrąg pokrywający oba
    def cover(self, other):
        #chyba tak się to robi?
        x_val = abs(self.pt.x - other.pt.x)/2
        y_val = abs(self.pt.y - other.pt.y)/2

        rad_sum = self.radius + other.radius
        a = pow((self.pt.x - other.pt.x), 2)
        b = pow((self.pt.y - other.pt.y), 2)
        radius = math.sqrt(rad_sum + a + b)/2

        return Circle(x_val,y_val, radius)
        
# Kod testujący moduł.

import unittest

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c1 = Circle(2, 2, 4)
        self.c2 = Circle(1, 1, 3)
        self.c3 = Circle(0, 1, 2)
        self.c4 = Circle(0, 0, 3)


    def test_init(self):
        catched = False
        try:
            x = Circle(3,4, -5)
        except ValueError:
            catched = True

        self.assertTrue(catched)

            
        
    def test_repr(self):
        self.assertEqual(repr(self.c1), "Circle(2, 2, 4)")
        self.assertEqual(repr(self.c3), "Circle(0, 1, 2)")

    def test_equal(self):
        self.assertTrue(self.c3 == Circle(0, 1, 2))

    def test_not_equal(self):
        self.assertTrue(self.c1 != self.c2)

    def test_move(self):
        self.assertEqual(self.c1.move(1,1), Circle(3, 3, 4))

    def test_area(self):
        self.assertEqual(self.c4.area(), 9*math.pi)

    def test_cover(self):
        result = self.c3.cover(self.c4)
       
        expected = Circle(0,0.5,1.22)
        self.assertAlmostEqual(result.pt.x, expected.pt.x)
        self.assertAlmostEqual(result.pt.y, expected.pt.y)
        self.assertAlmostEqual(result.radius, result.radius)
        

if __name__ == '__main__':
    unittest.main()
