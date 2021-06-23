# scope global variables and global keyword

l = 10  #global
def function1(n):
    # l = 5
    global l
    m = 8       ## global variables can changes on this global keyword
    l = l + 30
    print(l,m)
    print(n,"I have printed")
function1("this is maruf")
print(l)


x = 88
def maruf ():
    x = 32
    def harry():
        global x
        x = 80
    print("before calling harry()",x)

    print("after calling rohan()",x)
maruf()