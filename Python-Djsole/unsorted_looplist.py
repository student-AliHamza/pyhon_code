
def sorted_list(list2, n):
    total, total2 = 0, 0
    for i in list2:
        total = total + i
    
    for i2 in range(n+1):
        total2 = total2 + i2
    
    print(total2-total)
sorted_list( [3, 7, 1, 2, 8, 4, 5],8)