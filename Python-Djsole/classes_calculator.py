class Calculator:
    def __init__(self):
        self.result = 0
    def add(self,a,b):
        return a + b
    def subtract(self,a,b):
        return a - b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b!= 0:
         return a / b
        else:
            print("cannot divide zero ")

obj_calculator = Calculator()
num1 = int(input("enter a number"))
num2 = int(input("enter a second number"))
result_add = obj_calculator.add(num1,num2)
print("The addition of two number is",result_add)
result_sub = obj_calculator.subtract(num1,num2)
print("The subtraction of two number is",result_sub)
result_multiply = obj_calculator.multiply(num1,num2)
print("The multiplication of two number is",result_multiply)
result_divide = obj_calculator.divide(num1,num2)
print("the division of two number is",result_divide)