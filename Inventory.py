"""1) INVENTORY MANAGEMENT:
1. Product Management: This module is used to add, update and delete the products.
2. Purchase Management: This module is used to manage the purchase system.
3. Sales Management: This module is used to manage the sale of the products.
4. User Management: This module is used to add/delete the user/staff.
5. Database setup: This module is used to setup the database in the system for the first time."""


"""import sqlite3

v1=sqlite3.connect("product.db")
print("connected")

v2=v1.cursor()

#statement='''create table product(PID Number(5) primary key,Product_Name varchar(30),Price Number(8,3),Quantity Number(4));'''
#v2.execute(statement)
#print("table created")

q1 = '''INSERT INTO product VALUES (?, ?, ?, ?);'''
#v2.execute(q1, (1, "pasta", 20.0, 5))
#v2.execute(q1, (2, "maggi", 15, 10))
#v2.execute(q1, (3, "oats", 50, 6))
#v2.execute(q1, (4, "Cooking oil", 100, 4))
#v2.execute(q1, (5, "wheat", 10, 20))


v1.commit()
#print("record inserted")


def add_product(pid, name, price, quantity):
    v1 = sqlite3.connect("product.db")
    v2 = v1.cursor()
    v2.execute("INSERT INTO products VALUES (?, ?, ?, ?)", (pid, name, price, quantity))
    v1.commit()
    #conn.close()"""

"""import sqlite3

v1=sqlite3.connect("purchase.db")
print("connected")

v2=v1.cursor()
#statement='''create table product(S_NO Number(5) primary key,Product_Name varchar(30),Price Number(8,3),Quantity Number(4) );'''
#v2.execute(statement)
#print("table created")


q1 = '''INSERT INTO product VALUES (?, ?, ?, ?);'''
#v2.execute(q1, (1, "pasta", 20.0, 5))
#v2.execute(q1, (2, "maggi", 15, 10))
#v2.execute(q1, (3, "oats", 50, 6))
#v2.execute(q1, (4, "Cooking oil", 100, 4))
#v2.execute(q1, (5, "wheat", 10, 20))


v1.commit()
print("record inserted")"""



#ST
'''import sqlite3

v1=sqlite3.connect("product.db")

v2=v1.cursor()
print("connected")'''
#statement='''create table sold(S_NO Number(5) primary key,Product_Name varchar(30),Price Number(8,3),Quantity Number(4));'''
#v2.execute(statement)
#print("table created")
#statement='''create table user(UID Number(5) primary key,User_Name varchar(30),Address varchar(50),Phn_no Number(10));'''
#v2.execute(statement)
#print("table created")

#statement='''create table emp(ID Number(5) primary key,emp_Name varchar(30),Address varchar(50),Phn_no Number(10));'''
#v2.execute(statement)
#print("table created")


#Display

def add(v2,v1):
        print("enter following details to add  :")
        PID=int(input("enter a product id :"))
        Product_Name=input("enter a product name :")
        Price=float(input("enter a price :"))
        Quantity=int(input("enter a quantity :"))
        v2.execute("INSERT INTO product VALUES (?, ?, ?, ?)", (PID, Product_Name, Price, Quantity))
        v1.commit()
        print("insterted successfully")
        out=v2.execute('select * from product')
        print("updated product list * ")
        print()
        for i in out:
            print(i)

def addU(v2,v1):
        print("enter following details to add  :")
        UID=int(input("enter a User id :"))
        User_Name=input("enter a User name :")
        address=input("enter a address :")
        phn=int(input("enter a mobile number :"))
        v2.execute("INSERT INTO user VALUES (?, ?, ?, ?)", (UID, User_Name, address, phn))
        v1.commit()
        print("insterted successfully")
        out=v2.execute('select * from user')
        print("user list * ")
        print()
        for i in out:
            print(i)

def addE(v2,v1):
        print("enter following details to add  :")
        ID=int(input("enter a employee id :"))
        emp_Name=input("enter a employee name :")
        address=input("enter a address :")
        phn=int(input("enter a mobile number :"))
        v2.execute("INSERT INTO emp VALUES (?, ?, ?, ?)", (ID, emp_Name, address, phn))
        v1.commit()
        print("insterted successfully")
        out=v2.execute('select * from emp')
        print("employee list * ")
        print()
        for i in out:
            print(i)


def addsold(v2, v1):
        print("Enter following details to add sold product:")
        PID = int(input("Enter a s_no: "))
        Product_Name = input("Enter product name: ")
        Price = float(input("Enter price: "))
        Quantity = int(input("Enter quantity: "))

        # Add to 'sold' table
        v2.execute("INSERT INTO sold VALUES (?, ?, ?, ?)", (PID, Product_Name, Price, Quantity))
        v1.commit()
        print("Inserted into sold table successfully.")

        # Fetch existing quantity from 'product' table
        result = v2.execute("SELECT * FROM product WHERE Product_Name = ?", (Product_Name,)).fetchone()

        if result is None:
            print("Product not found in inventory.")
            return

        current_quantity = result[3]  

        if Quantity > current_quantity:
            print("Error: Sold quantity exceeds available inventory.")
            return

        new_quantity = current_quantity - Quantity

        # Update the product table with reduced quantity
        v2.execute("""
            UPDATE product 
            SET Quantity = ? 
            WHERE Product_Name = ?
        """, (new_quantity, Product_Name))

        v1.commit()
        print("Inventory updated successfully.")

        # Show updated product list
        out = v2.execute("SELECT * FROM product")
        print("Updated Product List:")
        for i in out:
            print(i)

def adds(v2,v1):
        print("enter following details to add  :")
        PID=int(input("enter a product id :"))
        Product_Name=input("enter a product name :")
        Price=float(input("enter a price :"))
        Quantity=int(input("enter a quantity :"))
        v2.execute("INSERT INTO product VALUES (?, ?, ?, ?)", (PID, Product_Name, Price, Quantity))
        v1.commit()
        print("insterted successfully")
        out=v2.execute('select * from product')
        print("updated product list * ")
        print()
        for i in out:
            print(i)


def update(v2,v1):
    print("select the product to update  :")
    Product_Name=input("enter a old product name :")
    result=v2.execute("SELECT * FROM product WHERE Product_Name = ?", (Product_Name,))
    
    if result is None:
        print("Product not found.")
        return

    print("Enter new values :")

    new_name = input(f"New name [{Product_Name}]: or update you have to give the existing name  :") 
    new_price = input("New price: or enter the old price ")
    new_quantity = input("New quantity:  ")

    if new_price:
        new_price = float(new_price)
    else:
        new_price = result[2]

    if new_quantity:
        new_quantity = int(new_quantity)
    else:
        new_quantity = result[3]

    v2.execute("""
        UPDATE product 
        SET Product_Name = ?, Price = ?, Quantity = ?
        WHERE Product_Name = ?
    """, (new_name, new_price, new_quantity, Product_Name))

    v1.commit()
    print("Product updated successfully.")

    out = v2.execute("SELECT * FROM product")
    print("Updated Product List:")
    for i in out:
        print(i)

def updates(v2,v1):
    print("select the product to update  :")
    Product_Name=input("enter a old product name :")
    result=v2.execute("SELECT * FROM product WHERE Product_Name = ?", (Product_Name,))
    
    if result is None:
        print("Product not found.")
        return

    print("Enter new values :")

    new_name = input(f"New name [{Product_Name}]: or update you have to give the existing name  :") 
    new_price = input("New price: or enter the old price ")
    new_quantity = input("New quantity:  ")

    if new_price:
        new_price = float(new_price)
    else:
        new_price = result[2]

    if new_quantity:
        new_quantity = int(new_quantity)
    else:
        new_quantity = result[3]

    v2.execute("""
        UPDATE product 
        SET Product_Name = ?, Price = ?, Quantity = ?
        WHERE Product_Name = ?
    """, (new_name, new_price, new_quantity, Product_Name))

    v1.commit()
    print("Product updated successfully.")

    out = v2.execute("SELECT * FROM product")
    print("Updated Product List:")
    for i in out:
        print(i)


def updatesold(v2,v1):
    print("select the product to update  :")
    Product_Name=input("enter a old product name :")
    result=v2.execute("SELECT * FROM sold WHERE Product_Name = ?", (Product_Name,))
    
    if result is None:
        print("Product not found.")
        return

    print("Enter new values :")

    new_name = input(f"New name [{Product_Name}]: or update you have to give the existing name  :") 
    new_price = input("New price: or enter the old price ")
    new_quantity = input("New quantity:  ")

    if new_price:
        new_price = float(new_price)
    else:
        new_price = result[2]

    if new_quantity:
        new_quantity = int(new_quantity)
    else:
        new_quantity = result[3]

    v2.execute("""
        UPDATE sold 
        SET Product_Name = ?, Price = ?, Quantity = ?
        WHERE Product_Name = ?
    """, (new_name, new_price, new_quantity, Product_Name))

    v1.commit()
    print("Product updated successfully.")

    out = v2.execute("SELECT * FROM sold")
    print("Updated Product List:")
    for i in out:
        print(i)

def delet(v2,v1):
    product_name = input(("enter a product to delet :"))
    result = v2.execute("SELECT * FROM product WHERE Product_Name = ?", (product_name,)).fetchone()
    
    if result is None:
        print("Product not found.")
        return
    
    v2.execute("DELETE FROM product WHERE Product_Name = ?", (product_name,))
    v1.commit()
    print("Product deleted successfully.")

    out = v2.execute("SELECT * FROM product")
    print("Updated Product List:")
    for i in out:
        print(i)


def deletU(v2,v1):
    UID = input(("enter a UserID to delet :"))
    result = v2.execute("SELECT * FROM user WHERE UID = ?", (UID,)).fetchone()
    
    if result is None:
        print("user not found.")
        return
    
    v2.execute("DELETE FROM user WHERE UID = ?", (UID,))
    v1.commit()
    print("USER deleted successfully.")

    out = v2.execute("SELECT * FROM user")
    print("user List:")
    for i in out:
        print(i)

def deletE(v2,v1):
    ID = input(("enter a UserID to delet :"))
    result = v2.execute("SELECT * FROM emp WHERE ID = ?", (ID,)).fetchone()
    
    if result is None:
        print("user not found.")
        return
    
    v2.execute("DELETE FROM emp WHERE ID = ?", (ID,))
    v1.commit()
    print("Employee deleted successfully.")

    out = v2.execute("SELECT * FROM emp")
    print("Employee List:")
    for i in out:
        print(i)
    
def delets(v2,v1):
    product_name = input(("enter a product to delet :"))
    result = v2.execute("SELECT * FROM product WHERE Product_Name = ?", (product_name,)).fetchone()
    
    if result is None:
        print("Product not found.")
        return
    
    v2.execute("DELETE FROM product WHERE Product_Name = ?", (product_name,))
    v1.commit()
    print("Product deleted successfully.")

    out = v2.execute("SELECT * FROM product")
    print("Updated Product List:")
    for i in out:
        print(i)



while True:
    print()
    print()
    print(" Select The Following")
    print("---------------------")
    print()
    print()
    print("1.purchase Management")
    print()
    print("2.Product Management")
    print()
    print("3.Sales Management ")
    print()
    print("4.User Management ")
    print()
    print("5.Exit>>>........")
    print()
    print("-----------------------")
   


    option=input("Select the options  :")

    if option=="2":
       print()
       print("Select 1 to Add the product")
       print()
       print("Select 2 to update the product")
       print()
       print("select 3 to delet the product")
       print()
       select =int(input("select the option :"))
       if select ==1:
           import sqlite3
           v1=sqlite3.connect("product.db")
           v2=v1.cursor()
           product_list=list(v2.execute('select Product_Name from product'))
           pro=[]
           for i in product_list:
               for j in i:
                   pro.append(j)
           print(pro)
           product=input("enter a product :")
           print()
            
           if product in pro:
               print("The product is already exist")
           else:
               add(v2,v1)
       elif select ==2:
           import sqlite3
           v1=sqlite3.connect("product.db")
           v2=v1.cursor()
           product_list=list(v2.execute('select Product_Name from product'))
           pro=[]
           for i in product_list:
               for j in i:
                   pro.append(j)
           out=v2.execute('select * from product')
           print(" product list * ")
           print()
           for i in out:
               print(i)
        
           product=input("enter a product :")
           print()
           if product in pro:
               update(v2,v1)
               
           else:
               print("product is not exist")
       elif select ==3:
           import sqlite3
           v1=sqlite3.connect("product.db")
           v2=v1.cursor()
           product_list=list(v2.execute('select Product_Name from product'))
           pro=[]
           for i in product_list:
               for j in i:
                   pro.append(j)
           out=v2.execute('select * from product')
           print(" product list * ")
           print()
           for i in out:
               print(i)
        
           product=input("check a product to delet:")
           print()
           if product in pro:
               delet(v2,v1)
               
           else:
               print("product is not exist")
           
    elif option=="1":
            print()
            print("Select 1 to Add the product")
            print()
            print("Select 2 to Remove the sold product")
            print()
            
            selected =int(input("select the option :"))
            if selected ==1:
                    import sqlite3
                    v1=sqlite3.connect("purchase.db")
                    v2=v1.cursor()
                    product_list=list(v2.execute('select Product_Name from product'))
                    pro=[]
                    for i in product_list:
                            for j in i:
                                pro.append(j)
                    print(pro)
                    product=input("enter a product :")
                    print()
                    
                    if product in pro:
                        print("The product is already exist")
                    else:
                        adds(v2,v1)

            elif selected ==2:
                    print()
                    print("choose 1. To remove the sold product")
                    print()
                    print("choose 2.To upadate the quantity of existing product")
                    print()
                    choose=int(input("select the choice :"))
                    if choose==1:
                            import sqlite3
                            v1=sqlite3.connect("purchase.db")
                            v2=v1.cursor()
                            product_list=list(v2.execute('select Product_Name from product'))
                            pro=[]
                            for i in product_list:
                                for j in i:
                                   pro.append(j)
                            out=v2.execute('select * from product')
                            print(" product list * ")
                            print()
                            for i in out:
                                print(i)
                        
                            product=input("check a product to delet:")
                            print()
                            if product in pro:
                                delets(v2,v1)
                               
                            else:
                                print("product is not exist")
                    elif choose==2:
                            import sqlite3
                            v1=sqlite3.connect("purchase.db")
                            v2=v1.cursor()
                            product_list=list(v2.execute('select Product_Name from product'))
                            pro=[]
                            for i in product_list:
                                for j in i:
                                    pro.append(j)
                            out=v2.execute('select * from product')
                            print(" product list * ")
                            print()
                            for i in out:
                                print(i)
                        
                            product=input("enter a product :")
                            print()
                            if product in pro:
                                updates(v2,v1)
                               
                            else:
                                print("product is not exist")
                            
                    

            
    elif option =="3":
            print()
            print("Select the product to Add to sold")
            import sqlite3
            v1=sqlite3.connect("product.db")
            v2=v1.cursor()
            product_list=list(v2.execute('select Product_Name from sold'))
            pro=[]
            for i in product_list:
                for j in i:
                    pro.append(j)
            print(pro)
            product=input("enter a product :")
            print()
            
            if product in pro:
               updatesold(v2,v1)
            else:
                addsold(v2,v1)




                
    elif option == "4":
            print()
            print("Select 1: For Users  ")
            print()
            print("Select 2: For Staffs  ")
            print()
            sel=int(input("select the preferences :"))
            if sel ==1:
                    print()
                    print("choose 1. To add user")
                    print()
                    print("choose 2.To delet user")
                    print()
                    cho=int(input("select the option :"))
                    if cho==1:
                            import sqlite3
                            v1=sqlite3.connect("product.db")
                            v2=v1.cursor()
                            user_list=list(v2.execute('select User_Name from user'))
                            pro=[]
                            for i in user_list:
                                for j in i:
                                    pro.append(j)
                            print(pro)
                            user_name=input("enter a name :")
                            print()
                            if user_name:
                                addU(v2,v1)
                            else:
                                    print("add user name ")
                    elif cho==2:
                            import sqlite3
                            v1=sqlite3.connect("product.db")
                            v2=v1.cursor()
                            user_list=list(v2.execute('select UID from user'))
                            pro=[]
                            
                            for i in user_list:
                                for j in i:
                                    pro.append(j)
                            print("pro",pro)
                            out=v2.execute('select * from user')
                            print(" user list * ")
                            print()
                            for i in out:
                                print(i)
                        
                            UID=int(input("enter user ID to delet "))
                            print()
                            if UID in pro:
                                deletU(v2,v1)
                               
                            else:
                                print("User ID is not exist")
                            
                            
            elif sel ==2:
                    print()
                    print("choose 1. To add employee")
                    print()
                    print("choose 2.To delet employee")
                    print()
                    chos=int(input("select the option :"))
                    if chos==1:
                            import sqlite3
                            v1=sqlite3.connect("product.db")
                            v2=v1.cursor()
                            emp_list=list(v2.execute('select emp_Name from emp'))
                            pro=[]
                            for i in emp_list:
                                for j in i:
                                    pro.append(j)
                            print(pro)
                            emp_name=input("enter a name :")
                            print()
                            if emp_name:
                                addE(v2,v1)
                            else:
                                    print("add employee name ")
                    elif chos==2:
                            import sqlite3
                            v1=sqlite3.connect("product.db")
                            v2=v1.cursor()
                            emp_list=list(v2.execute('select ID from emp'))
                            pro=[]
                            
                            for i in emp_list:
                                for j in i:
                                    pro.append(j)
                            print("pro",pro)
                            out=v2.execute('select * from emp')
                            print(" employee list * ")
                            print()
                            for i in out:
                                print(i)
                        
                            UID=int(input("enter user ID to delet "))
                            print()
                            if UID in pro:
                                deletE(v2,v1)
                               
                            else:
                                print("Employee ID is not exist")
                

                    

 
            

    elif option=="5":
        print("exiting")
        break
    else:
        print("invalid option")

  

   
        
        
    






