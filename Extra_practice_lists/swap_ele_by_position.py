"""
Input : List = [25, 65, 21, 90], pos1 = 1, pos2 = 3
Output : [21, 65, 25, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]



"""

class SwapElemetByPositios():
    #approch1 (comma assignment)
    """
    Time Complexity: O(1), for using constant operations.
    Auxiliary Space: O(1), for using constant extra space.
    """
    def swapElement(p_list,pos1,pos2):
        # p_list=[]
        p_list[pos1-1],p_list[pos2-1]=p_list[pos2-1],p_list[pos1-1]
        return p_list
    
    #approch2 (temp variable)
    """
    Time Complexity: O(1), for using constant operations.
    Auxiliary Space: O(1), for using constant extra space.
    """
    def swapElementTemp(p_list,pos1,pos2):
        temp=p_list[pos1-1]
        p_list[pos1-1]=p_list[pos2-1]
        p_list[pos2-1]=temp
        return p_list

calling=SwapElemetByPositios
print(calling.swapElement([25, 65, 21, 90], pos1 = 1, pos2 = 3))
print(calling.swapElementTemp([25, 65, 21, 90], pos1 = 1, pos2 = 3))
