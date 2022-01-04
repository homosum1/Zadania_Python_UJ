"""
Przygotować moduł Pythona z funkcjami tworzącymi listy liczb całkowitych 
do sortowania. Przydatne są m.in. następujące rodzaje danych: 
(a) różne liczby int od 0 do n-1 w kolejności losowej, 
(b) różne liczby int od 0 do n-1 prawie posortowane 
    (liczby są blisko swojej prawidłowej pozycji), 
(c) różne liczby int od 0 do n-1 prawie posortowane w odwrotnej kolejności, 
(d) n liczb float w kolejności losowej o rozkładzie gaussowskim, 
(e) n liczb int w kolejności losowej, o wartościach powtarzających się, 
    należących do zbioru k elementowego (k < n, np. k^2 = n).
"""

import random
from typing import Sequence
import numpy as np

class Generator:

    @staticmethod
    def random_numbers(n):
        sequence = []
        for i in range(n):
            sequence.append(random.randint(0, n))
        return sequence

    @staticmethod
    def almost_sorted_numbers(n, random_condition = 8):
        sequence = []    
        for i in range(n):
            if i%random_condition==0: 
                sequence.append(random.randint(0,n))
            else:
                sequence.append(i)
        return sequence

    @staticmethod
    def reversed_almost_sorted(n, random_condition = 8):
        sequence = Generator.almost_sorted_numbers(n, random_condition)
        return sequence.reverse()

    @staticmethod
    def gaussian_distribution(n, mu = 10.0, sigma = 2.0):
        old_sequence = np.random.randn(n) * sigma + mu
        sequence = [int(old_sequence) for old_sequence in old_sequence]
        return sequence

    @staticmethod
    def repeating_numbers(n):
        k = (int)(np.sqrt(n))
        container = []
        for i in range(k):
            container.append(i)

        sequence = []
        for i in range(n):
            index = random.randrange(k)
            sequence.append(container[index])

        return sequence



