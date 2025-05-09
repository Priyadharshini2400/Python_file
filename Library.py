#Database creation
#import sqlite3
#v1=sqlite3.connect("library.db")
#v2=v1.cursor()
#print("connected")
#statement="""create table BookRecords(Bno TEXT primary key,Author varchar(20),Title varchar(20),Quantity number(10));"""
#statement1="""create table Members(MID TEXT primary key,Name varchar(20),Role varchar(20),Contact number(10));"""
#statement2="""create table Issue(IssueID TEXT primary key,Bno TEXT,MID TEXT,Issue_date TEXT, Due_date TEXT,FOREIGN KEY(Bno) REFERENCES bookRecord(Bno),FOREIGN KEY (MID) REFERENCES Members(MID));"""
#v2.execute(statement2)
#print("table created")




#Module for Book
def addB():
    print()
    print("Enter your Book Details")
    import sqlite3
    v1=sqlite3.connect("library.db")
    v2=v1.cursor()
    bno=input("Enter Book Code : ")
    author=input("Enter Author Name : ")
    title=input("Enter Title : ")
    quantity=int(input("Enter Quantity :"))
    v2.execute('''Insert into BookRecords values(?,?,?,?)''',(bno,author,title,quantity))
    v1.commit()
    print()
    print("Books Inserted successfully")
    print()
    res=v2.execute('select * from BookRecords')
    for i in res:
        print(i)

def updateB():
    print()
    import sqlite3
    v1=sqlite3.connect("library.db")
    v2=v1.cursor()
    bno =input("Enter Book Code to update : ")
    out=v2.execute('select * from BookRecords where Bno=?',(bno,))
    record = out.fetchone()
    print(record)
    author=input("Enter Author Name : or leave as blank  ") or record[1]
    title=input("Enter Title : or leave as blank ") or record[2]
    quantity_input = input("Enter new Quantity (leave blank to keep unchanged): ")
    quantity = int(quantity_input) if quantity_input else record[3]
    v2.execute('''update BookRecords set Author=?,Title =?,Quantity =? where Bno=?''',(author,title,quantity,bno))
    v1.commit()
    print("updated successfully")
    print()
    res=v2.execute('select * from BookRecords')
    for i in res:
        print(i)

def deletB():
    print()
    import sqlite3
    v1=sqlite3.connect("library.db")
    v2=v1.cursor()
    bno =input("Enter Book Code to Delete : ")
    v2.execute('DELETE FROM BookRecords where Bno=?',(bno,))
    v1.commit()
    print("Removed successfully!")
    print()
    res=v2.execute('select * from BookRecords')
    for i in res:
        print(i)


#Member Module

def addM():
    print()
    print("Enter Member Details")
    import sqlite3
    v1=sqlite3.connect("library.db")
    v2=v1.cursor()
    mid=input("Enter Member ID : ")
    name=input("Enter  Name : ")
    role=input("Enter role : ")
    cont=int(input("Enter Contact no. :"))
    v2.execute('''Insert into Members values(?,?,?,?)''',(mid,name,role,cont))
    v1.commit()
    print()
    print("Members added successfully")
    print()
    res=v2.execute('select * from Members')
    for i in res:
        print(i)

def updateM():
    print()
    import sqlite3
    v1=sqlite3.connect("library.db")
    v2=v1.cursor()
    mid =input("Enter Member ID to update : ")
    out=v2.execute('select * from Members where MID=?',(mid,))
    record = out.fetchone()
    print(record)
    name=input("Enter  Name : or leave as blank  ") or record[1]
    role=input("Enter role : or leave as blank ") or record[2]
    con = input("Enter new Contact no. (leave blank to keep unchanged): ")
    co = int(con) if con else record[3]
    v2.execute('''update Members set Name=?,Role =?,contact =? where MID=?''',(name,role,co,mid))
    v1.commit()
    print("updated successfully")
    print()
    res=v2.execute('select * from Members')
    for i in res:
        print(i)

def deletM():
    print()
    import sqlite3
    v1=sqlite3.connect("library.db")
    v2=v1.cursor()
    mid =input("Enter Member ID to Delete : ")
    v2.execute('DELETE FROM Members where MID=?',(mid,))
    v1.commit()
    print("Removed successfully!")
    print()
    res=v2.execute('select * from Members')
    for i in res:
        print(i)



#Issue Module


def addI():
    print()
    print("Enter Issue Details")
    import sqlite3
    v1=sqlite3.connect("library.db")
    v2=v1.cursor()
    issue=input("Enter Issue ID : ")
    bno=input("Enter Book code : ")
    mid=input("Enter  Member ID : ")
    issue_date=input("Enter issue date : ")
    due=input("Enter Due date : ")
    v2.execute('''Insert into Issue values(?,?,?,?,?)''',(issue,bno,mid,issue_date,due))
    v2.execute("UPDATE BookRecords SET Quantity = Quantity - 1 WHERE Bno = ?", (bno,))
    v1.commit()
    print()
    print(" added successfully")
    print()
    res=v2.execute('select * from Issue')
    for i in res:
        print(i)

def return_book():
    import sqlite3
    v1=sqlite3.connect("library.db")
    v2=v1.cursor()
    bno = input("Enter Book Code: ")
    mid = input("Enter Member ID: ")
    v2.execute("DELETE FROM issue WHERE Bno = ? AND MID = ?", (bno, mid))
    v2.execute("UPDATE BookRecords SET Quantity = Quantity + 1 WHERE Bno = ?", (bno,))
    v1.commit()
    res=v2.execute('select * from Issue')
    for i in res:
        print(i)
    print("Book returned.")






    
    
    
    
    
        


    
              
    
    
    



#Library Management System
print()
print()
print("*****Library Management System*****")
print()
print()
print("Welcome To ABC school...............")
print()
print()


while True:
    print()
    print("select :1  For Book Details ")
    print()
    print("select :2  For Member Details ")
    print()
    print("select :3  For Issue Details ")
    print()
    print("select :4  To Exit ")
    print()
    select=int(input("Enter your selected option : "))
    
    if select ==1:
        #Book Details
        print()
        print("*****Book Details*****")
        print()
        print("select :1 To Add Books")
        print()
        print("select :2 To Update Book")
        print()
        print("select :3 To Delete Book")
        print()
        option=int(input("Enter your option  :  "))
        print()
        if option==1:
            print()
            addB()
        elif option ==2:
            print()
            updateB()
        elif option==3:
            print()
            deletB()
            
        else:
            print("Invalid!")
            
            
        
        
        
    elif select ==2:
        #Member Details
        print()
        print("*****Member Details*****")
        print()
        print("select :1 To Add Member")
        print()
        print("select :2 To Update Member")
        print()
        print("select :3 To Delete Member")
        print()
        options=int(input("Enter your option  :  "))
        print()
        if options==1:
            print()
            addM()
        elif options ==2:
            print()
            updateM()
        elif options==3:
            print()
            deletM()
        else:
            print("Invalid!")
        
    elif select ==3:
        print()
        print("*****Issue Details*****")
        print()
        print("select :1 To ADD Issue list")
        print()
        print("select :2 To Remove Issue list")
        print()
        choice=int(input("Enter your option  :  "))
        print()
        if choice==1:
            print()
            import sqlite3
            v1=sqlite3.connect("library.db")
            v2=v1.cursor()
            bno =input("Enter Book Code to check Availability : ")
            out=v2.execute('select * from BookRecords where Bno=?',(bno,))
            record = out.fetchone()
            if record:
                if int(record[3]) > 0:
                    print(record)
                    addI()
                else:
                    print("Book is currently not available (quantity = 0).")
            else:
                print("Book not found.")
            
        elif choice ==2:
            print()
            return_book()
        else:
            print("Invalid!")
        
    elif select ==4:
        print("Exiting.....")
        break
    else:
        print("Enter valid option")
    
    
