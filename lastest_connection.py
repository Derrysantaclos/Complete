import database as database
from mysql_table import SqlTable


last_db = database.use_database("derrysantaclos")
mycursor = last_db.cursor()

NewBook = SqlTable("Newbook", last_db, mycursor)
NewBook.create(
    "ID int primary key auto_increment, Name varchar(50), Book varchar(50), price int")
columns_for_values = ["Name", "Book", "Price"]


def value_s():
    book_sellers = [
        {"name": "Robert", "book": "Rich Dad", "price": 1500},
        {"name": "Dan", "book": "money principles", "price": 2600},
        {"name": "Malcom", "book": "success stories", "price": 1700},
        {"name": "Obama", "book": "Stories my dad", "price": 1300},
        {"name": "Mosh", "book": "let's code", "price": 5000},
        {"name": "Enith", "book": "one time free", "price": 2500},
        {"name": "Ken", "book": "Heart is free", "price": 900},
        {"name": "Awolowo", "book": "Once upon a Nigeria", "price": 2300},
        {"name": "Drook", "book": "Dark magic", "price": 2000},
        {"name": "Robert", "book": "Poor Dad", "price": 1900},
        {"name": "Steve", "book": "behind the hidden walls", "price": 800}
    ]
    vals = []
    for each in book_sellers:
        lst_in_order = (each["name"], each["book"], each["price"])
        vals.append(lst_in_order)

    return(vals)


value_to_insert = value_s()
#NewBook.insert_column_data(columns_for_values, value_to_insert)
NewBook.select_data("booksellers")
