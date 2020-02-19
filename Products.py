class Products:

    # Create the table#
    def create_table(self, cursor_object):
        # Append all the params with a ',' between them#
        query = 'CREATE TABLE Products (id INTEGER PRIMARY KEY,description TEXT NOT NULL,price REAL NOT NULL,' \
                'quantity INTEGER NOT NULL); '
        cursor_object.execute(query)

    # Insert values into the table#
    def insert_line(self, cursor_object, id, description, price, quantity):
        params = (id, description, price, quantity)
        cursor_object.execute("INSERT INTO Products VALUES (?,?,?,?);", params)

    # Deletes a line from the table#
    def delete(self, cursor_object, id):
        cursor_object.execute("DELETE FROM Products WHERE id = (?)", id)

    # Gets the quantity of a given id#
    def get_quantity(self, cursor_object, id):
        cursor_object.execute("SELECT quantity FROM Products WHERE id=({});".format(id))
        temp = cursor_object.fetchone()
        return temp

    # Sets the quantity of a given id#
    def set_quantity(self, cursor_object, id, newquantity):
        params = (newquantity, id)
        cursor_object.execute("UPDATE Products SET quantity=(?) WHERE id=(?);", params)

    # Get the price by the products id#
    def get_price(self, cursor_object, id):
        cursor_object.execute("SELECT price FROM Products WHERE id=({});".format(id))
        temp = cursor_object.fetchone()
        return temp[0]