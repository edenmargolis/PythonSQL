class Activities:

    # Create the table#
    def create_table(self,cursor_object):

        # Append all the params with a ',' between them#
        query = 'CREATE TABLE Activities (product_id INTEGER INTEGER REFERENCES Product(id),quantity INTEGER NOT ' \
                'NULL,activator_id INTEGER NOT NULL,date DATE NOT NULL); '
        cursor_object.execute(query)

    # Insert values into the table#
    def insert_line(self,cursor_object, product_id, quantity, activator_id, date):
        params = (product_id,quantity,activator_id,date)
        cursor_object.execute("INSERT INTO Activities VALUES (?,?,?,?);", params)

        # Deletes a line from the table #
    def delete(self,cursor_object,id):
        cursor_object.execute("DELETE FROM Activities WHERE id = (?)",id)