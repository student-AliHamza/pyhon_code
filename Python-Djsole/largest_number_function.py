def largest_numbers():
    list = [10,20,30,4,90,8]
    max = list[0]
    for number in list:
        if number > max:
            max = number
    return max

result = largest_numbers()
print("the greatest number is",result)
     