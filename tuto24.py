### try except exception handeling
num1 = input("enter num1:")
num2 = input("enter num2:")
try:
    print(int(num1)+int(num2))
except Exception as e:
    print(e)


print("print this line")
