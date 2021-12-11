from customer import Customer
from admin import Admin
from person import Person

class Account:

        def __init__(self, balance, account_no):
                self.balance = float(balance)
                self.account_no = account_no

        def deposit(self, amount):
                self.balance+=amount

        def withdraw(self, amount):
                self.balance=self.balance-amount

        #create a withdraw class opposite to the deposit class

                        
        def print_balance(self):
                print("Your account balance is %.2f" %self.balance)

        def get_balance(self):
                return self.balance

        def get_account_no(self):
                return self.account_no

        def account_menu(self):
                #print the options you have
                 print (" ")
                 print ("Your Transaction Options Are:")
                 print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                 print ("1) Deposit money")
                 print ("2) Withdraw money")
                 print ("3) Check balance")
                 print ("4) Back")
                 print (" ")
                 option = int(input ("Choose your option: "))
                 return option

        def run_account_options(self):
                loop = 1
                while loop == 1:
                        choice = self.account_menu()
                        if choice == 1:
                                amount=float(input("\nPlease enter amount to be deposited: \n"))
                                deposit = self.deposit(amount)
                                self.print_balance()
                        elif choice == 2:
                                amount=float(input("\nPlease enter the amount you want to withdraw: \n"))
                                deposit = self.withdraw(amount)
                                self.print_balance()
                        elif choice == 3:
                                self.print_balance()
                        elif choice ==4:
                                loop = 0
                print ("Exit account operations")


