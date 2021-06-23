# functions and docstring
a = 10
b = 7
c = sum((a,b)) #built in function
print(c)

## creating function

def func1(a,b):
    print("this is functions one",a+b)

def func2(a,b):
    """This is the function for calculating avarage of two numbers"""
    ave = (a+b)/2
    return ave

v = func2(5,7)
print(v)
print(func2.__doc__)