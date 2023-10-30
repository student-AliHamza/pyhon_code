# def find_intersection(list1, list2):
#     intersection = []
#     for item in list1:
#         if item in list2 and item not in intersection:
#             intersection.append(item)
#     return intersection
# # Example usage:
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# result = find_intersection(list1, list2)
# print("intersection of the list is",result)
def find_intersection(list1,list2):
    intersection  = []
    for item in list1:
        if item in list2 and item not in intersection:
            intersection.append(item)
    return intersection

list1 = [2,4,5,6,8,9]
list2 = [4,6,79,3,8]
result = find_intersection(list1,list2)
print('the intersection of the list is',result)