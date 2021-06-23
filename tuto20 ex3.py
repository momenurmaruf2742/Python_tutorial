#### tuto 19 excercise 2 solved
n = 20
number_of_guessess = 1
print("only 9 time you can try")
while (number_of_guessess<=9):
    guess_number = int(input("enter your guessess number \n"))

    if guess_number>n:
        print("please leass then the number :",guess_number)
    elif guess_number<n:
        print("please enter the bigger number :",guess_number)
    else:
        print("you won the gussing game the xnumber is:",guess_number)
        break

    print(9-number_of_guessess,"you have left")
    number_of_guessess = number_of_guessess +1
if number_of_guessess>9:
    print("over")