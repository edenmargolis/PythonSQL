import sqlite3
from sqlite3 import Error

from Employees import Employees
from Coffee_Stands import Coffee_stands


# create a database connection to our SQLite database ->return a connection holder#
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('moncafe.db')
    except Error as e:
        print(e)
    return conn


# Print a table#
def print_all_table(cursor_object, table, selector):
    cursor_object.execute("SELECT * FROM " + table + " ORDER BY " + selector + " ASC;")
    rows = cursor_object.fetchall()
    for row in rows:
        print(row)


# Print the last joined table#
def print_join_table(cursor_object):
    cursor_object.execute(
        "SELECT Activities.date, Products.description, Activities.quantity , Employees.name ,Suppliers.name FROM Activities INNER JOIN Products ON Activities.product_id = Products.id LEFT JOIN Employees ON Activities.activator_id = Employees.id LEFT JOIN Suppliers ON Suppliers.id = Activities.activator_id;")
    rows = cursor_object.fetchall()
    for row in rows:
        print(row)


# Print the employees sales report#
def report(cursor_object):
    cursor_object.execute("SELECT Employees.name, Employees.salary, Coffee_stands.location FROM Employees LEFT JOIN Coffee_stands WHERE Employees.coffee_stand = Coffee_stands.id;")
    rows= cursor_object.fetchall()
    for row in rows:
        output = row[0]+" " +str(row[1])+" "+row[2]
        sales=0
        cursor_object.execute("SELECT Activities.quantity, Employees.name ,Products.price FROM Activities LEFT JOIN Employees ON Activities.activator_id = Employees.id LEFT JOIN Products ON Activities.product_id = Products.id;")
        result=cursor_object.fetchall()

        for item in result:
            if row[0] == item[1]:
                price = float(item[2])
                amount = abs(int(item[0]))
                sales=sales+price*amount
        print(output+" "+str(sales))



# The engine#
conn = create_connection()

# The query executor#
cursor = conn.cursor()

# Create references to the classes
employees_ref = Employees()
coffee_stands_ref = Coffee_stands()

# Print each table#
print('Activities')
print_all_table(cursor, 'Activities', 'date')

print('Coffee stands')
print_all_table(cursor, 'Coffee_stands', 'id')

print('Employees')
print_all_table(cursor, 'Employees', 'id')

print('Products')
print_all_table(cursor, 'Products', 'id')

print('Suppliers')
print_all_table(cursor, 'Suppliers', 'id')

print('Employees report')
report(cursor)

print('Activities')
print_join_table(cursor)
