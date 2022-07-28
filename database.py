import mysql.connector
import security


second_db = mysql.connector.connect(
    host="localhost",
    username="root",
    # gets my password from a module in this package for privacy iss.
    password=security.password()
)

# we need a cursor to start moving on the interface
mycursor = second_db.cursor()

# lets use our cursor to click/execute show databases
mycursor.execute("show databases")
result = mycursor.fetchall()
print(result)


def use_database(name_of_database):
    # first we get a list of all the data bases
    mycursor.execute("show databases")
    database_list = mycursor.fetchall()
    # check if our database already exist.
    # the items in the list is in sort of tuple of the form (name_of_database,)
    # so we check if the item does not exists in the list, then we create
    if (name_of_database.lower(),) not in database_list:  # databases in mysql are saved in lower cases
        # creates database of such name
        mycursor.execute(f"CREATE DATABASE {name_of_database}")
        print(f"{name_of_database} has been created and selected")
    else:
        print(f"{name_of_database} has been selected")

    # and it selects our database to our database
    return mysql.connector.connect(
        host="localhost",
        username="root",
        password=security.password(),
        database=name_of_database
    )
