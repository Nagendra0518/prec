a=float(input("enter first num:"))
b=float(input("enter second num:"))
print("press 1 for add\n,press 2 for sub\n,press 3 for mul\n,press 4 for div\n,")
choice=int(input("eneter your choice 1-4:"))
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:
    print(a*b)
elif choice==4:
    print(a/b)
else:
    print("invalid num:")