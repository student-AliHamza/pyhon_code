def tri_recrsion(k):
    if k>0:
        return  k + tri_recrsion(k-1)
        print(result)
    else:
        result = 0
        return result
    
numbers = int(input("enter a number"))

print(numbers)
result = tri_recrsion(numbers)
print(result)