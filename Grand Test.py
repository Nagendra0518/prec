#================================ GRAND TEST ==============================================

#--------------------AMSTRONG NUM CHECK----------------------

# a = int(input("enter a number: "))
# b = a
# c = len(str(a))
# d = 0
# while a > 0:
#     r = a % 10
#     d = d + (r**c)
#     a = a // 10
# if b == d:
#     print("it is amstrong number")
# else:
#     print("it is not amstrong number")

#-------------------PALINDROME CHECK----------------------

# a = int(input("enter the number: "))
# b = a
# c = 0
# while a > 0:
#     r = a % 10
#     c = c * 10 + r
#     a = a // 10
# if b == c:
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")
    
#        OR

# a = input("enter a number:")
# if a == a[::-1]:
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")

# def palindrome(s1): 
#     s = ""
#     for i in s1:
#         s = i + s
#     if s == s1:
#         return s
# l1 = ['mom','dad','malayalam','python','jpython']
# l2 = [j for j in [palindrome(i) for i in l1] if j is not None]
# print(l2)


#-----------FIBANOCCI SERIES IN LIST--------------

# a = 0
# b = 1
# c = 0
# l1 = []
# while c < 10 :
# #     print(a,end=" ")
#     l1 = l1 + [a]
#     a,b = b,a+b
#     c = c + 1
# print(l1)

#-----------FIBANOCCI SERIES IN  REVERSE LIST--------------

# a = 0
# b = 1
# c = 0
# l1 = []
# while c < 10 :
#     l1 = [a] + l1
#     a,b = b,a+b
#     c = c + 1
# print(l1)

#---------sum of fibonacci numbers ----------

# a = 0
# b = 1
# c = 0
# sum = 0
# while c < 10:
#     sum = sum + a
#     a,b = b,a+b
#     c = c + 1
# print(sum)

#------count of fibonacci series-----------

# a = 0
# b = 1
# c = 0
# count = 0
# while c < 10:
#     count  += 1
#     a,b = b,a + b
#     c = c + 1
# print(count)

#-------checking vowels----------

# ch = input("enter the character:")
# vowels = "aeiouAEIOU"
# if ch in vowels:
#     print("it vowel")
# else:
#     print("it is not vowel")

# ch = input("enter the character:")
# count = 0
# vowels = "aeiouAEIOU"
# for i in ch: 
#     if i in vowels:
#         count += 1 
# print(count)

#------string in reverse order----------

# n = input("enter the character:")
# a = ""
# for i in n:
#     a = i + a
# print(a)

#----------- count letters -------

# n = input("enter the character:")
# count = 0
# a = ""
# for i in n:
#     a = a + i
#     count += 1
# print(count)

#---------FACTORIAL--------------

# n = int(input("enter a number:"))
# sum = 1
# for i in range(1,n + 1):
#     sum = sum * i
# print(sum)

       # OR
      
# def m1(n):
#     if n == 1:
#         return 1
#     return n * m1(n-1)
# a = m1(6)
# print(a)  

#---------PRIME NUMBER---------------

# n = int(input("enter a number: "))
# if n > 1:
#     ref = True
#     for i in range(2,n):
# #     for i in range(2,n//2+1):
#             if n % i == 0:
#               ref = False
#               break
#     if ref:
#        print("prime number")
#     else:
#        print("not prime number")
# else:
#     print("not a prime num") 

#-----------prime num below 100 in list--------

# n = 2
# l = []
# while n <= 100:
#     ref = True
#     for i in range(2,n):
#         if n % i == 0:
#             ref = False
#             break
#     if ref:
#        l += [n]
#     n += 1
# print(l)
              
#-----------prime num below 100 in reverse in list---------------

# n = 2
# l = []
# while n <= 100:
#     ref = True
#     for i in range(2,n):
#         if n % i == 0:
#             ref = False
#             break
#     if ref:
#         l = [n] + l
#     n += 1
# print(l)

#-----------prime num in list to another list ---------------

# n = 2
# l = [1,2,3,4,5,6,7,8,9,-11,-10]
# def prime_num(n):
#     if n > 1:
#         ref = True
#         for i in range(2,n):
#             if n % i == 0:
#                 ref = False
#                 break
#         if ref:
#             return n
# l1 = [j for j in [prime_num(i) for i in l] if j is not None]
# print(l1)

#--------------OR---------------------

# numbers = [11, 14, 17, 18, 19, 20, 23, 24, 29, 30]
# prime_numbers = []
# for num in numbers:
#     if num > 1:  
#         is_prime = True
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             prime_numbers.append(num)
# print("Original list:", numbers)
# print("Prime numbers list:", prime_numbers)


#-------sum of even numbers from list-------------

# l = [1,2,3,4,5,6,7,8,9,2,3,4,5]
# sum = 0
# for i in l:
#     if i % 2 == 0:
#         sum += i
# print(sum)

#-------sum of odd numbers from list------------- without using (sum) function

# l = [1,2,3,4,5,6,7,8,9,2,3,4,5]
# a = 0
# for i in l:
#     if i % 2 != 0:
#         a += i
# print(a)

#----print even numbers from list-----------

# a = [1,2,3,4,5,6,7,8,9,10]
# b = 0
# while b < len(a):
#     if a[b] % 2 == 0:
#         print(a[b],end=" ")
#     b += 1

# for i in range(0,10):
#     if i % 2 == 0:
#         print(i,end=" ")

#----print odd numbers from list-----------

# a = [1,2,3,4,5,6,7,8,9,10]
# b = 0
# while b < len(a):
#     if a[b] % 2 != 0:
#         print(a[b],end=" ")
#     b += 1

# for i in range(0,10):
#     if a[i] % 2 != 0:
#         print(a[i],end=" ")


#===========GRAND TEST 2=======================

#EVEN ODD BASED ARRAY QUESTIONS

#1.take an list of 10 numbers. write logic for printing even numbers prsent in the list

# x = [1,2,3,4,5,6,7,8,9,10]
# for i in range(0,len(x)):
#     if i % 2 == 0:
#         print(i,end=" ")

#2.take an list of 10 numbers. write logic for printing even numbers prsent in even indexes of the list

# x = [10,2,3,4,50,6,7,8,9,10]
# y = 0
# while y < len(x):
#     if x[y] % 2 == 0:
#         print(x[y],end=" ")
#     y += 2

            # OR

# x = [10,2,3,4,50,6,7,8,9,10]
# for i in range(0,len(x),2):
#     if x[i] % 2 == 0:
#         print(x[i],end=" ")

#3.take an list of 10 numbers. write logic for printing odd numbers present in the list

# x = [10,2,3,4,50,6,7,8,9,10]
# for i in range(0,len(x)):
#     if x[i] % 2 != 0:
#         print(x[i],end=" ")

#4.take an list of 10 numbers. write logic for printing odd numbers prsent in odd indexes of the list

# x = [10,3,2,4,50,5,7,8,9,1]
# for i in range(1,len(x),2):
#     if x[i] % 2 != 0:
#         print(x[i],end=" ")

#5.take an list of 10 numbers. write logic for calculating sum of even numbers and sum of odd numbers present in the list
# x = [1,2,3,4,5,6,7,8,9,10]
# sv = 0
# sd = 0
# for i in x:
#     if i % 2 == 0:
#         sv += i
#     else:
#         sd += i
# print(sv)
# print(sd)

#6.take an list of 10 numbers. write logic to calculate avg of the numbers present in the list
# x =[1,2,3,4,5,6,7,8,9,10]
# average = sum(x)/len(x) 
# print(average)

# Sample list of 10 numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# total_sum = 0
# index = 0
# # Calculate the sum using a for loop and track the number of elements
# for number in numbers:
#     total_sum += number 
#     index += 1           
# average = total_sum / index 
# print("Average of the numbers:", average)

#7. take an list of 10 numbers.write logic to calculate avg of even numbers present in the list . write logic to calculate avg of odd numbers present in the list
# x =[1,2,3,4,5,6,7,8,9,10]
# sv = 0
# sd = 0
# for i in x:
#     if i % 2 == 0:
#         sv += i
#         half = len(x)/2
#         avgv = sv / half
#     else:
#         sd += i
#         half = len(x)/2
#         avgd = sd / half
# print(avgv)
# print(avgd)

#8. take an list of 10 numbers. write logic for calculating difference between sum of even numbers and sum of odd numbers present in the list . difference should be printed as possitive number.
# x = [1,2,3,4,5,6,7,8,9,10]
# sv = 0
# sd = 0
# for i in x:
#     if i % 2 == 0:
#         sv += i
#     else:
#         sd += i
# print("difference of sum of even and odd :",sv-sd)

#9. take list of 10 numbers. write logic for printing even numbers and where ever odd numbers are present you have to print palle in place of that number.
# x = [1,2,3,4,5,6,7,8,9,10]
# lt = []
# for i in x:
#     if i % 2 == 0:
#        print(i,end=" ")
#     else:
#        print("palle",end=" ")

#10. take an list of 10 numbers. write logic for printing the list numbers which are divisible by both 3 & 5.
# x = [1,2,30,4,15,6,7,8,9,10]
# for i in x:
#     if i % 3 == 0 and i % 5 == 0:
#         print(i,end=" ")

#11. take an list of 10 numbers.write logic for calculating sum of numbers which are divisible by both 3 & 5.
# x = [1,2,30,4,15,6,7,8,9,10]
# s = 0
# for i in x:
#     if i % 3 == 0 and i % 5 == 0:
#        s += i
# print(s)

#12.take an list of 10 numbers. swap adjacent numbers. i.e 0th element should be copied into 1st element and vice versa. 2nd element should be copied into 3rd element and vice versa. etc.
# x = [1,2,3,4,5,6,7,8,9,10]
# for i in range(0,len(x)-1,2):
#     x[i],x[i+1] = x[i+1],x[i]
# print(x)

#13.take an list of 10 numbers. count how many negative numberse are there in the list and replace those elements with value 0.
# x = [1,-2,-8,9,-6,-4,7,3,9,10]
# count = 0
# for i in range(0,len(x)):
#     if x[i] < 0:
#         count += 1
#         x[i] = 0
# print(count)
# print(x)

#14.take an list of 10 numbers. read a number from keyboard. find the position of that number in the list.if number is not available you have to print number is not available. otherwise you have to print the position of that number.
# x = [1,2,3,4,5,6,7,8,9,10]
# n = int(input("enter a number: "))
# position = -1
# for i in range(0,len(x)):
#     if x[i] == n:
#        position = i
#        break
# if position != -1:
#     print(position)
# else:
#     print("not available")

#15.take an list of 10 numbers. read a number from keyboard. find the total occurences of that number in the list . use for loop, dont use any shortcut single line codes.
# x = [1,2,3,4,5,6,7,8,9,7,5]
# n = int(input("enter a number: "))
# occurrences = 0
# for i in x:
#     if i == n:
#         occurrences += 1
# print(occurrences)
        
#16.take list1 of 10 numbers. take list2 of 10 numbers. print common elements of list1 and list2. use for loop, dont use any shortcut single line codes.
# list1 = [1,2,3,6,8,5,4,7,8,9]
# list2 = [10,2,3,6,5,46,0,33,65,56]
# lt = []
# for i in list1:
#     for j in list2:
#         if i == j:
#             lt.append(i)
#             break
# print(lt)

#17.take list1 of 10 numbers. take list2 of 10 numbers. print list1 elements which are not present in list2. use for loop, dont use any shortcut single line codes.
# list1 = [100,2,3,4,50,6,7,8,9,10]
# list2 = [1,2,3,4,5,6,7,8,9,10]
# lt = []
# for i in list1:
#     found = False
#     for j in list2:
#        if i == j:
#             found = True
#             break
#     if not found:    
#        lt.append(i)
# print(lt)

#18.take list1 of 10 numbers. take list2 of 10 numbers. print list2 elements which are not present in list1.use for loop, dont use any shortcut single line codes.
# list1 = [100,2,3,4,50,6,7,8,9,10]
# list2 = [1,2,3,4,5,6,7,8,9,10]
# lt = []
# for i in list2:
#     found = False
#     for it in list1:
#         if i == it:
#             found = True
#             break
#     if not found:    
#         lt.append(i)
# print(lt)

#19.take list1 of 10 numbers. take list2 of 10 numbers. print uncommon elements of list1 and list2.use for loop, dont use any shortcut single line codes.
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = [1,12,3,44,5,66,7,88,9,10]
# lt = []
# for i in list1:
#     found = False
#     for j in list2:
#         if i == j:
#             found = True
#             break
#     if not found:    
#         lt.append(i)
# for i in list2:
#     found = False
#     for j in list1:
#         if i == j:
#             found = True
#             break
#     if not found:
#         lt.append(i)
# print(lt)

#ARRAY COPYING BASED QUESTIONS.


#1.take an list1 of 10 numbers.take an empty list2. write for loop logic to copy list1 elements into list2.
# x = [1,2,3,4,5,6,7,8,9,10]
# y = []
# for i in x:
#        y.append(i)
# print(y)

#2.take an list1 of 10 numbers. take an empty list2 . write for loop logic to copy list1 elements in reverse order into list2. Reverse order means last element of list1 should be copied into 0th position of list2. last but one element of list 1 should be copied inot list2 1st index etc...
# x = [1,2,3,4,5,6,7,8,9,10]
# y = []
# for i in range(len(x)-1,-1,-1):
#        y.append(x[i])
# print(y)

#3. take an list1 of 10 numbers. take empty list2 and empty list3. copy even numbers prsent into list1 into list2 and copy odd numbers present in list1 into list3.
# x = [1,2,3,4,5,6,7,8,9,10]
# y = []
# z = []
# for i in x:
#        if i % 2 == 0:
#               y.append(i)
#        else:
#               z.append(i)
# print(y)
# print(z)

#4. take an list1 of 10 numbers. take list2 of 10 numbers. assume that list1 and list2 sizes are same. take empty list3. add list1 and list2 elements and store into list3 in the same position.
# i.e add 0th element of list1 and list2 and store in 0th index of list3
#     add 1st element of list1 and list2 and store in 1st index of list3 etc..

# x = [1,2,3,4,5,6,7,8,9,10]
# y = [10,9,8,7,6,5,4,3,2,1]
# z = []
# for i in range(0,len(x)):
#        z.append(x[i]+y[i])
# print(z) 

#5. take an list1 of 10 numbers. take list2 of 10 numbers. take list3 and list4 as empty lists. if sum of 0th element of list1 and list2 is even, then copy that sum into list3 else copy that sum into list4.
#    if sumo f 1st element of list1 and list2 is even, then copy that sum into list3 else copy that sum into list4. etc..
# x = [1,2,3,4,5,6,7,8,9,10]
# y = [10,20,30,40,50,60,70,80,90,100]
# a = []
# b = []
# for i in range(len(x)):
#        total = x[i]+y[i]
#        if total % 2 == 0:
#               a.append(total)
#        else:
#               b.append(total)
# print(a)
# print(b)

#6. take list1 of some numbers, take list2 of some numbers. ensure that list1 and list2 sizes are different. now take empty list3. first copy list1 elements into list3, then copy list2 element into list3.
#    so if i print list3 then first it should print list1 element then it should display list2 elements.
# x = [1,2,3,4,5,6,7]
# y = [2,4,6,7,9]
# z = []
# for i in x:
#        z.append(i)
# for i in y:
#        z.append(i)
# print(z)

#7. take list1 with 10 numbers. copy even index elements of list1 into list2. copy odd index elements of list1 into list3.
# x = [1,2,3,4,5,6,7,8,9,10]
# y = []
# z = []
# for i in x:
#        if i % 2 == 0:
#               y.append(i)
#        else:
#               z.append(i)
# print(y)
# print(z)

#8. take list1 with 10 numbers. copy biggest of sequence pair of elements from list1 into list2. eg list1=[10,-20,30,40,50,-60,70,-80,90,100]
#    now sequence pair of elements of list1 are [10,-20]   [30,40]  [50,-60]  [70,-80]  [90,100]
#    big of first pair is 10, big of second pair is 40, big of third pair is 50, big of 4th pair is 70, big of 5th pair is 100.
#    and you have to copy 10,40,50,70,100 into list2.
# x = [10,-20,30,40,50,-60,70,-80,90,100]
# y =[]
# for i in range(0,len(x),2):
#        first = x[i]
#        second = x[i+1] if i + 1 < len(x) else None
#        maxm = first if second is None else max(first,second)
#        y.append(maxm)
# print(y)

#9.take list1 of 10 numbers. take list2 of 10 numbers. take empty list3 and list4. copy common elements of list1 and list2 into list3. and copy rest (uncommon elements) of list1 and list2 elements into list4.
# x = [1,3,3,4,2,6,7,8,9,8]
# y = [9,9,8,7,6,5,1,3,1,2]
# a = []
# b = []
# for i in x:
#        if i in y and i not in a:
#               a.append(i)
# for i in x:
#        if i not in a:
#               b.append(i)
# for i in y:
#        if i not in a and i not in b:
#               b.append(i)
# print(a)
# print(b) 

#STRINGS BASED QUESTIONS

#1.take str1 = "palle". count how many vowels are there in the string. and write logic to find how many consonents are there in the string.
# str = "palle"
# vowels = "aeiouAEIOU"
# count = 0
# con_count = 0
# for char in str:
#        if char in vowels:
#           count += 1
#        else:
#           con_count += 1
# print(count)
# print(con_count)  

#---------------------or------------------

# n = input("enter the char: ")
# vowels = "aeiou"
# count = 0
# con_count = 0
# for ch in n:
#        if ch in vowels:
#               count += 1
#        else:
#               con_count += 1
# print(count)
# print(con_count)

#2. take str1 = "palle java python bangalore". write logic find how many words are there in the string.
# str1 = "palle java python bangalore"
# words = str1.split()
# count = len(words)
# print(count)

#3. take str1 = "palle". print letters which are not vowels.
# str1 = "palle"
# vowels = "aeiouAEIOU"
# lt =  []
# for char in str1:
#        if char  not in vowels:
#               lt.append(char)
# print(lt)
# print(''.join(lt))     
       
#4. take str1 = "abcd" take str2="wxyz" copy str1 and str2 letters into str3 so that when we print str3 output should look like "awbxcydz".
# x = "abcd" 
# y = "wxyz"
# z = ""
# for i in range(len(x)):
#        z += x[i] + y[i]
# print(z)       

#5. take str1 = "abcdef" take str2="uvwxyz" copy str1 and str2 letteres into str3 so that when we 
# print str3 output should look like "abuvcdwxefyz"
# str1 = "abcdef"
# str2 = "uvwxyz"
# str3 = ""
# for i in range(0, len(str1), 2):
#     str3 += str1[i:i+2] + str2[i:i+2]
# print(str3)

#6.take str1 = "abcdef". copy vowels into str2 and copy consonents into str3.
# x = "abcdef"
# y = ""
# z = ""
# vowels = "aeiouAEIOU"
# for char in x:
#        if char in vowels:
#               y += char
#        else:
#               z += char
# print(y)
# print(z)

#7.take two strings str1=”abcd”; str2=”wxyz”. Assume that both str1 and str2 length is same. Write a generic 
# logic to form string str3 in such way that str3 value will be “azbycxdw”. Your logic should work even if we change 
# str1 and str2 contents, and assume both strings str1 and str2 lengths are same always. Should not use string builder or string buffer.
# def interleave_strings(str1, str2):
#     str3 = ""
#     length = len(str1)
#     for i in range(length):
#         str3 += str1[i] + str2[length - 1 - i]
#     return str3
# str1 = "abcd"
# str2 = "wxyz"
# str3 = interleave_strings(str1, str2)
# print(str3)

#8.take str1 = "abcd" take str2="wxyz" copy str1 and str2 letters into str3 so that when we print str3 outpu should look like "azbycxdw".

# def interleave_strings(str1, str2):
#     str3 = ""
#     length = len(str1)
#     for i in range(length):
#         str3 += str1[i] + str2[length - 1 - i]
#     return str3
# str1 = "abcd"
# str2 = "wxyz"
# str3 = interleave_strings(str1, str2)
# print(str3)

#9. take two strings str1 with some value.  You have to copy str1 elements into String str2 in such a way that
# # whenever you encounter vowel(small letter) then you have to copy letter z into str2 otherwise copy same letter into str2. 
# EG: if str1 = “palle” then str2 will be “pzllz”.

# str1 = "palle"
# vowels = "aeiou"
# str2 = ""
# for char in str1:
#     if char in vowels:
#         str2 += 'z'    
#     else:
#         str2 += char     
# print(str2)

# def replace_vowels_with_z(str1):
#     vowels = "aeiou"
#     str2 = ""
#     for char in str1:
#         if char in vowels:
#             str2 += 'z'
#         else:
#             str2 += char
#     return str2
# str1 = "palle"
# str2 = replace_vowels_with_z(str1)
# print(str2)

















