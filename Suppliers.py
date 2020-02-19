class Suppliers:
    # Create the table#
    def create_table(self,cursor_object):
        # Append all the params with a ',' between them#
        query = 'CREATE TABLE Suppliers (id INTEGER PRIMARY KEY,name TEXT NOT NULL,contact_information TEXT);'
        cursor_object.execute(query)

    # Insert values into the table#
    def insert_line(self,cursor_object, id, name, contact_information):
        params = (id, name, contact_information)
        cursor_object.execute("INSERT INTO Suppliers VALUES (?,?,?);", params)

    # Deletes a line from the table #
    def delete(self,cursor_object, id):
        cursor_object.execute("DELETE FROM Suppliers WHERE id = (?)", id)
