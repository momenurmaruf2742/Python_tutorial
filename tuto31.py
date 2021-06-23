# using with block to open python file

with open("maruf.txt") as f:
    a = f.read(6)
    print(a)

# f = open("maruf.txt")
# print(f.readlines())
# print(f.readline())
#
#           if using with block than we don`t need to use opeen and cloose function for pointer
#
#
# f.close()