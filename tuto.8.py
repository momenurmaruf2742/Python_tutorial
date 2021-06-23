mystr = "Maruf is a bad boy"
print(mystr) #genaral printing
print(len(mystr)) #showing length of this string

#slicing
print(mystr[0:18]) #slicing printing

print(mystr[0:18:1])##advanced slicing last colon don`t skip coz 1 by 1 charecter
print(mystr[0:19:2])##advance slicing last colon skiping one charecter

print(mystr[-7:-1])#last theke - kore kore indexing korbe
print(mystr[::-1])#last a -1 dile string ke ulta print korbe
print(mystr[::-2])#string ulta kore akta kore skip

#string function

print(mystr.isalnum())#if no space in the string than it`s can true lnum means alphanumeric number
print(mystr.isalpha())#if the cherecter is alphabet
print(mystr.endswith("boy"))#if last cherecter ends with boy
print(mystr.count("M"))#M is counting how many time is comming on this string
print(mystr.capitalize())#if frist cherecter is small
print(mystr.find("is"))#
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("bad","good"))

"""
google search for string function
"""