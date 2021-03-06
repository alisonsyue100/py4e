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
            b=float(input("Enter Celsius temperature:"))
            c=(F(b))
            print(c)

        if a==2:
            d=float(input("Enter Fahrenheit temperature:"))
            e=(C(d))
            print(e)
            
        if a==3:
            print("Exit\nHave a nice day!")

        else:
            return main()
    else:
        return main()
             
main()



    
    

