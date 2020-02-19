import sqlite3
from sqlite3 import Error

class Coffee_stands:

    # Create the table#
    def create_table(self,cursor_object):

        # Append all the params with a ',' between them#
        query = 'CREATE TABLE Coffee_stands (id INTEGER PRIMARY KEY,location TEXT NOT NULL,number_of_employees ' \
                'INTEGER); '
        cursor_object.execute(query)

    # Insert values into the table#
    def insert_line(self,cursor_object, id, location, number_of_employees):
        params = (id, location, number_of_employees)
        cursor_object.execute("INSERT INTO Coffee_stands VALUES (?,?,?);", params)

    # Deletes a line from the table #
    def delete(self,cursor_object,id):
        cursor_object.execute("DELETE FROM Coffee_stands WHERE id = (?)",id)

    # Return the location of a coffee stand#
    def get_location_by_id(self, cursor_object, id):
        cursor_object.execute("SELECT location FROM Coffee_stands WHERE id=({});".format(id))
        temp = cursor_object.fetchone()
        return temp[0]