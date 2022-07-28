""" A SqlTable class to ease writing of Sql Queries.

    SqlTable class has basic methods of an sql table

"""


class SqlTable:
    """ To use an SqlTable.

    This class simplifies the use of an SqlTable. 
    SqlTable class has basic methods of an sql table.

    Parameters:
    name_of_table(str): The name of your table. You are advised to use the same name as the object name. i.e. Table_name = SqlTable(Table_name, .....).
    db_reference(obj):  The database you want your table to be written.
    name_of_cursor(obj):  The object representing your connection cursor.

    Use SqlTable.create(.....) to activate your table
    """

    # first our constructor, to allow the table take name of table while creating it
    def __init__(self, name_of_table, db_reference, name_of_cursor):

        self.name_of_table = name_of_table
        self.name_of_cursor = name_of_cursor
        self.db_reference = db_reference

    def create(self, column_and_properties):
        """Registers the table into the database.
        Creates the table and its columns in the database

        Parameters:
        column_and_properties: Column name followed by the property as a single string seprated with spaces. 
        For multiple columns, a comma, within the string should be used to seperate from the other
        e.g. "column1 int primary key, column2 varchar(20),........,last_column int". 

        """
        # let's check if the table exists to avoid error
        # first lets get a list of all tables in the database
        self.name_of_cursor.execute("show tables")
        table_list = self.name_of_cursor.fetchall()
        if (self.name_of_table.lower(),) not in table_list:
            self.name_of_cursor.execute(
                f"CREATE TABLE {self.name_of_table} ({column_and_properties})")
            print("table created")
            # creates if not in list
        else:
            print(
                f"{self.name_of_table} exists use .modify or .insert to work on the table")

    def column_list(self):  # returns a list of column available in the table
        """ Returns a list of all columns present in your Table"""
        self.name_of_cursor.execute(f"SHOW COLUMNS FROM {self.name_of_table}")
        col_list = [col[0] for col in self.name_of_cursor.fetchall()]
        return col_list

    def modify_column(self, column_name, property_details):
        """To modify certain column in the table.

            To edit column properties.
            Parameters:

            column_name(str): Name of column to modify.
            propery_details(str): The new property of the column e.g. VARCHAR(20) to change the datatype from whatever to variable type of maximum of 20 characters


        """
        # check if column truly exists
        # first get a list of all column in the table
        if column_name in self.column_list():
            print("column available")
            self.name_of_cursor.execute(
                f"ALTER TABLE {self.name_of_table} MODIFY {column_name} {property_details}")
            print(f"{column_name} modified successfully")

        else:
            print("column not found, use insert_column to insert new column")

    def add_column(self, column_name, property_details):
        if column_name not in self.column_list():  # so as to create a new name
            self.name_of_cursor.execute(
                f"ALTER TABLE {self.name_of_table} add column {column_name} {property_details}")
            print(f"column {column_name} added successfully")

        else:  # column name already exists
            print(
                f"{column_name} exists, consider using another name or modifying existing column")

    def insert_column_data(self, columns, vals):
        """To insert data into table

        Parameters:
        columns(List or Tuple): Columns where data are to be inserted into.
        vals(List of tuples): Values to be inserted.e.g. to insert one row into two columns[(arg1,arg2)], to insert two rows into two columns: [(arg1,arg2),(arg4,arg5)]
        """
        # the columns where data shoul be given should be in form of a list or tuple
        # we need to convert all to a single string
        col_str = ""  # first, its an empty list
        for each in columns:
            col_str += each + ","
        # remove the last char which is a comma
        col_str = col_str[:-1]
        no_of_s = "%s, " * (len(columns)-1)
        data_command = f"insert into {self.name_of_table} ({col_str}) VALUES ({no_of_s}%s)"
        self.name_of_cursor.executemany(data_command, vals)
        self.db_reference.commit()  # just like: refresh/save
        print(self.name_of_cursor.rowcount, "row inserted")

    def select_data(self, table_for_select, columns="*", where_for_select="is not null", order_for_selection="null"):
        self.name_of_cursor.execute(
            f"SELECT {columns} FROM {table_for_select} WHERE {where_for_select} ORDER BY {order_for_selection}")
        result = self.name_of_cursor.fetchall()
        print(result)
