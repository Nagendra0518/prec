    # import array
# e = array.array("i",[10,20,30,40] )
# print(e)

# a = '10'
# b= '20'
# print(a*b)
 # swapping with using third variable 
# x =10
# y= 20
# z = x 
# x= y
# y= z
# print(x)
# print(y) 

# swapping without using third variable
# x= 10
# y= 12
# x,y=y,x
# print(x,y)


# 3. read a number from the keyboard and print factorial of a number

# ex: factorial of 5= 120

# n1 = int(input("enter a number:"))
# sum1 = 1
# if  n1 < 0:
# 	print('not found')
# elif n1 == 1:
# 	print(sum1)
# else:
#     for i in range(1,n1+1):
# 	    sum1 = sum1 * i
# print(sum1)

# 4. read a string from the keyboard and count no of vowels present in string
# a = input("enter the name: ")
# count = 0
# vowels = "aeiouAEIOU"
# for i in a:
#     if i in vowels:
#         count += 1
# print(count)

# 5. read a string from the keyboard and print in reverse order
# print string in reverse order
# s1 = input("enter a string:")
# rev = ""
# for i in s1:
# 	rev = i + rev
# print(rev)

# 6. read a string from the keyboard and print whether it is palindrome or not 

# s1 = input("enter a string:")
# rev = ""
# for i in s1:
# 	rev = i + rev
# print(rev)

# if rev == s1: # checking palindrome or not
# 	print("it is palindrome")
# else:
# 	print("not a palindrome")

# 7. print only palindrome from list 
# def palindrome(s1):
# 	rev = ""
# 	for i in s1:
# 		rev = i + rev
# 	if rev == s1: # checking palindrome or not
# 		return rev
# l1 = ["mom","dad",'malayalam','python','jpython']
# l2 = [j for j in [palindrome(i) for i in l1] if j is not None]
# print(l2)

   
# 9 store first 10 fibonacci numbers in list
# x = 0
# y = 1
# i = 0
# l1 = []
# while i < 10:
# 	l1 = l1 +[x]
# 	x,y = y,x + y
# 	i = i + 1
# print(l1)
 
# for i in range(0,10):
#     print('1' * i ) 

# 12.print all fibonacci numbers below 100
# x = 0
# y = 1
# count = 0
# while x < 100:
# 	print(x,end=" ")
# 	count += 1
# 	x,y = y,x + y
# print("count is:",count)


# str1 = "ramesh"
# list1 = list(str1)
# for i in range(len(list1)):
#     for j in range(0, len(list1) - i - 1):
#         if list1[j] > list1[j + 1]:
#             list1[j], list1[j + 1] = list1[j + 1], list1[j]
# print("".join(list1))

# n = int(input("enter a number:")) # 0
# dummy = n # 121
# rev = 0 #121
# while n > 0:
#     r = n % 10 # 1
#     rev = rev * 10 + r
#     n = n // 10 # 12
# if rev == dummy:
#     print("it is a palindrome")
# else:
#     print("not a palindrome")


# n = int(input("enter a number:")) # 0
# dummy = n # 121
# rev = 0 #121
# while n > 0:
#     r = n % 10 # 1
#     rev = rev + r ** len(str(dummy))
#     n = n // 10 # 12
# if rev == dummy:
#     print("it is a armstrong number")
# else:
#     print("armstrong number")

# n = 5
# for i in range(1,n+1):
#     print("* "* i)

# n = 5
# for i in range(1,n+1):
#     print("1 "* i)

# n = 5
# for i in range(1,n+1):
#     print("A "* i)

# n = 5
# for i in range(n,0,-1):
# for i in range(5,0,-1):
    # print("* "* i)


# n = 5
# for i in range(1,n+1):
#     print(" " * (n-i),end="")
#     print("* "* i)

# n = 5
# for i in range(n,0,-1):
#     print(" " * (n - i), end="")
#     print("* "* i)

# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()  
    
# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# n = 5
# for i in range(1,n+1):
#     print(" " * (n - i), end="")
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# n = 5
# for i in range(1,n+1):
#     print(" " * (n - i), end="")
#     for j in range(1,i+1):
#         print(chr(64+j),end=" ")
#     print()

# n = 5
# for i in range(1,n+1):
#     print(" " * (n - i), end="")
#     for j in range(1,i+1):
#         print(chr(64+i),end=" ")
#     print()
 

#prime number checking     
# n = int(input("enter the number:"))
# ref = False
# if n <= 1:
#     print("not a prime number")
# else:
#     for i in range(2,n):
#         if n % i ==0:
#             ref = True
#             break
#     if ref:
#         print("it is a prime number")
#     else:
#         print("not a prime number")