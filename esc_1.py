import mysql.connector as msc
import os

mydb = msc.connect(host="localhost",
                   user="root",
                   password=os.getenv("MYSQL_PASSWORD"),
                   allow_local_infile=True
                   )
crs = mydb.cursor()
qry01 = "CREATE DATABASE if not exists escapism"
crs.execute(qry01)
qry02 = "USE escapism"
crs.execute(qry02)
qry03 = ("CREATE TABLE IF NOT EXISTS book (Book_Number int(10) primary key,Book_Title varchar(25),Author_Name varchar("
         "25),Start_Date DATE,End_Date DATE,Rating int(6),Review varchar)")
crs.execute(qry03)

mydb.commit()
crs.close()


def menu():
    print("""

                                       +====================================+  
                                       |      ****  MAIN MENU  ****         |
                                       +====================================+
                                       |                                    |      
                                       |  1. Add Your Book                  |
                                       |  2. Your Shelf                     |   
                                       |  3. Boo Info                       |
                                       |  0. Exit                           |                                     
                                       |                                    |
                                       |                                    |         
                                       |                                    |
                                       +====================================+
                                  """)
    ch = int(input("ENTER YOUR OPTION: "))
    if ch == 1:
        print(" ")
        add()

    elif ch == 2:
        print(" ")
        shelf()

    elif ch == 3:
        print(" ")
        info()

    elif ch == 0:
        exit()

    else:
        print(" ")
        print("~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")
    return


def add():
    global Rating, Review
    import mysql.connector as msc
    from datetime import datetime
    mydb = msc.connect(host="localhost",
                       user="root",
                       password="sreeshya@2004",
                       database="escapism")
    crs = mydb.cursor()
    mydb.autocommit = True
    Book_Number = Book_Number.set(Book_Number.get() + 1)
    Book_Title = input("Enter the Book Title: ")
    Author_Name = input("Enter the Author: ")
    Start_Date = input("Enter the Start Date(DD/MM/YYYY): ")
    d1 = datetime.strptime(Start_Date, "%d/%m/%Y")
    End_Date = input("Enter the End Date(DD/MM/YYYY): ")
    d2 = datetime.strptime(End_Date, "%d/%m/%Y")
    # d1=input("Enter the Start Date(DD/MM/YY): ")
    # d2=input("Enter the End Date(DD/MM/YY): ")
    while True:
        rate = input("Do you want to Rate the Book?? (y/n): ")
        if rate == "y":
            while True:
                Rating = int(input("Enter your Rating (0-5): "))
                if Rating < 0 or Rating > 5:
                    print("Invalid choice")
                else:
                    break
            break
        elif rate == "n":
            break
        else:
            print("Invalid choice")

    while True:
        rev = input("Do you want to Review the Book?? (y/n): ")
        if rev == "y":
            Review = input("Enter the Review: ")
            break
        elif rate == "n":
            break
        else:
            print("Invalid choice")
    s1 = "INSERT INTO  book VALUES(%s,%s,%s,%s,%s,%s,%s)"
    data = (Book_Number, Book_Title, Author_Name, Start_Date, End_Date, Rating, Review)
    crs.execute(s1, data)

    mydb.commit()
    crs.close()


def shelf():
    print(" ")


def info():
    print(" ")
