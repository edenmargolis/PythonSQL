class Employees:


    # Create the table#
    def create_table(self, cursor_object):
        # Append all the params with a ',' between them#
        query = 'CREATE TABLE Employees (id INTEGER PRIMARY KEY,name TEXT NOT NULL,salary REAL NOT NULL,coffee_stand ' \
                'INTEGER REFERENCES Coffee_stand(id)); '
        cursor_object.execute(query)

    # Insert values into the table#
    def insert_line(self, cursor_object, id, name, salary, coffee_stand):
        params = (id, name, salary, coffee_stand)
        cursor_object.execute("INSERT INTO Employees VALUES (?,?,?,?);", params)

