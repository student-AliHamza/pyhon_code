list = []
for i in range(6):
    numbers = int(input('enters a numbers'))
    list.append(numbers)
    print(list)

    list2 = []
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if(list[i]>list[j]):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
list2.append(list)
print(list)
