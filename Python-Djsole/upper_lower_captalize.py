string = input("enter the string")
print(string)
print("enter 1 for upper case")
print("enter 2 for lower case")
print("enter 3 for title")
print("enter 4 for captalize")
input_value =int(input())
if input_value == 1:
    print(string.upper())
elif input_value == 2:
    print(string.lower())
elif input_value == 3:
    print(string.title())
else:
    print(string.capitalize())

