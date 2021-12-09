
""""
P(0, 0) = 0.5,
P(i, 0) = 0.0 dla i > 0,
P(0, j) = 1.0 dla j > 0,
P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.
"""


def iterative_version_P(i, j):
    iterations = i
    if j > i:
        iterations = j

    # słownik Dict
    Dict = {}

    # dodanie przypadku 1
    Dict[(0, 0)] = 0.5

    # dodanie przypadków 2 i 3 
    for x in range(1, iterations + 1):
        Dict[(x, 0)] = 0
        Dict[(0, x)] = 1

    # iteracyjne obliczenie przypadku czwartego
    for x in range(0, iterations):
        for y in range(0, iterations):
            P_val = 0.5 * (Dict[(x, y + 1)] + Dict[(x + 1, y)])
            Dict[(x+1, y+1)] = P_val

    # zwracam konkretną obliczoną wartość
    return Dict[(i,j)]


def recursive_version_P(i, j):
    if i == 0 and j == 0:
        return 0.5
    if i > 0 and j == 0:
        return 0.0
    if i == 0 and j > 0:
        return 1.0

    if i > 0 and j > 0:
        return 0.5 * (recursive_version_P(i-1, j) + recursive_version_P(i, j-1))



import unittest


class Comparer(unittest.TestCase):
    def test_equal(self):

        self.assertEqual(iterative_version_P(4, 0), recursive_version_P(4,0))
        self.assertEqual(iterative_version_P(0, 6), recursive_version_P(0,6))
        self.assertEqual(iterative_version_P(0, 0), recursive_version_P(0,0))        
        self.assertEqual(iterative_version_P(4, 3), recursive_version_P(4,3))

        

if __name__ == '__main__':
    unittest.main()