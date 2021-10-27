val = True

# zadanie dla zmiennych int, z wykorzystaniem funkcji isnumeric()

#while(val):
#   x = input()
#   if( x.isnumeric() ):
#       power = pow(int(x), 3)
#       print(str(x) + " " + str(power) +"\n")
#   else:
#       if(x == "STOP"):
#           print("zakońcozno działanie programu\n")
#           break
#       else:
#           print("wprowadzono nieprawidłowe dane")        

while(val):
    x = input()
    try:
        value = float(x)
    except ValueError:
        if(x == "STOP"):
           print("zakońcozno działanie programu\n")
           break;
        else:
           print("wprowadzono nieprawidłowe dane") 
    else:
        power = pow(value, 3)
        print(str(x) + " " + str(power) +"\n")
