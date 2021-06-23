#dictionary is nothing but key value pairs

d1 = {"Maruf":"burger",
      "Rohan":"Fish",
      "Harry":"roti",
      "Subam": {"B":"maggie","L":"roti","D":"chicken"}} #this is dictionary and another dictionary in this

print(d1["Subam"]["B"]) #they can be nested #dictionary nested #list nested #tuple

d1["Ankit"]="Junck food"  #self update
print(d1)
del d1["Ankit"]  #delete perticuler dictionary

print(d1)

# dictionary function

d2 = d1.copy()#copy frist then assign it on d2
del d2["Maruf"]

print(d2)
print(d2.get("Rohan"))#values of rohan
d2.update({"Leena":"Tofee"}) #update
print(d1.keys())#key
print(d1.values())#value
print(d1.items())#items
print(d2)

#google search for dictionary function for python
