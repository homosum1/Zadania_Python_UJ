from math import gcd
from math import lcm


class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError
        self.x = x
        self.y = y

    # zwraca "x/y" lub "x" dla y=1
    def __str__(self):
        if self.y == 1:
            return str(self.x)
        else:
            return str(self.x) + "/" + str(self.y)

    # zwraca "Frac(x, y)"
    def __repr__(self):
        return "Frac(" + str(self.x) + ", " + str(self.y)  + ")"
    
    def __eq__(self, other):   
        NWD1 = gcd(int(self.x), int(self.y))
        NWD2 = gcd(int(other.x), int(other.y))
    
        x1 = self.x / NWD1
        y1 = self.y / NWD1
        x2 = other.x / NWD2
        y2 = other.y / NWD2

        if x1 == x2 and y1 == y2:
            return True
        else:
            return False

        

    def __ne__(self, other):
        return (self != other)

    def __lt__(self, other):
        if self.x/self.y < other.x/other.y:
            return True
        else:
            return False
        
    def __le__(self, other):
        if self.x/self.y <= other.x/other.y:
            return True
        else:
            return False
        

    def simplify(self):
        NWD = gcd(int(self.x), int(self.y))
        x = self.x / NWD
        y = self.y / NWD
        return Frac(x,y)

    def same_denominator(self, other):
        NWW = lcm(self.y, other.y)

        a = NWW / self.y
        b = NWW / other.y

        new_self = Frac(self.x, self.y)
        new_other =  Frac(other.x, other.y)

        new_self.x *= a
        new_self.y *= a
        new_other.x *= b
        new_other.y *= b
        
        return [new_self, new_other]


    # frac1+frac2, frac+int
    def __add__(self, other):
        if type(other) is int:
            result = Frac(self.x + self.y*other, self.y)
            return result.simplify()
        else:
            el = self.same_denominator(other)
            result = Frac(el[0].x + el[1].x, el[0].y)
            return result.simplify()
 

        
    # int+frac
    __radd__ = __add__             


     # frac1-frac2, frac-int
    def __sub__(self, other):
        if type(other) is int:
            result = Frac(self.x - self.y*other, self.y)
            return result.simplify()
        else:
            el = self.same_denominator(other)
            result = Frac(el[0].x - el[1].x, el[0].y)
            return result.simplify()

        
    # int-frac
    def __rsub__(self, other):      
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

     # frac1*frac2, frac*int
    def __mul__(self, other):
        if type(other) is int:
            result = Frac(self.x*other, self.y)
            return result.simplify()
        else:
            result = Frac(self.x*other.x, self.y*other.y)
            return result.simplify()

    # int*frac
    __rmul__ = __mul__             

    # frac1/frac2, frac/int, Py3
    def __truediv__(self, other): 
        if type(other) is int:
            result = Frac(self.x, self.y*other)
            return result.simplify()
        elif type(other) is Frac:
            inverted = Frac(self.x * other.y, self.y * other.x)
            return inverted.simplify()


    # int/frac, Py3
    def __rtruediv__(self, other):  
        result = Frac(self*other.y, other.x)
        return result.simplify()


    # operatory jednoargumentowe
    
    # +frac = (+1)*frac
    def __pos__(self):  
        return self
    
    # -frac = (-1)*frac
    def __neg__(self):
        return Frac(self.x * (-1), self.y)

    # odwrotnosc: ~frac
    def __invert__(self):
        return Frac(self.y, self.x)

    # float(frac)
    def __float__(self): 
        return self.x/self.y

     # immutable fracs
    def __hash__(self):
        return hash(float(self))  
        # assert set([2]) == set([2.0])


# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase):
    def setUp(self):
        self.f1 = Frac(1,1)
        self.f2 = Frac(2,4)
        self.f3 = Frac(3,7)

    def test_str(self):
        self.assertEqual(str(self.f3), "3/7")

    def test_repr(self):
        self.assertEqual(repr(self.f1), "Frac(1, 1)")

    def test_add_frac(self):
        self.assertEqual(self.f1 + self.f2, Frac(3,2))
        self.assertEqual(self.f3 + 1, Frac(10,7))

    def test_sub_frac(self):
        self.assertEqual(self.f1 - self.f2, Frac(1,2))
        self.assertEqual(self.f3 - 1, Frac(-4,7))

    def test_mul_frac(self):
        self.assertEqual(self.f3 * self.f2, Frac(3, 14))

    def test_div_frac(self):
        self.assertEqual(self.f1 / self.f3, Frac(7,3))

    def test_equal(self):
        self.assertTrue(self.f1 == Frac(1,1))

    def test_inverse(self):
        self.assertEqual(~self.f3, Frac(7,3))

    def test_neg(self):
        self.assertEqual(-self.f1, Frac(-1, 1))

    def test_float(self):
        self.assertEqual(float(self.f1), 1)

    def test_exception(self):
        with self.assertRaises(ValueError):
            Frac(1,0)
    

if __name__ == '__main__':
    unittest.main()
