# seek tell more in python
f = open("maruf2.txt")
# print(f.read())#read for hole file
print(f.readline())
f.seek(12)#reset after 12 cherecter
print(f.readline())
print(f.tell())#this tell function for tell about what is the cherecter

f.close()