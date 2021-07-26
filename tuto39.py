import math

# f string string formeting

# type one
me = 'maruf'
num = 3
me_num= 'thsi is %s %s'%(me,num)
print(me_num)

# type two
me2 = 'Maruf'
num2 = 4
a = 'this is {} {}'
b = a.format(me2,num2)
print(b)

# f string
c = f'this is {me} {me} {math.cos(12)} '
print(c)