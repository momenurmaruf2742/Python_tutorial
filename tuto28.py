# writing and appending to a file  and tuto 27 is solving excersise 3

# f = open("maruf2.txt","w") # file open in write mode
# c = f.write("maruf is looser")
# print(c) # how many charecter in this writing file
# f.close()

# handle read and write

a = open("maruf2.txt","r+")# open file in read and write mode

print(a.read())
a.write("\nloser")
a.close()