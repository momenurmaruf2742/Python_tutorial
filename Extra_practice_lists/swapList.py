"""
form a list i have to swap element between frist
and last
"""
class SwapElement():
    #approch 1
    def swapList(newlist):
        size = len(newlist)
        #swap logic
        temp=newlist[0]
        newlist[0]=newlist[size - 1]
        newlist[size -1] = temp
        return newlist
    #approce 2
    def swapList2(newlist):
        newlist[0],newlist[-1]=newlist[-1],newlist[0]
        return newlist
list1=[12,14,22,63,45,66]
list2=[11,14,22,63,45,55,456]
s=SwapElement
print(s.swapList(list1))
print(s.swapList2(list2))
