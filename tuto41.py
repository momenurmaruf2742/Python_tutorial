#args and kwagrs
#
# def function_name_print(a,b,c,d,e,f):
#     print(a,b,c,d,e,f)
# function_name_print('maruf','opu','shahin','tarikul','ashif','noman')
#

def funargs(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

mar = ['maruf','opu','shahin','tarikul','ashif','noman','the programmer']
nm = 'this is normal argument'
kw = {"harry":"mentor","sivam":"trainer"}
funargs(nm,*mar,**kw)
