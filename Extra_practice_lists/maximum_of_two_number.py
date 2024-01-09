# finding max number using if else statement
def max_number_if_else(numer1,number2):
    if numer1 > number2:
        return numer1
    return number2

print(max_number_if_else(100,21))

# using lamda functions
maximum = lambda a,b:a if a > b else b
print(maximum(a=3,b=4))