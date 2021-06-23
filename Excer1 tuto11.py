# excercise creat a durectiry and take input from user and return the meaning of the word from the dictionary

d1 = {
    "safe":"without enjure",
    "mutable":"can change",
    "immutable":"can`t change",
    "Ramadan":"it`s a month of arabic that better from the 1000 month"

}
search = input("Enter your search with 'safe','mutable','immutable','Ramadan'\n")
print("Here is your result of search is :",d1[search])