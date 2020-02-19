import sqlite3
from sqlite3 import Error

from Employees import Employees
from Products import Products
from Activities import Activities
import os
import sys

# The connection to the database#
def init_db():
    # Connect to the database and return a pointer to it#
    try:
        conn = sqlite3.connect('moncafe.db')
    except Error as e:
        print(e)
    return conn


# Read the config file line by line and process each line#
def file_processor(filepath):
    f = open(filepath, 'r')
    list_of_lines = f.readlines()

    date_nums = []
    # Iterate through each line in the file and process it#
    for line in list_of_lines:
        # Split the line into a list #
        result = [x.strip() for x in line.split(',')]
        date_nums.append(result[3])

    # Sort the numbers #
    date_nums = [int(i) for i in date_nums]
    date_nums.sort()

    # From the earliest to the latest#
    for date in date_nums:
        for line in list_of_lines:
            if line.__contains__(str(date)):
                line_process(line)
                list_of_lines.remove(line)

    f.close()


# Process each line#
def line_process(line):
    # Split the line into a list#
    result = [x.strip() for x in line.split(',')]

    # Checks if we need to decrease the product's quantity #
    if int(result[1]) < 0:

        # Check if the remained quantity is a positive number #
        if int(products_table.get_quantity(cursor, result[0])[0]) - abs(int(result[1])) >= 0:

            old_quantity = int(products_table.get_quantity(cursor, result[0])[0])
            difference = abs(int(result[1]))

            # Sets the new quantity of the product #
            products_table.set_quantity(cursor, result[0], str(old_quantity - difference))
            # Adds to the line to the Activities table #
            activities_table.insert_line(cursor, result[0], result[1], result[2], result[3])


    # If we need to increase the quantity add the new quantity and update the activities table #
    elif int(result[1]) >= 0:
        prev_quality = int(products_table.get_quantity(cursor, result[0])[0])
        new_quality = prev_quality + int(result[1])
        products_table.set_quantity(cursor, result[0], str(new_quality))
        activities_table.insert_line(cursor, result[0], result[1], result[2], result[3])


# The engine#

conn = init_db()

# The query executor#
cursor = conn.cursor()

# References to tables#
activities_table = Activities()
products_table = Products()
employees_table = Employees()

# Process the config file#
file_processor(sys.argv[1])

# Commit the changes to the database#
conn.commit()

# Print it#
os.system('python3 printdb.py')