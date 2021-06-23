# reading file in python
""""
 "r" for read and its defult
 "w" for write
 "x" for create file if not exist
 "a" append add in the last in any file
 "t" text file its also default
 "b" binarry mode
 "+" read and write"""





f = open("maruf.txt","rt")
#content = f.read()#here is 23 charecter readable

# print(f.readline())#print line by line but extra line added
# print(f.readline())
# print(f.readlines()) # read in list
# for li in f:
#     print(li,end="") #print file for line by line
# for line in content:# print charecter by charecter
#     print(line)
# print(content) #print hole content
f.close()
