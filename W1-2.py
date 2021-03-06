def Fahreheit(Enter_Celsius_temperature):
    return (Enter_Celsius_temperature)*5/9+32

def Celsius(Enter_Fahrenheit_temperature):
    return ((Enter_Fahrenheit_temperature)-32)*9/51

while True:

    O=int(input("Enter a action:"))


    if O==1:
        while True:
            Celsius=(input("Enter Celsius temperature:"))
            if Celsius.isdigit(): 
                C = (Fahreheit(int(Celsius)))
                print ("Fahreheit:"+str(int(C)))
                break
            else:
                print("Error, please enter numeric input")   
        
    if O==2:
        while True:
            Fahrenheit=(input("Enter Fahrenheit temperature:"))
            if Fahrenheit.isdigit():
                F = Celsius(int(Fahrenheit))
                print ("Celsius:"+str(int(F)))
                break
            else:
                print("Error, please enter numeric input")
                
    if O==3:
        print("Exit")
        break

    

