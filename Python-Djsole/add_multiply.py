list = []
sum = 0
multiply = 1
def test():
    for i in range(6):
        if i == 0:
            if 0:
                print('test')
            print("this is zero ")
        numbers = int(input('enters a numbers'))
        list.append(numbers)
        sum += numbers
        multiply *= numbers
print(list)
print("sum of the numbers",sum)
print("multiply the numbers",multiply)
