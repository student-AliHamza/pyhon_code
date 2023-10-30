# parent class
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)

# Child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited. Updated balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds: Balance Available", self.balance)
        else:
            self.balance -= amount
            print("Amount withdrawn. Updated balance:", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance:", self.balance)

name = input('Enter your name: ')
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
obj = Bank(name, age, gender)
obj.show_details()
while True:
    operation = input("Enter 1 for deposit, 2 for withdrawal, 3 for view balance:q for quit ")

    if operation == "1":
        deposit_amount = int(input("Enter the deposit amount: "))
        obj.deposit(deposit_amount)
    elif operation == "2":
        withdraw_amount = int(input("Enter the withdrawal amount: "))
        obj.withdraw(withdraw_amount)
    elif operation == "3":
        obj.view_balance()
    elif operation.lower == 'q':
        print("Existing the program,Good-By")
        break
    else:
        print("Invalid operation")
