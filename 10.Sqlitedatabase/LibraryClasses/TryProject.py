from Library import *
import time


print("""
************************************************
Welcome to the Library Proggramming...

Operations:

1- Show the books

2- Book inqury

3- Add book

4- Delete book

5- +1 the edition year

Please 'q'. if you want the exiting in the program.
************************************************
""")

library = Library()


while True:
    operation = input("Type to action you want(number): ")
    if operation == "q":
        print("Exiting the program... Please wait.")
        time.sleep(5)
        break
    elif operation == "1":
        library.showBooks()

    elif operation == "2":
        name = input("Which books do you want?: ")
        print("The book is being questioned...")

        time.sleep(2)

        library.queryBook(name)

    elif operation == "3":
        
        name = input("Name: ")
        author = input("Author: ")
        publish = input("Publisher: ")
        types = input("Type: ")
        yearOfPriting = int(input("Year of Priting: "))
        pageNumber = int(input("Page number: "))

        newBook = Book(name,author,publish,types,yearOfPriting,pageNumber)

        print("Add the books. ")
        time.sleep(2)

        library.addBook(newBook)

        print("Added the book.")
        
        
    elif operation == "4":
        name = input("Which books you want to delete?: ")

        answer = input("Are you sure?(Y)(N): ")

        if answer == "Y":
            print("The book is deleting...")
            time.sleep(2)
            library.deleteBook(name)

        elif answer == "N":
            print("The book is not deleting.")
        else:
            print("Please enter the correct value.")
    elif operation == "5":
        name = input("Which book do you want to priting year increase?: ")
        time.sleep(2)
        library.changingEditionyear(name)
        print("Increased the year of print...")
    else:
        print("Invalid value.")
