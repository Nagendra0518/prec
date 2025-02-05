n = int(input("enter the units: "))
bill = 0
if n > 0:
    if n <= 200:
        bill = 0
    elif n > 200 and n <= 350:
        bill = 200 * 0 + (n - 200)*2
    elif n > 350 and n <= 450:
        bill = 200 * 0 + 150 * 2 + (n - 350)*5
    else: 
        bill = 200 * 0 + 150 * 2 + 100 * 5 + (n - 450)*10 
    print(bill)
else:
    print("invalid input")       