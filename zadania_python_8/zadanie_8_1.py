import math

def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""

    if a == 0 and b == 0:
        if c != 0:
            return "równanie speczne\n"
        else:
            return "równanie nieoznaczone\n"

    delta = (b**2) - (4*a*c)
    if delta >= 0:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)

        if delta > 0:
            return "rozwiązania równania to: x1 = " + str(x1) + " i x2 = " + str(x2) + "\n"
        else:
            return "rozwiązanie równania to: x = " + str(x1) + "\n"
    else:
        return "równanie nie ma rozwiązań\n"


