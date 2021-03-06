def F(b):
    return (b)*5/9+32

def C(d):
    return ((d)-32)/5*9

#b為輸入的攝氏溫度
#d為輸入的華氏溫度


def main():
    o=(input("Enter a action:"))
    if o.isdigit():
        a=int(o)
        if a==1:
            b=input("Enter Celsius temperature:")
            if b.isdigit():
                c=F(int(b))
                print("Fahrenheit tempreature:"+str(c))
            else:
                print("Error, please enter numeric input")
                return main()

        if a==2:
            d=input("Enter Fahrenheit temperature:")
            if d.isdigit():
                e=C(int(d))
                print("Celsius temperature:"+str(e))

            else:
                print("Error, please enter numeric input")
                return main()
            
        if a==3:
            print("Exit\nHave a nice day!")

        else:
            return main()
    else:
        return main()
             
main()



    
    

