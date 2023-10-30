# numbers = []
# for i in range(5):
#     num = int(input("enters a numbers"))
# numbers.append(num)
# divisible_by_5 = []
# for num in numbers:
#     if num % 5 == 0:
      
#         divisible_by_5.append(num)
#         if divisible_by_5:
#           print("Numbers divisible by 5:", divisible_by_5)
# else:
#     print("No numbers are divisible by 5.")
numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

divisible_by_5 = []

for num in numbers:
    if num % 5 == 0:
        divisible_by_5.append(num)

if divisible_by_5:
    print("Numbers divisible by 5:", divisible_by_5)
else:
    print("No numbers are divisible by 5.")