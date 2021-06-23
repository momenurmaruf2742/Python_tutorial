#break and continue

i = 0

# how to break loop
while (True):
    if i+1<5:
        i = i +1
        continue
    print(i+1,end=" ")
    if i==50:

        break
    i = i +1
#input many time while input is greter then 100 and print it to "congratulations you in put 100 +"
while (True):
    num = int(input(" enter your number \n"))
    if num <=100:
        print("try again")

        continue
    print("congratulations you input 100 + is :",num)
    if num>100:
        break


#same problems others solutions
while(True):
    np = int(input("\n enter your number"))
    if np>100:
        print("congratulation")
        break
    else:
        print("try")
        continue
