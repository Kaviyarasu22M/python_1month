year=int(input("enter the leapyear:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("it is leapyear")
        else:
            print("it is not leapyear")
    else:
        print("it is leap year")
else:
    print("it is not leapyear")