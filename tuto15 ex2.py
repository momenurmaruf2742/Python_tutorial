#tutorial 14 excersice 1 solved

num1 = int(input("Enter your frist number:"))
num2 = int(input("Enter your second number:"))
what_do_you_want = (input("""
        a=addition
        b=subtruct
        c=multiply
        d=divided

"""))
if what_do_you_want =="a":
    if num1 ==56 and num2==9:
        print("here is your sum:",77)
    else:
        print("here is your number :",num1+num2)
elif what_do_you_want =="b":
    print("here is your subtruct:",num1-num2)
elif what_do_you_want =="c":
    if num1== 45 and num2 ==3:
        print("here is your multiply:",555)
    else:
        print("here is your multiply:",num1*num2)
elif what_do_you_want== "d":
    if num1==56 and num2==6:
        print("here is your div:",4)
    else:
        print("here is your div:",num1//num2)
else:
    print("wrong input")
