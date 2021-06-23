#list
grocery = ["Harpic","vim bar","deodrant","Bhindi","Lollypop"]

print(grocery)
print(grocery[1])#indexin waise print

numbers = [2,7,9,11,3]
#numbers.sort()
#numbers.reverse()
print(numbers[::-1])#slicing and revers
print(max(numbers))
print(min(numbers))

#append
numbers.append(11)#adding 11 in the last index
numbers.insert(2,23)#adding 23 in 2 number index
numbers.remove(11)#11 remove from main list
numbers.pop()#remove last index number
numbers[1] = 4
print(numbers)

#tulple = immutable
tp= (1,2,3,4,)
print(tp)

#swaping
a = 1
b = 2
a,b = b,a
print(a,b)

"""
search google for list function
"""