def Fahreheit(Enter_Celsius_temperature):
    return (Enter_Celsius_temperature)*5/9+32

def Celsius(Enter_Fahrenheit_temperature):
    return ((Enter_Fahrenheit_temperature)-32)*9/51

while True:

    a=(input("Enter a action:"))
    if a.isdigit():
        O = int(a)
        if O==1:
            while True:
                Cel=(input("Enter Celsius temperature:"))
                if Cel.isdigit(): 
                    C = (Fahreheit(int(Cel)))
                    print ("Fahreheit:"+str(int(C)))
                    break
                else:
                    print("Error, please enter numeric input")   
        if O==2:
            while True:
                Fah=(input("Enter Fahrenheit temperature:"))
                if Fah.isdigit():
                    F = Celsius(int(Fah))
                    print ("Celsius:"+str(int(F)))
                    break
                else:
                    print("Error, please enter numeric input")
                    
        if O==3:
            print("Exit")
            break
     else:
        print("input")

