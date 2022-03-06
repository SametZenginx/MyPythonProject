import sqlite3
con = sqlite3.connect("library.db")

cursor = con.cursor()
def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS books (Name TEXT,Author TEXT,BookPublishing TEXT,NumberofPage INT)")
    con.commit() #Saves the change.

def addData():
    cursor.execute("INSERT INTO books VALUES('Istanbul Hatirası','Ahmet Umit','Everest',561)")
    con.commit()

def addDataUser(name,author,bookPublishing,numbersofPage):
    cursor.execute("INSERT INTO books VALUES(?,?,?,?)",(name,author,bookPublishing,numbersofPage))
    con.commit()

def getData():
    cursor.execute("Select * From books")
    aList = cursor.fetchall()
    print("Information the books table: ")
    for i in aList:
        print(i)

def getData2():
    cursor.execute("SELECT Name,Author From books")
    aList = cursor.fetchall()
    print("Information the books name author: ")
    for i in aList:
        print(i)

def getData3(bookPublishing):
    cursor.execute("SELECT * From books where BookPublishing = ?",(bookPublishing,))
    aList = cursor.fetchall()
    for i in aList:
        print(i)
def updateData(oldbookPublishing,newbookPublishing):
    cursor.execute("UPDATE books set BookPublishing = ? where BookPublishing = ?",(newbookPublishing,oldbookPublishing))
    con.commit()

def deleteData(author):
    cursor.execute("DELETE From books where Author = ?",(author,))
    con.commit()


"""
name = input("Name: ")
author = input("Author: ")
bookPublishing = input("Book publishing: ")
numbersofPage = input("Numbers of page: ")
addDataUser(name,author,bookPublishing,numbersofPage)
Input.

-getData()
-getData2()
-getData3("Everest")
-updateData("Dogan kitap","Everest")
getData()
-

"""
getData()
con.close()

