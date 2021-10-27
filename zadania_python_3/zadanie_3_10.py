dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman2int(roman_number):
    length = len(roman_number);
    result  = 0
    # dzięki funkcji enumarate możemy przejść po kolejnych elementach zadanej liczby rzymskiej
    for (index, roman) in enumerate(roman_number):
        print(str(index) + " " + str(roman))
        # sprawdzan czy podczas konwersji należy dodać czy odjąć liczby 
        if (index < length - 1) and (dictionary[roman] < dictionary[roman_number[index+1]]):
            result = result - dictionary[roman]
        else:
            result = result + dictionary[roman]
    return result


inputted_value = input("Wprowadź liczbę rzymską: ")
print("liczba " + inputted_value + " w zapisie arabskim to: " + str(roman2int(inputted_value)));

