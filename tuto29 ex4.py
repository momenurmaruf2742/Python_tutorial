# # excersise 4 partan printing
# number_of_stars = int(input("enter your number to print stars:"))
# new = int(input("'1'of stars start from 1 and '0' for stars start from N:"))
# bool = bool(new)
# if bool==True:
#     print(bool)
#     for i in range(1,number_of_stars+1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()
# elif bool ==False:
#     print(bool)
#     for i in range(number_of_stars,0,-1):
#         for j in range(1, i + 1):
#             print("*",end=" ")
#         print()
#others solutions
print("pattern printing")
num = int(input(" enter how many number you wants to print"))
bool1 = input("1 for tsrue 0 for false")
if bool1 == "1":
    for i in range(0,num+1):
        print("*"*int(i))
elif bool1 =="0":
    for i in range(num,0,-1):
        print("*"*int(i))
