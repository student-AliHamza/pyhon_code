def find_missing_number(list, n):
    for i in range(1, n + 1):
        if i not in list:
            return i

list = [3, 7, 1, 2, 8, 4, 5]
n = 8
missing_number = find_missing_number(list, n)
print("The missing number is", missing_number)
