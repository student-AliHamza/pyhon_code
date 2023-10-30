# find the factorial 
def factorial(n):
    if(n>0):
        return n * factorial(n-1)
    else:
        return 1

number = int(input("enter a number"))
result = factorial(number)
print(number)
print("the result of factorial is",result)

