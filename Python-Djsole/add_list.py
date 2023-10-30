list = []
sum_numbers=0
for i in range(7):
    numbers = int(input("enters a numbers"))
    
    list.append(numbers)


    sum_numbers = sum(list)
    
print(list)
print("sum of numbers is :",sum_numbers)


result = 1
for num in list:
 result *= num
 print("multiplying the numbers are",result)



    