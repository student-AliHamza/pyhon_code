
numbers = []
for i in range(5):
 num = int(input('enters a numbers'))
 numbers.append(num)
 print(numbers)

 even_numbers = []
 for num in numbers:
  if num % 2 == 0:
   even_numbers.append(num)
   print(even_numbers)
   sum_of_numbers = sum(even_numbers)
   print("sum of even numbers is ",sum_of_numbers)
   
   

