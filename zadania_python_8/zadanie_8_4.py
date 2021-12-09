import math

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    
    P = ( math.sqrt((a+b+c)(a+b-c)(a-b+c)(-a+b+c)) ) /4

    # gdy odcinki o podanych długościach nie tworzą trójkąta, ani nie lezą w jednej prostej, wtedy
    # a + b < c, zatem p - c < 0 więc nasze P nalezy do liczb zespolonych.

    if isinstance(P, complex):
        raise ValueError
    else:
        return P

    