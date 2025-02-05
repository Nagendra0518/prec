# import getpass

# class ATM:
#     def __init__(self):
#         self.users = {
#             "1234": {"pin": "4321", "balance": 1000},
#             "5678": {"pin": "8765", "balance": 2000}
#         }
#         self.current_user = None

#     def authenticate_user(self):
#         user_id = input("Enter your user ID: ")
#         if user_id in self.users:
#             pin = getpass.getpass("Enter your PIN: ")
#             if pin == self.users[user_id]["pin"]:
#                 self.current_user = user_id
#                 print("Authentication successful!")
#                 return True
#             else:
#                 print("Invalid PIN.")
#         else:
#             print("User ID not found.")
#         return False

#     def check_balance(self):
#         print(f"Your current balance is: ${self.users[self.current_user]['balance']}")

#     def deposit(self):
#         amount = float(input("Enter amount to deposit: "))
#         if amount > 0:
#             self.users[self.current_user]['balance'] += amount
#             print(f"Deposited ${amount}. New balance: ${self.users[self.current_user]['balance']}")
#         else:
#             print("Invalid deposit amount.")

#     def withdraw(self):
#         amount = float(input("Enter amount to withdraw: "))
#         if 0 < amount <= self.users[self.current_user]['balance']:
#             self.users[self.current_user]['balance'] -= amount
#             print(f"Withdrawn ${amount}. New balance: ${self.users[self.current_user]['balance']}")
#         else:
#             print("Invalid or insufficient funds.")

#     def logout(self):
#         self.current_user = None
#         print("Logged out successfully.")

#     def run(self):
#         if not self.authenticate_user():
#             return
#         while True:
#             print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Logout")
#             choice = input("Choose an option: ")
#             if choice == "1":
#                 self.check_balance()
#             elif choice == "2":
#                 self.deposit()
#             elif choice == "3":
#                 self.withdraw()
#             elif choice == "4":
#                 self.logout()
#                 break
#             else:
#                 print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     atm = ATM()
#     atm.run()











# from turtle import *
# import colorsys as cs
# pensize(2)
# tracer(2)
# h= 0.2
# bgcolor('black')
# lt(80)
# fd(250)
# lt(180)
# lt(80)
# for i in range(330):
#     c=cs.hsv_to_rgb(h,1,1)
#     color(c)
#     h+=0.004
#     fd(i)
#     rt(50)
#     rt(40)
#     fd(500)
#     rt(120)
# done()