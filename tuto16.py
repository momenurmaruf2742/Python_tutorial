# for loops
list1 = ["Harry","Larry","Carry","Marry"]
for maruf in list1:
    print(maruf)

list = [["maruf",24],["momenur",23],["islam",1]]
dict1= dict(list)
print(dict1)



for maruf,mar in list:
    print(maruf,"khabe",mar)


list2 = [int ,float,"maruf",12,22,112,21,223,6,7,8,5]
for item in list2:
    if str(item).isnumeric() and item>=6:
        print(item)
