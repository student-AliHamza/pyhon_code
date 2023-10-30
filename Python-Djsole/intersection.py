

def intersection():

    list1 = [2,3,4,5,6]
    list2 = [4,1,9,3,6]

    result = list(set(list1) & set(list2))
    print("the intersection of list is",result)
    
    result = list1 + list2
    print("the union of list is",result)


intersection()