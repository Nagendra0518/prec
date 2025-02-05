# ---------LOOPS-----------

# str2 = "learning python is simple"
# s1 = " "
# l1 = []
# for i in str2:
#     if i == " ":
#         l1 = l1 + [s1]
#         s1 = " "
#     else:
#         s1 = s1 + i
# l1 =l1+ [s1]
# print(l1)
     
     
# for i in range(11):
#     if i == 5:
#         pass
#     print(i,end =" ")

# def read():
#     print("nagendra")
# read()

# def double(a):
#     print(a * 2)
# double(100)
# double(11)

# def sum(a,b):
#     print(a + b)
# sum(10,11)

# for i in range(5): 
#     x='* '
#     x= x*i
#     print(f'{x:^10}')
# for i in range(5): 
#     x='* '
#     x= x*(5-i)
#     print(f'{x:^10}')

# sum = 0
# for i in range(1,10):
#     sum = sum + i
#     print(sum,end=" ")
    
    
# def make_abba(a, b):
#   print(a+b)
# make_abba('hi','bye')
    
     
# def birthday(name):
#     print(f"happy birthday {name}")
# birthday("nagendra")
    
# def make_abba(a,b):
#   print(a + b,b + a)
# make_abba('hi','bye')    
    

# def make_abba(a,b):
#   print(a + b,b + a)
# make_abba('Hi','Bye')
# make_abba('Yo','Alice')
# make_abba('What','Up')

#--------------FUNCTIONS-------------

#------------POSITIONAL PARAMETERS-----------
# def sub(a,b):
#     print(a + b)
# sub(a=10,b= 22)
# sub(b=10,a= 20) 


# --------------KEYWORD PARAMETERS----------
# def sub1(a,b):
#     print(a + b)
# sub1(10,20)
# sub1(10,23)
        
   
#---------one keyword and one positional------------- 

# def add(age,name):
#     print(age)
#     print(name)
# add(22,"nagendra")

#-----------using default parameter--------------

# def bio_data(name,age,pancardnum="nothing"):
#     print(name)
#     print(age)
#     print(pancardnum)
# bio_data("nag",22)

# def fun(name,email,*hobbies):
#     print(name)
#     print(email)
#     print(hobbies)
# fun("nag","nag@gmail.com","reading","cricket","cooking")
# fun("nag","nag@gmail.com","reading")
# fun("nag","nag@gmail.com")

# def m1(name,*skills,age = 22,pancard = "one"):
#     print(name)
#     print(skills)
#     print(age)
#     print(pancard)
# m1("nag","python","html","sql","css","javascript")

#----------using arbitary keyword parameter-----------

# def m1(name,**address):
#     print(name)
#     print(address)
# m1("nagendra",hno = 33,street = "nagalakatta",pincode= 560068,city= "jammalamadugu")


# d = {"hno":33,"street":"nagalakatta","pincode": 560068,"city": "jammalamadugu"}
# for i in d:
#     print(i,d[i])
# for i,j in d.items():
#     print(i,j)

# for i in d.keys():
#     print(i)
    
# for i in d.values():
#     print(i)

# def fun(x,*y,z=100):
#     print(x)
#     print(y)
#     print(z)
# fun(10,20,30,40,60)
# fun(10,20,30,40)
# fun(10,20,30,z=108)


# x= [10,30,40,50,60,66,7,7,6]
# x.remove(7)
# print(x)

# def m1(name,bachname,*student_diseases,**student_marks):
#     print(name)
#     print(bachname)
#     print(student_diseases)
#     print(student_marks)
# m1("suresh","aliens","malleria","dengue","cold",java=24,python=25,computers=23)

# ------------USING LIST-------------

# x = [10,20,30,40,50,60]
# x.append(70)
# print(x)

# x = [10,20,30,40,50,60]
# x.append([70,80,90])
# print(x)

# x = [10,20,30,40,50,60]
# x.extend([70,80,90])
# print(x)

# x = [10,20,30,40,50,60]
# x.insert(2,"nag")
# print(x) 

# x = [10,20,30,40,50,60]
# x.pop(2)
# print(x)

# x = [10,20,30,40,50,60]
# x.pop()
# print(x)

# x = [10,20,30,40,50,60]
# y= x.pop(2)
# x.pop()
# print(y)
# print(x)

# x = [10,20,30,40,50,60,50]
# x.remove(50)
# print(x)

# x = [10,20,30,40,50,60,20,20]
# x.index(20,1,4)
# print(x)

# x = [10,20,30,40,50,60,20,20]
# x.reverse()
# print(x)

# x = [10,20,30,40,50,60,20,20]
# x.sort()
# print(x)
# x.sort(reverse=True)
# print(x)

# x = [10,20,30,40,50,60,20,20]
# y = x.copy()
# print(y)



#-----------------------------LIST COMPREHENSION-----------------------------

# x= list(range(0,101,2))
# print(x)

# x= []
# for i in range(0,101,2):
#     x. append(i)
# print(x)

# x= []
# for i in range(0,10,2):
#     x. append(i)
#     print(x)

# x = [i**2 for i in range(0,101,2)]
# print(x)

# x = [i**2 for i in range(1,9)]
# print(x)

# x = [10,20,30,40,50,60]
# y = [x[i]*2 for i in range(6)]
# print(y)

# x = [10,20,30,40,50,60]
# y = [x[i] for i in range(6) if i % 2 == 1]
# print(y)


# l = [1,2,4,6,5,6,8,6,7,8,54,8,9,5,3,2]
# even=[i for i in l if i % 2 == 0]
# odd=[i for i in l if i % 2 == 1]
# print(even)
# print(odd)

# l = [1,2,4,5,6,8,7,8,4,5,6,78,89,9,8]
# x = ["python" if i % 2 == 0 else "django" for i in l]
# print(x)

# x = [l[i] for i in range(len(l)-1,-1,-1)]
# print(x)

# alternate_index_even_numbers = [l[i] for i in range(0,len(l),2) if l[i] % 2 ==0]
# print(alternate_index_even_numbers)


# -------------INTERVIEW QUESTION-------------

# num = int(input("enter the num:"))
# if num % 3 == 0 and num % 5 == 0:
#     print("palla nagendra")
# elif num % 3 == 0:
#     print("palla")
# elif num % 5 == 0:
#     print("nagendra")
# else:
#     print("invalid")

# -------LIST COMPREHENSION----------

# x = [i + 5 for i in range(10)]
# print(x) 

# x = [10,20,30,40,50,60,2,31,3,435]
# num = [i for i in x if i % 2 == 0 and i > 0]
# print(num) 


# for i in x:
#     if i % 2 == 0:
#         print(i * 2,end= " ")
#     else:
#         print(i- 2,end = " ")


# num = [i * 2 if i % 2 == 0 else i - 2 for i in x ]
# print(num)

# a = 2
# b = 1
# while b<=3:
    # a= a + 1            # it is itterating infinity numbers
#     print(a,end=" ")

    
# i = 1
# while i < 9:
#     if i not in (2,4,6,8):
#         i = i + 1
#         continue              # 2,4,6,8,
#     print(i,end= " ,")
#     i = i + 1 

# ------------insta codes--------------
# a = {1,2,3}
# b = {4,5,6} 
# print(a & b)

# a = [1,2,3]
# while a:
#     print(a.pop()) 

# a = [1,2,3]
# b = [4,5,6] 
# print(a + b)

# a = 0 
# for i in range(1,9):
#     a = a + i
#     print(i,end= ", ")
# print(a)

# vowel = ['a','e','i','o','u']
# string ='nagendra'
# count = 0
# for i in string:           # to count the vowels in string
#     if i in vowel:
#         count+=1
# print(count)


# def alpha(n):
#     for i in range(1,n+1):
#         for j in range(i,n+1):
#             print(chr(ord('A') -1+j),end=" ")
#             print()
# alpha(5)

# a = [1,2,3]
# b = [4,5,6] 
# list = [a,b]
# print(list[1][2])


# a = 1
# for i in range(2,6):
#     for j in range(2,6):
#         if i % j == 0:
#             a= a + i
# print(a)

# a = [0,1,2,31]
# l = a[1::-1]
# print(l)


# def heart():
#     for i in range(6):
#         for j in range(7):
#             if ((i==0 and j%3!=0) or
#                 (i==1 and j%3==0) or
#                 (i-j==2) or (i+j==8)):      ##-----------Heart in numbers-----------
#                 print(i,end=" ")
#             else:
#                 print(" ",end=" ")
#         print()
# heart() 



# ----------SET COMPREHENSIONS-------------

# x  = {i for i in range(10)}
# print(x) 

# y = [1,2,3,4,5,6,7,8,8,9,9,9,9,56,76,66,66,]
# x1= {i for i in y}
# print(x1)


#DICTIONARY COMPREHENSIONS

# num = {i:i**2 for i in range(1,10)}
# print(num)


# l = ["python","java","c#","django"]
# d = {i:len(i) for i in l}
# print(d)


# ------------LOCAL AND GLOBAL VARIABLES---------------

# capital = "delhi"
# def fun():
#     course = "python"
#     print("india capital:",capital)
#     print("course:", course)
# fun()


# x = 10
# y = 20
# def fun():
#     x = 100
#     print(x + y)
# def fun1():
#     y = 50
#     print(x + y)
# fun()
# fun1()
# print(x + y)


# x = 10
# def fun():
#     x = 20
#     print(x)
#     print(globals() ['x'])
# fun()

# x = 10
# y = 20
# def f1():
#     y =30
#     print(y)
#     print(globals()['x'])
#     print(globals() ['y'])
# f1()

# x = 10
# y = 20
# def m1():
#     global x
#     x =1000
#     print(x)
# m1()
# print(x)


#============LEGB RULE===============

# pi = 10
# from math import pi
# def m1():
#     pi = 100
#     def m2():
#         pi = 1000
#         print(pi)
#     m2()
# m1()


#==========OOPS===========

# class Doctor:
#     def write(self):
#         print('subjects')
#     def read(self):
#         print('exams')
# s1= Doctor()
# s1.write()
# s1.read()

# def fun(x,y):
#     print('x=',x)
#     print('y=',y)
#     print(x+y)
# fun(10,20)

#-----class-------

# class Doctor:
#     def fun(self,x,y):
#         print('x=',x)
#         print('y=',y)
# d1=Doctor()
# d1.fun(10,'nagendra') 

# class nag():
#     a=30
#     def output(self):
#         print(self.a)
# b=nag()
# b.output()


#---------multilevel inherintance---------

# class grandfather():
#     def outputa(self):
#         print('iam a grandfather')
# class parent(grandfather):
#     def outputb(self):
#         print('iam a parent')
# class child(parent):
#     def outputc(self):
#         print('iam a child')
# c=child()
# c.outputa()
# c.outputb()      
# c.outputc()


# -------multiple inheritance--------

# class father():
#     def outputa(self):
#         print('iam a father')
# class mother():
#     def output(self):
#         print('iam a mother')
# class child(father,mother):
#     def outputc(self):
#         print('iam a child')
# c=child()
# c.outputa()
# c.output()      
# c.outputc()

#--------herarchical inheritance--------

# class father():
#     def outputa(self):
#         print('iam a father')
# class child1(father):
#     def output(self):
#         print('iam a child1')
# class child2(father):
#     def outputc(self):
#         print('iam a child2')
# c=child1()
# c1=child2()
# c.outputa() 
# c.output()
# c1.outputa()  
# c1.outputc()


# class Patient():
#     def nag(self,name,age):
#         print(name)
#         print(age)
#     def read(self,s_name):
#         print(s_name)
# c1 = Patient()
# c1.nag("nagendra",22)
# c1.read("nagendra")
 
#-------CONSTRUCTOR-----------

# class PythonDeveloper():
#     def __init__(self,no,name,age):
#         print("no:",no)
#         print("name:",name)
#         print("age:",age)
#     def read(self,s_name):
#         print("s_name:",s_name)
# c1 = PythonDeveloper(5,"nagendra",22)
# c1.read("nagendra")

# class Python():
#     def __init__(self):
#         print("good")
#         print("morning")
#         print("sir")
# p1= Python()
# p1= Python()

# class School:
#     def __init__(self,x):
#         print(x) #10
#     def m1(self):
#         print(x)  #error
# s1=School(10)
# s1.m1()

# class School:
#     def __init__(self,x):
#         self.num=x
#     def m1(self):
#         print(self.num)
# s1=School(100)
# s1.m1()


# class Doctor:
#     def __init__(self,name,exp):
#         self.name = name
#         self.exp = exp
#     def suggest(self):
#         print(self.name) 
#         print(self.exp)
# s1 = Doctor("nag",2) 
# s1.suggest()

# class Student:
#     def __init__(self,name,age,place):
#         self.name1=name
#         self.age1=age
#         self.place1=place
#     def m1(self):
#         print(self.name1,self.age1,self.place1)
# s1=Student("nag",22,"bangalore")
# s1.m1()
# s2=Student("veena",21,"jammalamadugu") 
# s2.m1()
# print(s2.name1,s2.age1,s2.place1)
# print(s1.name1,s1.age1,s1.place1)


# class School:
#     def __init__(self,name,age):
#         self.name1=name
#         self.age1=age
#     def m1(self):
#         print(self.name1,self.age1)
# s1=School("nagendra",23)
# s1.m1()
# print(s1.name1)
# print(s1.age1)

# class School:
#     def __init__(self,x):
#         self.num=x
#     def m1(self):
#         print(self.num)
# s1=School(100)
# s1.m1()
# s2=School(200)
# s2.m1()

# class TrainersDept:
#     def __init__(self):
#         print("good")
#     def m1(self):
#         print("morning")
# class SalesDept:
#     def __init__(self,x):
#         print(x)
#     def m2(self):
#         print("sir")
# class HrDept:
#     def __init__(self, y):
#         print(y)
#     def m3(self):
#         print("medam")
# class Marketing:
#     def __init__(self, z):
#         print(z)
#     def m4(self):
#         print("sir/medam")
# td=TrainersDept()
# td.m1()
# sd=SalesDept(10)
# sd.m2()
# hd=HrDept(20)
# hd.m3()
# md=Marketing(30)
# md.m4()

# class Employee:
#     def m1(self):
#         print("hello world")
#     def m2(self):
#         print("hello python")
# e1=Employee()
# e1.m1()
# e2=Employee()
# e2.m2() 


# class Doctor:
#     def __init__(self,doctorname):
#         print("hello",doctorname)
#     def m1(self,doctorname,specialist):
#         print(doctorname, "is a",specialist)
# d1=Doctor("suresh")
# d1.m1("suresh","ent doctor")
# d2=Doctor("nag")
# d2.m1("ramesh","dentist")


# class Calculator:
#     def __init__(self,x,y):
#         self.x1=x
#         self.y1=y
#     def add(self):
#         print(self.x1+self.y1)
#     def sub(self):
#         print(self.x1-self.y1)
# c1=Calculator(100,20)
# c1.add()
# c1.sub()

# class School:
#     def __init__(self):
#         pass
#     def m1(self):
#         print(self.name,self.age)
# s=School()
# s.name = "palle"
# s.age = 22
# s.m1()

#-----class variable-------

# joined_year = 2023
# class Institute:
#     institute_name = "palle technologies"
#     def __init__(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course
#     def m1(self):
#         print("student name =",self.name)
#         print("student age = ",self.age)
#         print("student course =",self.course)
#         print(Institute.institute_name)
#         print(globals() ['joined_year'])
# s1 =Institute("ramesh",23,"python")
# s1.m1() 
# s2=Institute("ramesh",23,"python")
# print(Institute.institute_name)
# print(s2.name)
# print(s2.age)
# print(s2.course)


#----------TYPES OF METHODS--------------

#-------CLASS METHOD----------

#-------accessing class variable inside the variable---------

# class M:
#     name="nagendra"
#     num=5
#     def __init__(self):
#         self.x=10
#     def m1(self):
#         self.y=1000
#         print(M.name)
#         print(self.name)
#         print(self.y)
#         print("instance variable")
#         print(self.x)
# a1=M()
# a1.m1()

#-------accesing class variable outside the method---------

# class M:
#     name="nagendra"
#     num=5
#     def __init__(self):
#         self.x=10
#     def m1(self):
#         self.y=1000
# a1=M()
# print(a1.name)
# print(M.name)
# print(a1.x)
# print(M.num)
# a1.m1()
# print(a1.y)

#-------instance variable--------

# class M:
#     def __init__(self):
#         self.x=10
#         print("this is constructor")
#     def m1(self):
#         print("nagendra")
#         print(self.x)
# a1=M()
# a1.m1()

# class School:
#     @classmethod
#     def m1(cls):
#         cls.x=10
#         print("class method")
#     @staticmethod
#     def m2():
#         print("static method")
# s1=School()
# s1.m1()
# s1.m2()
# School.m2()
# School.m1()
# print(s1.x)
        
#-------- how to call methods--------

# class M:
#     def __init__(self):
#         self.x=100
#         print("this is constructor")
#     def m1(self):
#         print("nagendra")
#         print(self.x)
#     @classmethod
#     def m2(cls):
#         cls.x=10
#         print("class method")
#         print(cls.x)
#     @staticmethod
#     def m3():
#         print("static method")
# s1=M()                                   # ----M.m1() error----
# s1.m1()
# s1.m2()
# s1.m3()
# M.m2()
# M.m3()


# class Assignment:
#     def __init__(self,x,y):
#         print(x)
#         print(y)
#     def m1(self,name):
#         print(name)
#     @classmethod
#     def sample(cls,a,b,c):
#         print(a+b+c)
#     @staticmethod
#     def sample1(x):
#         print(x)
# a1=Assignment(10,20)
# a1.m1("nagendra")
# a1.sample(1,2,3)
# Assignment.sample(10,20,30)
# Assignment.sample1(1000)
# a1.sample1(100)


# class Assignment:
#     x ="palla nagendra"
#     def __init__(self):
#         self.y ="instance variable"
#         print(Assignment.x)
#         print(self.x)
#         print(self.y)
#     def sample(self):
#         print(self.y)
#         print(self.x)
#         print(Assignment.x)
#     @classmethod
#     def sample1(cls):
#         print(Assignment.x)
#         cls.z=12
#         print(cls.z)
#     @staticmethod
#     def sample2():
#         print(Assignment.x)
# a1=Assignment()
# a1.sample()
# a1.sample1()
# a1.sample2()
# Assignment.sample1()
# Assignment.sample2()


# class A:
#     x=10
#     def __init__(self):
#         self.y=20
#         print("hello")
#         print(self.y)
#     def m1(self):
#         print(A.x)
# a1=A()
# a1.m1()
# print(a1.x)
# print(a1.y)
# print(A.x)

#--------------method overriding---------------
# class A:
#     def m1(self):
#         print("nagendra")
# class B(A):
#     def m1(self): 
#         print("nag") 
# b1=B()
# b1.m1()
 
# class A:
#     def m1(self):
#         print("name")
# class B(A):
#     def m1(self):
#         print("agyftuf") 
#         print("jgf")
# b1=A()
# b1.m1()
# a1=B()
# a1.m1()

#------------method overloading------------

# class A:
#     def m1(self,x):
#         print(x)
#     def m1(self,y,z):          #--------python does not support METHOD OVERLOADING-----
#         print(y+z)
# b1=A()
# b1.m1(1,36) 
# b1.m1(1)

#-----------multilevel inheritance---------------

# class A:
#     def parent_class(self):
#         print("parent class")
# class B(A):
#     def intermediate_class(self):
#         print("intermediate")
# class C(B):
#     def child_class(self):
#         print("child class")
# c1=C()
# c1.parent_class()
# c1.intermediate_class()
# c1.child_class()
# b1=B()
# b1.parent_class()
# b1.intermediate_class()
        
#---------------super() key------------------

# class A:
#     def __init__(self):
#         print("class a")
# class B(A):
#     def __init__(self,x,y):
#         super().__init__()
#         print("class b =",x*y)
# class C(B):
#     def __init__(self):
#         super().__init__(10,44)
#         print("class c")
# b1=C()

# To print Odd numbers

# num = 0
# while num <= 101:
#     if num % 2 == 0:
#         num += 1
#         continue
#     print(num,end=" ")
#     num += 1

# To print even numbers

# number = [1,2,3,4,5,6,7,8,9,10]
# even_numbers= [num for num in number if num % 2 == 0]
# print(even_numbers)

#------------method overriding-------------------

# class A:
#     def f1(self):
#         print("hi")
# class B(A):
#     def f1(self):
#         print("hello")
# b1 = B()
# b1.f1()

# class A:
#     def m1(self,x):
#         print(x)
# class B(A):
#     def m1(self,y):
#         print(y)
# b1 = A()
# b1.m1(10)
# b1.m1(12)

#-----------------POLYMORPHISM--------------------

# x = 10
# print(type(x))

# x = "ten"
# print(type(x))

# x = 10,21
# print(type(x))

# x = 10.2
# print(type(x))

# class Polymorphism:
#     def f1(self,x):
#         print(type(x))
# c =Polymorphism()
# c.f1(10)
# c.f1("nag")

# class Arithmetic:
#     def sum(self,*x):
#         sum = 0
#         for i in x:
#             sum += i
#             print(sum,end=" ")
# a = Arithmetic()
# a.sum(10)
# a.sum(100,21)
# a.sum(40,50,60)

#-----------compile time error aslo known as syntax error------------

# print("hello)

#-------run time error also known as logical error------

# ZeroDivisionError,ValueError,IndexError etc

# a =10
# b = 0                     #---zeroDivisionError---
# print(a%b)

# --------------TRY block------------------

# a = 10
# b = 20
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print('caught the error')
# print("bye")

# a = 10
# b = 0
# try:
#     print(a%b)
# except ZeroDivisionError as msg:
#     print(msg)
# print("bye")

#-----------------READ MODE(r)-----------------

# f = open('C:/python Programs/file1.txt','r')
# line = f.read()
# print(line)
# f.close()

# f = open('C:/python Programs/file1.txt','r')
# line = f.readline()
# print(line)
# f.close()

# f = open('C:/python Programs/file1.txt','r')
# line = f.readlines()
# print(line)
# f.close()

#-----------------read and write mode(r+)-----------------------

# f = open('C:/python Programs/file1.txt','w+')
# f.write("new line added")
# f.seek(0)
# print(f.read())
# f.close()


# f = open('C:/python Programs/file1.txt','r')
# for i in f:
#     print(i,end="")
# f.close()


#-----------------------LAMBDA FUNCTIONS-----------------------

# c1 = lambda x : x ** 2
# print(c1(10))

# c2 = lambda : "hello"
# print(c2())

# c3 = lambda x,y : x + y
# print(c3(10,20))

# c4 = lambda x ,y = 20: x + y
# print(c4(10))
# print(c4(33,44))

# c5 = lambda * x : sum(x)
# print(c5(10,20,30,40))

# c5 = lambda * x : list(x)
# print(c5(10,20,30,40))

# n = input("enter the name: ")
# c6 = lambda x : x.upper()
# print(c6(n))

#Find the biggest of two numbers

# x= 12                                              
# y =33
# if x>y:                                         
#     print(x)
# else:
#     print(y)


#Find the biggest of two numbers using functions

# def big(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# a = big(11,22)
# print(a)

# big  = lambda x, y : x if x > y else y 
# a = big(62,10)
# print(a)

# big = lambda x,y,z :x if x > y and x > z else y if y > z else z
# print(big(100,200,30))

# def f1(fun):
#     result = fun(10)
#     print(result)
# def f2(x):
#     return x * 2
# f1(f2)

# def f1(fun):
#     result = fun(10)
#     print(result)
# f2= lambda x:x * 2
# f1(f2)

# def f1(fun):
#     result = fun(10)
#     print(result)
# f1(lambda x:x ** 2)

#------------lambda with filter-------------------

# x =[10,20,3,40,5]
# evennum = list(filter(lambda i : (i % 2 == 0),x))             #don't use "if" keyword in filter
# print(evennum)

# y =[10,20,3,40,5]
# oddnum = list(filter(lambda i : (i % 2 == 1),y))
# print(oddnum)

# x =[10,20,3,40,5,-2,-3,-4,-5]
# negativenum = list(filter(lambda i: i < 0,x))
# print(negativenum)

# x =[10,20,3,40,5,-2,-3,-4,-5]
# positivenum = list(filter(lambda i: i > 0,x))
# print(positivenum)

# num1 = tuple(filter(lambda i : i or i == 0 ,range(-10,11)))
# print(num1)

# oddnum = tuple(filter(lambda i : i % 2 == 1 or i == 0 ,range(-10,11)))
# print(oddnum)

# evennum = tuple(filter(lambda i : i % 2 == 0 or i == 0 ,range(-10,11)))
# print(evennum)

#------------lambda with MAP-------------------

# x =[10,4,5,6,7,3,5,7]
# for i in x:
#     print(i*2,end=" ")

# y = list(map(lambda i : i * 2,x))
# print(y)

# x =[10,-4,5,-6,7,-3,5,7,-4,-6,-4,5,-3,-3,34]
# y = list(map(lambda i : "positive" if  i > 0 else "negative" ,x))
# print(y)

# x =[10,-4,5,-6,7,-3,5,7,-4,-6,-4,5,-3,-3,34]
# y = list(map(lambda i : "negative" if  i < 0  else "even" if i % 2 == 0 else "odd" ,x))
# print(y)

# x =[10,-4,5,-6,7,-3,5,7,-4,-6,-4,5,-3,-3,34]
# rev = list(map(lambda i : x[i], range(len(x)-1,-1,-1)))
# print(rev)

# x =[10,-4,5,-6,7,-3,5,7,-4,-6,-4,5,-3,-3,34]
# alternate_index_numbers = list(map(lambda i : x[i] , range(0,len(x),2)))
# print(alternate_index_numbers)

# x =[10,-4,5,-6,6,-3,5,7,-4,-6,4,5,-3,-3,34]
# alternate_index_even_numbers = list(filter(lambda i : i % 2 == 0 and i > 0 ,map(lambda i : x[i],range(0,len(x),2))))
# print(alternate_index_even_numbers)

# x =[1,-4,5,-6,6,-3,5,7,-4,-6,4,5,-3,-3,34]
# alternate_index_odd_numbers = list(filter(lambda i : i % 2 == 1 and i > 0 ,map(lambda i : x[i],range(0,len(x),2))))
# print(alternate_index_odd_numbers)

#------------------------USING SUM----------------------------

# from functools import reduce


# x1 = [10,20,30,40,50,-60,-40] 
# sum_all_elements = reduce(lambda x, y: x + y,x1)
# print(sum_all_elements)

# x1 = [1,2,3,4,5,6,7,8,9]
# evennumbers =list(filter(lambda i : i % 2 == 0 ,x1))
# print(evennumbers)

# oddnumbers =list(filter(lambda i : i % 2 == 1 ,x1))
# print(oddnumbers)

# sum_even_numbers = reduce(lambda x,y : x + y,filter(lambda i : i % 2 == 0 ,x1))
# print(sum_even_numbers)

# sum_even_numbers = reduce(lambda x,y : x + y,evennumbers)
# print(sum_even_numbers)

# sum_odd_numbers = reduce(lambda x,y : x + y,filter(lambda i : i % 2 == 1 ,x1))
# print(sum_odd_numbers)

# d = {"vignesh":25,"sita":28,"veena":10,"sreenu":26}
# d1 = filter(lambda i : len(i) <= 5,d.keys())
# print(list(d1))
# print(d.items())

# d2 = sorted(d.items(),key=lambda i : i[1])
# print(dict(d2))

#-------------using ZIP to add dictionary data-----------------

# names = ["nagendra","suresh","ramesh","veena","sai"]
# ages = [22,21,32,21,20]
# print(dict(zip(names,ages)))

#=======================*****DECORATORS*****============================

# def m1(x, l1=[]):
#     l1.append(x)
#     # print(id(x))
#     # print(id(l1))
#     return l1
# print(m1(10))
# print(m1(20))
# print(m1(30))

# def m2():
#     print("hello")
# def m3():
#     m2()
# m3()

# def m6():
#     def m7():
#         print('hello')
#     return m7
# a = m6()
# print(a)
# a()

# def m6():
#     def m7():
#         print('hello')
#         return "python"
#     return m7()
# print(m6())

# def m1(x):
#     print(x)
# a= m1(10)
# print(a)

#--------custom decorators-----------

# def custom_decorator(fun):
#     def inner():
#         print("*" * 20)
#         print("*" * 20)
#         fun()
#         print("*" * 20)
#         print("*" * 20)
#     return inner
# @custom_decorator
# def m1():
#     print("welcome to python")
# m1()


# def square_decor(fun):
#     def inner(a):
#         s1 = fun(a)
#         return s1 ** 2
#     return inner
# @square_decor
# def m1(x):
#     return x
# a = m1(10)
# print(a)

# def cube_decor(fun):
#     def inner(a):
#         s1 = fun(a)
#         return s1 ** 3
#     return inner
# @cube_decor
# def m1(x):
#     return x
# a = m1(10)
# print(a)

# def sum_decor(fun):
#     def inner(x,y):
#         s = fun(x,y)
#         return sum(s)
#     return inner
# @sum_decor
# def m1(x,y):
#     return x,y
# a = m1(10,20)
# print(a)

# def upper_decor(fun):
#     def inner(a):
#         s = fun(a)
#         return s.upper()
#     return inner
# @upper_decor
# def m1(x):
#     return x
# a = m1("palle technologies")
# print(a)

# def lower_decor(fun):
#     def inner(a):
#         s = fun(a)
#         return s.lower()
#     return inner
# @lower_decor
# def m1(x):
#     return x
# a = m1("PALLE TECNOLOGIES")
# print(a)

# def split_decor(fun):
#     def inner(a):
#         s = fun(a)
#         return s.split()
#     return inner
# @split_decor
# def m1(x):
#     return x
# a = m1("palle technologies")
# print(a)

#---------------TIME CHECK----------------

# import time

# def time_decor(fun):
#     def inner():
#         start_time = time.time()
#         fun()
#         end_time = time.time()
#         return end_time - start_time
#     return inner
# @time_decor
# def m1():
#     for i in range(10):
#         pass
# a = m1()
# print(a)

#-------------Double decorator-----------------

# def split_decor(fun):
#     def inner(y):
#         s = fun(y)
#         return s.split()
#     return inner
# def upper_decor(fun):
#     def inner(y):
#         s = fun(y)
#         return s.upper()
#     return inner
# @split_decor
# @upper_decor
# def m1(x):
#     return x
# a = m1("palle technologies")
# print(a)

#---------Triple Decorator------------------  
            
# def cube_decor(fun):
#     def inner(a):
#         s1 = fun(a)
#         return s1 ** 3
#     return inner
# def square_decor(fun):
#     def inner(a):
#         s1 = fun(a)
#         return s1 ** 2
#     return inner
# def double_decor(fun):
#     def inner(a):
#         s1 = fun(a)
#         return s1 * 2
#     return inner
# @cube_decor
# @square_decor
# @double_decor
# def m1(x):
#     return x
# a =m1(1)
# print(a)

# num = int(input("enter num:"))
# if num >= 0 and num <10:
#     print("single digit number")
# elif num >= 10 and num <100:
#     print("it is two digit number")
# elif 10 <= num <100:
#     print("it is also two digit number")
# elif num >= 100 and num <1000:
#     print("three digit number")
# else:
#     print("above three digits number")

#---------Find the biggest of two numbers-----

# a = int(input("enter a number: "))
# b = int(input("enter b number: "))
# if a == b:
#     print("equal")
# elif a > b:
#     print("a is big")
# else:
#     print("b is big")



