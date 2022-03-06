import sqlite3

class Book():

    def __init__(self,name,author,bookPublishing,type,yearofPriting,numberPage):
        self.name = name
        self.author = author
        self.bookPublishing = bookPublishing
        self.type = type
        self.yearofPriting = yearofPriting
        self.numberPage = numberPage
    
    def __str__(self):

        return "----------------------------\n\nBook's Name: {}\nBook's Author: {}\nBook's Publisher of the book: {}\nBook type: {}\nBook year of priting: {}\nBook number of page: {}\n\n----------------------------\n\n".format(self.name,self.author,self.bookPublishing,self.type,self.yearofPriting,self.numberPage)

    
class Library():

    def __init__(self):

        self.createConnect()
    
    def createConnect(self):
        self.connection = sqlite3.connect("library.db")

        self.cursor = self.connection.cursor()

        query = "CREATE Table IF NOT EXISTS Books(Name TEXT,Author TEXT,BookPublishing TEXT,Type TEXT,YearOfPriting INT,NumberPage INT)"

        self.cursor.execute(query)

        self.connection.commit()

    def disconnect(self):
        self.connection.close()

    def showBooks(self):

        query = "SELECT * From Books"

        self.cursor.execute(query)

        books = self.cursor.fetchall()

        if len(books) == 0:
            print("There are no books in the library.")
        else:
            for i in books:
                
                book = Book(i[0],i[1],i[2],i[3],i[4],i[5])
                print(book)
    
    def queryBook(self,name):

        query = "SELECT * From Books where Name = ?"

        self.cursor.execute(query,(name,))

        books = self.cursor.fetchall()

        if len(books) == 0:
            print("There is no such book.")
        else:
            book = Book(books[0][0],books[0][1],books[0][2],books[0][3],books[0][4],books[0][5])

            print(book)
    
    def deleteBook(self,name):

        query = "DELETE From Books where Name = ?"

        self.cursor.execute(query,(name,))

        self.connection.commit()
    
    def addBook(self,book):

        query = "Insert into Books Values(?,?,?,?,?,?)"

        self.cursor.execute(query,(book.name,book.author,book.bookPublishing,book.type,book.yearofPriting,book.numberPage))

        self.connection.commit()

    def changingEditionyear(self,name):

        query = "SELECT * From Books where name = ?"

        self.cursor.execute(query,(name,))


        books = self.cursor.fetchall()

        if len(books) == 0:
            print("There is no such book.")
        else:
            prittingYear = books[0][4]

            prittingYear += 1

            query2 = "UPDATE Books set YearOfPritting = ? where Name = ?"

            self.cursor.execute(query2,(prittingYear,name))

            self.connection.commit()









            



















    