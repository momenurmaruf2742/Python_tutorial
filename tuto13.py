# if else conditions
var1 =  6
var2 = 56
var3 =  int(input())

if var3>var2:
    print("Greter")
elif var3==var2:
    print("equal")
else:
    print("Leaser")

list =[5,4,3,2,1]

list1 = int(input())
if list1 in list:
    print("yes is in the least")
else:
    print("no")

print(5 not in list)

#excersice

age = float(input("Enter Your age:\n"))
if age<18:
    print("you cant drive")
elif age==18:
    print("you can come for physical test we not sure you can drive or not")
else:
    print("you can drive")
