# a=10
# b=15
# print('before swap a is',a,'b is',b)
# a,b=b,a
# print('after swap a is',a,'b is',b)      


# # using xor 
# a, b = 5, 10
# print("Before swapping: a =", a, ", b =", b)
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print("After swapping: a =", a, ", b =", b)

# #using operators
# a, b = 5, 10
# print("Before swapping: a =", a, ", b =", b)
# a = a + b  # a becomes 15
# b = a - b  # b becomes 5 (original value of a)
# a = a - b  # a becomes 10 (original value of b)
# print("After swapping: a =", a, ", b =", b)


# Key Takeaways of garbage collection
# ✅ Python automatically manages memory using reference counting and cyclic garbage collection
# ✅ You can manually enable, disable, or force garbage collection using the gc module
# ✅ Cyclic references (objects referring to each other) are handled by the garbage collector
# ✅ Garbage collection helps prevent memory leaks and improves performance


# import copy

# # Original list with nested list
# original = [[1, 2, 3], 4, 5]

# # Shallow copy
# shallow_copied = copy.copy(original)
# shallow_copied[0][0] = 99  # Changes reflect in original!

# # Deep copy
# deep_copied = copy.deepcopy(original)
# deep_copied[0][1] = 77  # No change in original!

# print(original)  # [[99, 2, 3], 4, 5]
# print(deep_copied)  # [[99, 77, 3], 4, 5]



# import copy

# # Base shopping cart template
# cart_template = {"items": ["Apple", "Banana"], "total": 20}

# # Create a new user's cart using shallow copy
# user_cart = copy.copy(cart_template)

# # User modifies their cart
# user_cart["items"].append("Orange")

# # Check original cart
# print("Original Cart:", cart_template)  
# print("User's Cart:", user_cart)

# class Nag:
#     def __init__(self,price):
#         self.price = price
#     def display(self):
#         print(self.price)
# a = Nag('33000')
# a.display()

#------polymorphism types---------
#-----method overloading---------

# class A:
#     def sum(self,a,b):
#         return a+b
#     def sum(self,a,b,c):
#         return a+b+c
# obj = A()
# print(obj.sum(1,2))

# To over come the method overloading we want to use default parameters
# class A:
#     def sum(self,a,b):
#         return a+b
#     def sum(self,a,b,c=1):
#         return a+b+c
# obj = A()
# print(obj.sum(1,2)) 

#--------method over riding-----------

class A:
    def display(self):
        print("this is class A")
class B(A):
    def display(self):
        super().display()
        print("this is class B")     
obj = B()
obj.display()
