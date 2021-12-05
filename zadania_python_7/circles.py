from points import Point
import math
import copy

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

         # okręgi sobie równe
        if self == other:
            return Circle(self.pt.x, self.pt.y, self.radius)
        else:
            r1 = copy.copy(self)
            r2 = copy.copy(other)
            # upewniam się, ze r1 będzie większym okręgiem
            if r1.radius < r2.radius:
                buf = r1
                r1 = r2
                r2 = buf
            
            distance = math.sqrt((r1.pt.x - r2.pt.x)**2 + (r1.pt.y - r2.pt.y)**2)
            radius_dif = abs(r1.radius - r2.radius)

            if distance < radius_dif:
                return r1
            elif (distance + r1.radius) > r2.radius:
                rad = (distance + r1.radius + r2.radius)/2
                cor = 1/2 + (r2.radius - r1.radius)/(2*distance)
            
                final_x = (1-cor)*r1.pt.x + cor*r2.pt.x
                final_y = (1-cor)*r1.pt.y + cor*r2.pt.y

                return Circle(final_x, final_y, rad)
                
  
      
# Kod testujący moduł.

import unittest

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c1 = Circle(2, 2, 4)
        self.c2 = Circle(1, 1, 3)
        self.c3 = Circle(0, 1, 2)
        self.c4 = Circle(0, 0, 3)
        self.c5 = Circle(5, 3, 1)
        self.c6 = Circle(5, 6, 2)
        self.c7 = Circle(1, 4, 1)
        self.c8 = Circle(3, 4, 1)
        self.c9 = Circle(3, 2, 1)
        self.c10 = Circle(3, 6, 1)

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
        self.assertEqual(self.c5.cover(self.c6), Circle(5, 5, 3))
        self.assertEqual(self.c7.cover(self.c8), Circle(2, 4, 2))
        self.assertEqual(self.c9.cover(self.c10), Circle(3, 4, 3))


if __name__ == '__main__':
    unittest.main()
