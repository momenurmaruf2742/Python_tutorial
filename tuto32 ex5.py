# excercise for helth management system
# 3 clints -Harry,Rohan and Hammad
#total 6 file
import datetime

def gettime():
    return datetime.datetime.now()
def add_item(clint):
    if clint=="1":
        add_what = input("1 for excersise 2 for food: ")

        if add_what =="1":
            item_name = input("Whats your choice: ")
            with open("Harryexer.txt","a") as h:
                add =["[",gettime(),"]",item_name,"\n"]
                for item in add:
                    h.write("%s"% item)
            print("Sucessfully Addedd")

        elif add_what =="2":
            item_name = input("Whats your choice: ")
            with open("Harryfood.txt","a") as h:
                add =["[",gettime(),"]",item_name,"\n"]
                for item in add:
                    h.write("%s"% item)
            print("Sucessfully Addedd")

    elif clint=="2":
        add_what = input("1 for excersise 2 for food: ")

        if add_what =="1":
            item_name = input("Whats your choice: ")
            with open("rohan.txt","a") as h:
                add =["[",gettime(),"]",item_name,"\n"]
                for item in add:
                    h.write("%s"% item)
            print("Sucessfully Addedd")

        elif add_what =="2":
            item_name = input("Whats your choice: ")
            with open("rohanfood.txt","a") as h:
                add =["[",gettime(),"]",item_name,"\n"]
                for item in add:
                    h.write("%s"% item)
            print("Sucessfully Addedd")

    elif clint=="3":
        add_what = input("1 for excersise 2 for food: ")

        if add_what =="1":
            item_name = input("Whats your choice: ")
            with open("hammad.txt","a") as h:
                add =["[",gettime(),"]",item_name,"\n"]
                for item in add:
                    h.write("%s"% item)
            print("Sucessfully Addedd")

        elif add_what =="2":
            item_name = input("Whats your choice: ")
            with open("hammadfood.txt","a") as h:
                add =["[",gettime(),"]",item_name,"\n"]
                for item in add:
                    h.write("%s"% item)
            print("Sucessfully Addedd")


def retrive(clint):

    if clint=="1":
        add_what = input("1 for excersise 2 for food: ")
        if add_what =="1":
            try:
                with open("Harryexer.txt","r") as h:
                    b = h.readlines()
                    print("\n\n")
                    for i in b:
                        print(i)
            except:
                print("item not in the list add some item ")

        elif add_what =="2":
            try:
                with open("Harryfood.txt","r") as h:
                    b = h.readlines()
                    print("\n\n")
                    for i in b:
                        print(i)
            except:
                print("item not in the list add some item ")

    elif clint=="2":
        add_what = input("1 for excersise 2 for food: ")
        if add_what =="1":
            try:
                with open("rohan.txt","r") as h:
                    b = h.readlines()
                    print("\n\n")
                    for i in b:
                        print(i)
            except:
                print("item not in the list add some item ")

        elif add_what =="2":
            try:
                with open("rohanfood.txt","r") as h:
                    b = h.readlines()
                    print("\n\n")
                    for i in b:
                        print(i)
            except:
                print("item not in the list add some item ")

    if clint=="3":
        add_what = input("1 for excersise 2 for food: ")
        if add_what =="1":
            try:
                with open("hammad.txt","r") as h:
                    b = h.readlines()
                    print("\n\n")
                    for i in b:
                        print(i)
            except:
                print("item not in the list add some item ")

        elif add_what =="2":
            try:
                with open("hammadfood.txt","r") as h:
                    b = h.readlines()
                    print("\n\n")
                    for i in b:
                        print(i)
            except:
                print("item not in the list add some item ")




add_or_retrive = input("1 for add 2 for retrive: ")

clint = input("1 for Harry,2 for Rohan,3 for Hammad: ")
if add_or_retrive =="1":
    add_item(clint)
elif add_or_retrive =="2":
    retrive(clint)


