# using len()function
def lenOfList(list):
    n=len(list)
    return n
l=lenOfList(list=[1, 4, 5, 7, 8])
print(l)

#using recursive functions()
def count_element_by_recursive(list):
    if not  list:
        return 0
    return 1 + count_element_by_recursive(list[1:])
test_list = [1, 4, 5, 7, 8]
print("The total element of a list using Recursive",count_element_by_recursive(test_list))

# using enumerate
def count_element_by_enumerate(list):
    i=0
    for count,element in enumerate(list):
        i+=1
    return i

print("The enumerate function of the list is",count_element_by_enumerate([1, 4, 5, 7, 8]))