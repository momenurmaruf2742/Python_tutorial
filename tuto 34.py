# recursion and itrative logic

def factorial_itrative(n):
    """
    :parameter n: integer
    :return: n*n-1 * n-2.......1
    """
    fac = 1
    for i in range(n):
        fac = fac*(i+1)
    return fac



def factorial_recursive(n):
    """
    :parameter n: integer
    :return: n*n-1 * n-2.......1
    """
    if n == 1:
        return 1
    else:
        pass
    return n*factorial_recursive(n-1)

# logic
# if n = 5
# # 5*factorial_recursive(5-1)
# # 5*4*factorial_recursive(4-1)
# # 5*4*3*factorial_recursive(3-1)
# # 5*4*3*2*factorial_recursive(2-1)
# # 5*4*3*2*1=120
number = int(input("Enter the number"))
print("recursive",factorial_recursive(number))
print("itrative",factorial_itrative(number))

# ###### quiz fibonacci serise
# logic
# 0 1 1 2 3 5 8 13 21 .......adding previous 2 value

def fibonacci(n):
    if n == 1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
nm = int(input("inter fibonacci serese"))
print(fibonacci(nm))
# onother fibonacci
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
