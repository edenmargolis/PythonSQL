import sqlite3
from sqlite3 import Error
import os
import sys
from Employees import Employees
from Products import Products
from Suppliers import Suppliers
from Coffee_Stands import Coffee_stands
from Activities import Activities

# The initialization of the database#
def init_db():
    # If it already exists delete it#
    if os.path.isfile('moncafe.db'):
        os.remove('moncafe.db')

    # Create the database and return a pointer to it#
    try:
        conn = sqlite3.connect('moncafe.db')
    except Error as e:
        print(e)
    return conn


# Read the config file line by line and process each line#
def file_processor(filepath):
    f = open(filepath, 'r')
    list_of_lines = f.readlines()

    # Iterate through each line in the file and process it#
    for line in list_of_lines:
        line_process(line)

    f.close()


# Process each line#
def line_process(line):

    # Split the line into a list#
    result = [x.strip() for x in line.split(',')]
    if result[0] == 'E':

        # Add to Employees#
        employees_table.insert_line(cursor, result[1], result[2], result[3],result[4])

    elif result[0] == 'S':

        # Add to Suppliers#
        suppliers_table.insert_line(cursor, result[1], result[2], result[3])

    elif result[0] == 'P':

        # Add to Products#
        products_table.insert_line(cursor, result[1], result[2], result[3], '0')

    elif result[0] == 'C':

        # Add to Coffee stands#
        coffee_stands_table.insert_line(cursor, result[1], result[2], result[3])


# The engine#

conn = init_db()

# The query executor#
cursor = conn.cursor()

# Init tables#


employees_table = Employees()
employees_table.create_table(cursor)

suppliers_table = Suppliers()
suppliers_table.create_table(cursor)

products_table = Products()
products_table.create_table(cursor)

coffee_stands_table = Coffee_stands()
coffee_stands_table.create_table(cursor)

activities_table = Activities()
activities_table.create_table(cursor)

# Process the config file#
file_processor(sys.argv[1])

# Commit the changes to the database#
conn.commit()