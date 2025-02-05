n = int(input("enter a number:"))
if n % 4 == 0:
    if n % 100 == 10:
        if n % 400 == 0:
            print("it is leap year")
        else:
            print("it is not leap year")
    else:
        print("it is leap year")
else:
    print("it is not a  leap year") 
