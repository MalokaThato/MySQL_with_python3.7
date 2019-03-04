#Import the correct libreries and connect to the MySql
import MySQLdb

db = MySQLdb.connect("localhost", "root", "Umuzi123", "Umuzi")

cursor = db.cursor()

#Start checking if the required tables exist and if not create themself.


cursor.execute("""CREATE TABLE IF NOT EXISTS Customers (
         Customer_id  int NOT NULL PRIMARY KEY AUTO_INCREMENT,
         FirstName VARCHAR(50) NOT NULL,
         LastName VARCHAR(50) NOT NULL,
         Gender  ENUM('F', 'M') DEFAULT 'M',
         Address VARCHAR(150) NOT NULL, Phone INT(10) NOT NULL, Email VARCHAR(50) NOT NULL, City VARCHAR(100) NOT NULL, Country VARCHAR(100) NOT NULL )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Employees (
         Employee_id  int NOT NULL PRIMARY KEY AUTO_INCREMENT,
         FirstName VARCHAR(50) NOT NULL,
         LastName VARCHAR(50) NOT NULL,
         Email VARCHAR(50) NOT NULL, Job_Title VARCHAR(100) NOT NULL)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Products (
         Product_id  int NOT NULL PRIMARY KEY AUTO_INCREMENT,
         ProductName VARCHAR(150) NOT NULL,
         Description VARCHAR(250) NOT NULL,
         BuyPrice DECIMAL NOT NULL )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Payments (
         Customer_id int NOT NULL,
         PaymentDate DATETIME NOT NULL,
         Amount DECIMAL(5,2) NOT NULL,
         FOREIGN KEY CustomerId (Customer_id) REFERENCES Customers(Customer_id) ON DELETE CASCADE ON UPDATE CASCADE) ENGINE=InnoDB""")


cursor.execute("""CREATE TABLE IF NOT EXISTS Orders (
         Orderid int NOT NULL PRIMARY KEY AUTO_INCREMENT,
         OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
         RequiredDate DATE NOT NULL,
         ShippedDate DATE NOT NULL,
         Status VARCHAR(100) NOT NULL )""")

cursor.close()

#This function will get the values to insert into a table
def value_inserter(table):
    db = MySQLdb.connect("localhost", "root", "Umuzi123", "Umuzi")

    cursor = db.cursor()


    while True:

        if table.upper() == "C":
            first_name = input("Enter Customer first name: ")
            last_name = input("Enter Customer last name: ")
            gender = input("Enter Customer gender: ")
            address = input("Enter Customer address: ")
            phone = int(input("Enter Customer phone: "))
            email = input("Enter Customer email: ")
            city = input("Enter Customer city: ")
            country = input("Enter Customers country: ")

            cursor.execute("INSERT INTO Customers(FirstName, LastName, Gender, Address, Phone, Email, City, Country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (first_name, last_name, gender, address, phone, email, city, country,))

            db.commit()

        elif table.upper() == "E":
            first_name = input("Enter Employees first name: ")
            last_name = input("Enter Employees last name: ")
            email = input("Enter Employees email: ")
            job_title = input("Enter Employees job titile: ")

            cursor.execute("INSERT INTO Employees( FirstName, LastName, Email, Job_Title) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, job_title))

            db.commit()

        elif table.upper() == "P":
            product_name = input("Enter the products name: ")
            product_des = input("Enter the products description: ")
            product_price = input("Enter the products price: ")


            cursor.execute("INSERT INTO Products( ProductName, Description, BuyPrice) VALUES (%s, %s, %s)", (product_name, product_des, product_price))

            db.commit()

        elif table.upper() == "O":
            print("When entering the date make sure to use this formart: yyyy-mm-dd hh:mm:ss")
            order_date = input("Enter the order date: ")
            required_date = input("Enter the required date: : ")
            shipped_date = input("Enter the shipped date: : ")
            status = input("Is the order shipped?: ")


            cursor.execute("INSERT INTO Orders( OrderDate, RequiredDate, ShippedDate, Status) VALUES (%s, %s, %s, %s)", (order_date, required_date, shipped_date,status ))

            db.commit()


        elif table.upper() == "PAY":
            print("When entering the date make sure to use this formart: yyyy-mm-dd hh:mm:ss")
            customer_id = input("Enter the Customer ID: ")
            paymentdate = input("Enter the payment date: ")
            amount = input("Enter the amount: : ")



            cursor.execute("INSERT INTO Payments( Customer_id, PaymentDate, Amount) VALUES (%s, %s, %s)", (customer_id, paymentdate, amount))

            db.commit()


        elif table == "0":
            break

        table = input("""\nEnter the number 0 to exit \n
            Enter anything besides 0 to continue: \n
            To insert values into Customer table, enter: C \n
            To insert values into Employees table, enter: E \n
            To insert values into Products table, enter: P \n
            To Enter a payent enter: Pay \n
            To insert values into Orders table, enter the letter: O \n
            Enter selection: """)


    cursor.close()


while True:
    exit_loop = input("""
To insert values into Customer table, enter: C \n
To insert values into Employees table, enter: E \n
To insert values into Products table, enter: P \n
To insert values into Orders table, enter the letter: O \n
To Enter a payent enter: Pay \n
Alternatively to exit Enter the number: 0 \n
Enter selection: """)


    if exit_loop == "0":
        break

    elif exit_loop.upper() == "C":
        #call the function that handles entering info into the customer tables
        value_inserter(exit_loop)

    elif exit_loop.upper() == "E":
        #call the function that handles entering info into the employee tables
        value_inserter(exit_loop)

    elif exit_loop.upper() == "P":
        #call the function that handles entring info into the Product table
        value_inserter(exit_loop)

    elif exit_loop.upper() == "PAY":
        #call the function that handles entring info into the payment table
        value_inserter(exit_loop)


    elif exit_loop.upper() == "O":
        #call the function that handles entring info into the Orders table
        value_inserter(exit_loop)





#7. SELECT ALL records from table Customers
import pandas as pd
import pyodbc


query = "SELECT * FROM Customers"

df = pd.read_sql(query, db)

df.set_index("Customer_id", inplace=True)

print("\nPrinting all customers \n")
print(df)

#8.  	SELECT records only from the name column in the Customers table.

query = "SELECT FirstName, LastName FROM Customers"

df = pd.read_sql(query, db)


print("\nPrinting all customer names: \n")
print(df)


#9.Show the name of the Customer whose CustomerID is 1.
query = "SELECT * FROM Customers WHERE Customer_id = 1"
df = pd.read_sql(query, db)

df.set_index("Customer_id", inplace=True)

print("\nPrinting customer number 1's info \n")
print(df)


#10. UPDATE the record for CustomerID =1  on the Customer table so that the name is “Lerato Mabitso”.
db = MySQLdb.connect("localhost", "root", "Umuzi123", "Umuzi")

cursor = db.cursor()

cursor.execute("""UPDATE Customers SET FirstName = 'Lerato', LastName = 'Mabitso' WHERE Customer_id = 1 """)

db.commit()

query = "SELECT * FROM Customers WHERE Customer_id = 1"

df = pd.read_sql(query, db)

df.set_index("Customer_id", inplace=True)

print("\nPrinting customer number 1 with updated info \n")
print(df)

# 11 DELETE the record from the Customers table for customer 2 (CustomerID = 2).

cursor.execute("""DELETE FROM Customers WHERE Customer_id = 2 """)

db.commit()

query = "SELECT * FROM Customers"

df = pd.read_sql(query, db)

df.set_index("Customer_id", inplace=True)

print("\n Printing updated customers table: \n")
print(df)

#12.  Select all unique values from the table Products.
query = """SELECT DISTINCT * FROM Products """

df = pd.read_sql(query, db)

df.set_index("Product_id", inplace=True)

print("\n unique values from the Products table: \n")
print(df)

#13.  Return the MAXIMUM payment made on the PAYMENTS table.
query = """SELECT MAX(Amount) FROM  Payments """

df = pd.read_sql(query, db)

print("\n Max payment is: \n")
print(df)


#14.  Create a query that selects all customers from the "Customers" table, sorted by the "Country" column.
query = """SELECT * FROM Customers ORDER BY Country """

df = pd.read_sql(query, db)
df.set_index("Customer_id", inplace=True)
print("\n Printing Customers table sorted by Country: \n")
print(df)

#15.Create a query that selects all Products with a price BETWEEN R100 and R600.
query = """SELECT * FROM Payments WHERE Amount >= 100.00 AND Amount <= 600.00 """

df = pd.read_sql(query, db)
df.set_index("Customer_id", inplace=True)
print("\n Payments with the prices between 100.00 and 600.00: \n")
print(df)

#16.  Create a query that selects all fields from "Customers" where country is "Germany" AND city is "Berlin".

query = """SELECT * FROM Customers WHERE Country='Germany' AND City = 'Berlin' """

df = pd.read_sql(query, db)
df.set_index("Customer_id", inplace=True)
print("\n Printing Customers who live in Germany Berlin: \n")
print(df)

#17.  Create a query that selects all fields from "Customers" where city is "Cape Town" OR "Durban".
query = """SELECT * FROM Customers WHERE City='Cape Town' OR City = 'Durban' """

df = pd.read_sql(query, db)
df.set_index("Customer_id", inplace=True)
print("\n Printing Customers who stay in Cape Town or Durban: \n")
print(df)

#18.  Select all records from Products where the Price is GREATER than R500.
query = """SELECT * FROM Payments WHERE Amount > 500 """

df = pd.read_sql(query, db)
df.set_index("Customer_id", inplace=True)
print("\n Payments with the prices above 500: \n")
print(df)

#19.  Return the sum of the Amounts on the Payments table.
query = """SELECT SUM(Amount) FROM Payments """

df = pd.read_sql(query, db)

print("\n Total sum of Payments made: \n")
print(df)


#20. Count the number of shipped orders in the Orders table.
query = """SELECT COUNT(Status) FROM Orders WHERE Status = 'shipped' """

df = pd.read_sql(query, db)
print("\n Total number of shipped orders: \n")
print(df)

#21.  Return the average price of all Products, in Rands and in Dollars (assume the exchange rate is R12 to the Dollar).
query = """SELECT AVG(BuyPrice) FROM Products """

df = pd.read_sql(query, db)

print("\n The average price in the products table: \n")
rands = int(df.iloc[0])
dollar = int(df.iloc[0]/12)
print("In Rands: R" + str(rands) + "\nIn Dollars: $" + str(dollar))

#22. Using INNER JOIN create a query that selects all Payments with Customer information.
query = """SELECT * FROM Payments INNER JOIN Customers ON Customers.Customer_id = Payments.Customer_id """

df = pd.read_sql(query, db)

print("\nPrinting inner join with payments and customers tables: \n")
print(df)


#Close cursor
cursor.close()
