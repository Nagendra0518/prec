# print only even numbers

# x = [12,22,1,2,11,12,13,14,15,17,-22,-33,21,4,56,7,8]
# y = 0
# while y < len(x):
#     if x[y] % 2 == 0 and x[y] > 0:
#         print(x[y],end=" ") 
#     y = y + 1

# store only even numbers in list

# list = [1,2,3,4,5,6,7,8,5,43,3]
# even_list = []
# x = 0
# while x < len(list):
#     if list[x] % 2 == 0 and list[x] > 0:
#         even_list = even_list + [list[x]]
#     x += 1
# print(even_list)
    
       #OR 

# x = [1,2,3,4,5,2,2,3,6,7,42,2]
# list = []
# y = 0
# while y < len(x):
#     if x[y] % 2 == 0:
#         list += [x[y]]
#     y += 1
# print(list)

# reverse the even numbers in list

# list = [1,2,3,4,5,6,7,8,5,43,3]
# even_list = []
# rev_even_list =[]
# x = 0
# while x < len(list):
#     if list[x] % 2 == 0 and list[x] > 0:
#         even_list = even_list + [list[x]]
#         rev_even_list = [list[x]] + rev_even_list
#     x = x + 1
# print(rev_even_list)

# print A to Z alphabets

# x = 65
# while x <= 90:
#     print(chr(x), end = " ")
#     x = x + 1
    
# print Z to A alphabets

# x = 90
# while x > 64:
#     print(chr(x), end = " ")
#     x = x - 1

#  fibanocci series 

# x = 0
# y = 1
# n = 1
# l = []
# while n <= 10:
#     if n % 2 == 0:
#         print(x,end = " ")
#     l = l + [x]
#     x,y = y,x + y
#     n = n + 1
# print(l)
    
#------For Loops----------------
    
#1 to 10 numbers
# for i in range(1,10):
#     print(i, end=" ") 

# sum of first 10 numbers
# s = 0
# for i in range(10):
#     s += i
# print(s)

#alternate elements 
# for i in range(0,11,2):
#     print(i,end=" ")

#alternate elements in list
# a = [1,2,3,4,5,6,7,8,9,5,3,2]
# for i in range(0,len(a),2):
#     print(a[i],end=" ")

#sum of all elements in list
# a = [1,2,3,4,5,6,7,8,9,5,3,2]
# print(sum(a))
# s = 0
# for i in a:
#     s += i
# print(s)

#odd index even numbers
# a = [1,2,3,4,5,6,7,8,9,5,3,2]
# for i in range(1,len(a),2):
#     if a[i] % 2 == 0:
#         print(a[i],end=" ")

#reverse the list
# a = [1,2,3,4,5]
# # print(len(a))
# # for i in range(-1,-6,-1):
# for i in range(4,-1,-1):
#     print(a[i],end=" ")

#using while loop
# a = [1,2,3,4,5]
# b=4
# while b >= 0:
#        print(a[b],end=" ")
#        b = b - 1


#Design colors
from turtle import *
import colorsys as cs
pensize(2)
tracer(2)
h= 0.2
bgcolor('black')
lt(80)
fd(250)
lt(180)
lt(80)
for i in range(330):
    c=cs.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.004
    fd(i)
    rt(50)
    rt(40)
    fd(500)
    rt(120)
done()