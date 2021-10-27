class Time:

    def __init__(self, seconds=0):
        self.s = seconds

    def __str__(self):
        return "{} sec".format(self.s)

    def __repr__(self):
        return "Time({})".format(self.s)

time1 = Time(12)
time2 = Time(3456)
print(time1, time2)            # Python wywołuje str(), Python 2
print([time1, time2])          # Python wywołuje repr(), Python 2


# po wykmentowaniu definicji __str__ (zapewniającej ładny wygląd wypisanych danych)
# zmieni się wynik wywołania pierwszej funkcji print(), zamiast wyedytowanej
# odpowiednio do wypisywanego typu danych linii: 12 sec 3456 sec, otrzymamy
# Time(12) Time(3456)

# wykomentowanie elementu __repr__ (służącego do reprezentacji obiektu podczas wypisywania) spowoduje natomiast
#  wypisanie obiektu w nieczytelnej formie odwołującej się do miejsc w pamięci:
# [<__main__.Time object at 0x104d1bd60>, <__main__.Time object at 0x104d1bd00>]
