from math import gcd
from math import lcm

# Jeśli dobrze pamiętam w zadaniu nie należało korzystać z klas


# frac1 + frac2
def add_frac(frac1, frac2):
    NWW = lcm(frac1[1], frac2[1])

    a = NWW / frac1[1]
    b = NWW / frac2[1]
    
    # sprowadzan do wspólnego mianownika
    for i in range(len(frac1)):
        frac1[i] *= a
        frac2[i] *= b
 
    #dodaję
    result = [frac1[0] + frac2[0], frac1[1]]

    #upraszczam ułamek
    NWD = gcd(int(result[0]), int(result[1]))
    for i in range(len(result)):
        result[i] /= NWD

    return result


# frac1 - frac2
def sub_frac(frac1, frac2):
    NWW = lcm(frac1[1], frac2[1])

    a = NWW / frac1[1]
    b = NWW / frac2[1]
    
    # sprowadzan do wspólnego mianownika
    for i in range(len(frac1)):
        frac1[i] *= a
        frac2[i] *= b
 
    # odejmuję
    result = [frac1[0] - frac2[0], frac1[1]]

    #upraszczam ułamek
    NWD = gcd( int(result[0]), int(result[1]))
    for i in range(len(result)):
        result[i] /= NWD

    return result




# frac1 * frac2
def mul_frac(frac1, frac2):
    result = [frac1[0] * frac2[0], frac1[1] * frac2[1]]

    #upraszczam ułamek
    NWD = gcd(result[0], result[1])
    for i in range(len(result)):
        result[i] /= NWD

    return result



# frac1 / frac2
def div_frac(frac1, frac2):
    buf = frac2[0]
    frac2[0] = frac2[1]
    frac2[1] = buf
    
    return mul_frac(frac1, frac2)



# bool, czy dodatni
def is_positive(frac):
    if frac[0] >= 0 and frac[1] >= 0:
        return True
    else:
        return False

    

# bool, typu [0, x]
def is_zero(frac):
    if frac[0] == 0:
        return True
    else:
        return False



# -1 | 0 | +1
def cmp_frac(frac1, frac2):
    #upraszczam ułamek
    NWD1 = gcd(frac1[0], frac1[1])
    NWD2 = gcd(frac2[0], frac2[1])
    
    for i in range(len(frac1)):
        frac1[i] /= NWD1
        frac2[i] /= NWD2


    if frac1[0] == frac2[0] and frac1[1] == frac2[1]:
        return True
    else:
        return False

    

# konwersja do float
def frac2float(frac):
    return float(frac[0]/frac[1])


import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.f1 = [-1, 2]
        self.f2 = [0, 1]
        self.f3 = [3, 1]
        self.f4 = [6, 2]
        self.f5 = [0, 2]
        self.f6 = [3,7]
        self.f7 = [6,5]

        

    def test_add_frac(self):
        self.assertEqual(add_frac(self.f1, self.f2), [-1, 2])

    def test_sub_frac(self):
        self.assertEqual(sub_frac(self.f3, self.f7), [9,5])

    def test_mul_frac(self):
         self.assertEqual(mul_frac(self.f6, self.f7), [18,35])

    def test_div_frac(self):
         self.assertEqual(div_frac(self.f4, self.f3), [1,1])

    def test_is_positive(self):
        self.assertFalse(is_positive(self.f1))

    def test_is_zero(self): 
        self.assertTrue(is_zero(self.f2))

    def test_cmp_frac(self):
        self.assertTrue(cmp_frac(self.f3, self.f4))

    def test_frac2float(self):
        self.assertEqual(frac2float(self.f4), 3.0)

    
if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy


