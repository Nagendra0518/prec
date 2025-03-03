# LOOPS CONCEPT

#------------------WHILE LOOPS-----------------

#--1 to 11 numbers--

# x = 1
# while x < 11:
#     print(x,end = " ")
#     x += 1 

# reverse order

# x = 10
# while x > 0:
#     print(x,end = " ") 
#     x = x - 1

# even numbers from 0 to 101

# x = 0
# while x < 101:
#     print(x,end = " ") 
#     x = x + 2 

# odd numbers from 1 to 100

# x = 1
# while x < 100:
#     print(x,end = " ") 
#     x = x + 2

# odd numbers from 99 to 1

# x = 99
# while x > 0:
#     print(x,end = " ") 
#     x = x - 2  

#  sum of 1 to 10 numbers

# x = 1
# s = 0
# while x < 11:
#     s = s + x
#     x = x + 1
# print(s)    
    
# In list print 1 to 10 numbers
    
# x = [1,2,3,4,5,6,7,8,9,3,4,5,6,7,77,88,55,4]
# y = 0
# while y < 10:
#     print(x[y],end = " ")
#     y = y + 1

# alternate elements in the list

# x = [1,2,3,4,5,6,7,8,9,3,4,5,6,7,77,88,55]
# y = 0
# while y < len(x):
#     print(x[y],end = " ")
#     y = y + 2

# odd index position elements

# x = [1,2,3,4,5,6,7,8,9,3,4,5,6,7,77,88,55]
# y = 1
# while y < len(x): 
#    print(x[y],end = " ")
#    y = y + 2

# even index position elements

# x = [1,2,3,4,5,6,7,8,9,3,4,5,6,7,77,88,55]
# y = 0
# while y < len(x): 
#    print(x[y],end = " ")
#    y = y + 2

# all elements in reverse order
 
# x = [1,2,3,4,5,6,7,8,9,3,4,5,6,7,77,88,55]
# y = 16
# while y > -1: 
#    print(x[y],end = " ") 
#    y = y - 1 
   
# print("-----------------------")
   
# x = [1,2,3,4,5,6,7,8,9,3,4,5,6,7,77,88,55]
# y = 16
# while y >= 0: 
#    print(x[y],end = " ") 
#    y = y - 1 
   
# alternate elements in reverse order in list
   
# x = [1,2,3,4,5,6,7,8,9,3,4,5,6,7,77,88,55]
# lt = []
# y = 16
# while y > -1: 
#    lt += [x[y]] 
#    y = y - 2    
# print(lt)

# sum of all elements in the list

# x = [1,2,3,4,5]
# print(sum(x))
#    #OR
# s = 0
# a = 0
# while a < len(x):
#     s += x[a]
#     a += 1
# print(s)

# storing even elements in list

# x = [1,2,3,4,5,2,2,3,6,7,42,2]
# list = []
# y = 0
# while y < len(x): 
#     if x[y] % 2 == 0:
#         list += [x[y]]
#     y += 1
# print(list)

# storing odd elements in list

# x = [1,2,3,4,5,2,2,3,6,7,42,2]
# list = []
# y = 0
# while y < len(x): 
#     if x[y] % 2 != 0:
#         list += [x[y]]
#     y += 1
# print(list)

# storing even elements in list
# x = [1,2,3,50,7,8,50,4,3,5,6,64,3,3,3,44,3,3,34]
# lt = []
# y= 0
# while y < len(x):
#     if x[y] % 2 == 0:
#         lt += [x[y]]
#     y += 1
# print(lt)

# sum of alternate elements from the list

# x = [1,2,1,3,1,3,1,6]
# s = 0
# a = 0
# while a < len(x): 
#     s += x[a]
#     a += 2
# print(s)

#---------OR------------

# x = [10, 20, 30, 40, 50]
# sum = 0
# a = 0
# while a < len(x):
#     sum += x[a]
#     a += 2  
# print("Sum of alternate elements using while loop:",sum)

# sum of odd index position elements

# x = [1,2,3,4,5,6,7,8,9,3,4,5,6,7,77,8,55]
# sum = 0
# y = 1
# while y < len(x):
#     sum += x[y]
#     y += 2
# print(sum)

# sum of even index position elements

# x = [1,2,3,4,5,6,1,8,10,3,4,5,6,7,10,8,5]
# sum = 0
# y = 0
# while y < len(x):
#     sum += x[y]
#     y += 2
# print(sum)

#  sum of even numbers from 2 to 101

# a = 2
# sum = 0
# while a < 101:
#     sum += a
#     a += 2
# print(sum)

# sum of odd numbers from 1 to 50

# a = 1
# sum = 0
# while a < 51:
#     sum += a
#     a += 2 
# print(sum)  

#  odd index even numbers

# x = [10,2,30,5,4,6,7,8,9,7,7,6,55,8]
# y = 1
# while y < len(x):
#     if x[y] % 2 == 0:
#         print(x[y],end = " ")
#     y += 2
  
#  odd index odd numbers  
    
# x = [1,2,3,5,4,3,7,8,9,7,7,6,55,8]
# i = 1
# while i < len(x):
#     if x[i] % 2 != 0:
#         print(x[i],end = " ")
#     i += 2
    
# sum of odd numbers from 1 to 50

# s = 0
# a = 1
# while a < 50:
#     s += a
#     a += 2
# print(s)

# sum of even numbers from 0 to 50

# s = 0
# a = 0
# while a < 50:
#     s += a
#     a += 2
# print(s)


# even numbers from list

# x = [1,2,3,4,5,6,7,8,9]
# a = 0
# while a < len(x):
#     if x[a] % 2 == 0:
#         print(x[a],end=" ")
#     a += 1

# odd numbers from list

# x = [1,2,3,4,5,6,7,8,9]
# a = 0
# while a < len(x):
#     if x[a] % 2 != 0:
#         print(x[a],end=" ")
#     a += 1
 
# print numbers which is divisible by both 3 and 5  
 
# x = [10,11,30,13,14,15,16,17,12,19,18] 
# a = 0
# while a < len(x):
#     if x[a] % 3 == 0 and x[a] % 5 == 0 :
#         print(x[a],end=" ")
#     a += 1

# print alternate index even numbers

# x = [10,11,30,13,14,15,16,17,12,19,18]
# a = 0
# while a < len(x):
#     if x[a] % 2 == 0:
#         print(x[a],end=" ")
#     a += 2

# print even index even numbers

# x = [10,11,30,13,14,15,16,17,12,19,18]
# a = 0
# while a < len(x):
#     if x[a] % 2 == 0:
#         print(x[a],end=" ")
#     a += 2
 
# print alternate index odd numbers

# x = [101,11,3,13,14,15,1,17,12,19,1]
# a = 0
# while a < len(x):
#     if x[a] % 2 != 0:
#         print(x[a],end=" ")
#     a += 2
 
# print even index odd nubers

# x = [101,12,3,13,14,10,1,17,12,19,1]
# a = 0
# while a < len(x):
#     if x[a] % 2 != 0:
#         print(x[a],end=" ")
#     a += 2
 
# print Odd index even nubers

# x = [101,12,3,13,14,10,1,17,12,19,1]
# a = 1
# while a < len(x):
#     if x[a] % 2 == 0:
#         print(x[a],end=" ")
#     a += 2
 
# print Odd index odd nubers

# x = [101,12,3,13,14,10,1,17,12,19,1]
# a = 1
# while a < len(x):
#     if x[a] % 2 != 0:
#         print(x[a],end=" ")
#     a += 2

#print A to Z

# x = 65
# while x <= 90:
#     print(chr(x),end=" ")
#     x += 1
 
#print table

# x = int(input("enter the number:"))
# y = 1
# while y <= 10:
#     print(f"{x} * {y} = {x * y}")
#     y += 1

#odd number odd position in list
# x = [12,3,4,6,7,78,89,5,4,6,9,9,3]
# y = 1
# lt= []
# while y < len(x):
#     if x[y] % 2 == 1:
#         lt += [x[y]]
#     y += 2
# print(lt) 
 
 
# positive numbers

# x = [1,2,3,5,-4,4,-4]
# y = 0 
# while y < len(x):
#     if x[y] >= 0:
#         print(x[y],end=" ")
#     y += 1
 
# negative numbers

# x = [1,-2,3,5,-4,4,-4]
# a = 0
# while a < len(x):
#     if x[a] < 0:
#         print(x[a],end=" ")
#     a += 1
 
# sum of positive numbers

# x = [1,2,3,5,-4,4,-4]
# a = 0
# s = 0
# while a < len(x):
#     if x[a] > 0 :
#         s += x[a]
#     a += 1
# print(s)
    
# sum of negative numbers

# x = [1,2,3,5,-4,4,-4]
# a = 0
# s = 0
# while a < len(x):
#     if x[a] < 0 :
#         s += x[a]
#     a += 1
# print(s)
 
# Fibanocci series

# a = 0 
# b = 1
# while a <= 10:
#     print(a,end=" ") 
#     a,b = b,a + b
    
# fibonacci numbers below 500

# a = 0
# b = 1
# while a < 500:
#     print(a,end=" ") 
#     a,b = b, a + b
      
# sum of first 10 fibonacci numbers

# x = [0,1]
# for i in range(2,10):
#     x.append(x[-1]+x[-2])
# y = sum(x)
# print(y)

#   ------OR---------
# n = 10
# a = 0
# b = 1
# count = 0
# sum = 0
# while count < n:
#     sum += a
#     c = a + b
#     a = b
#     b = c
#     count += 1
# print(sum)
      

 
 
 
# for i in range(0,101,2):
#     print(i,end=" ")
 
# a = 0
# for i in x:
#     a = a + i
# print(a)


# x = [10, 20, 30, 40, 50]
# sum = 0
# for i in range(0, len(x), 2):
#     sum += x[i]
# print("Sum of alternate elements using for loop:", sum)

#  only even numbers from list

# y = [10,2,3,5,6,7,8,9,1,5,8,4,3,9,7,6]
# for i in range (0,len(y)):         
#     if y[i] % 2 == 0 and y[i] > 0:
#         print(y[i],end = " ") 



