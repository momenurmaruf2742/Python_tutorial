class Exists():
    
    # Check if an element exists in the list using the “in” statement
    
    def existsElementCheckByIn(lst,e):
        if e in lst:
            return "exist"
        else:
            return "Not exist"
    """
    Time Complexity: O(1)
    Auxiliary Space: O(n), where n is the total number of elements.
    """

    # Using For loop
    def existsElementCheckByForLoop(lst,e):
        for i in range (len(lst)):
            print(lst[i],e)
            if lst[i] == e:
                return "element exist"
    """
    Time Complexity: O(n)
    Auxiliary Space: O(1)
    """

    # Using count
    def existElementCheckByCount(lst,e):
        counter=lst.count(e)
        if counter > 0:
            return "element exist"
        else:
            return "element no in the list"

calling=Exists
print(calling.existElementCheckByCount([11,23,3,6,5,8,9,2,2],1))
