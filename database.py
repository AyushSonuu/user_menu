import sqlite3

connection = sqlite3.connect("dataa.db")
connection.row_factory = sqlite3.Row

# entries=[]
def create_table():
    '''transaction to create a table'''
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT , date TEXT);")
    # connection.commit()
def add_entry(entry_content,entry_date):
    # entries.append({"content":entry_content,"date":entry_date})
    with connection:
        # connection.execute(f"INSERT INTO entries VALUES('{entry_content}','{entry_date}');")
        connection.execute(
            "INSERT INTO entries VALUES(?,?);",(entry_content,entry_date)
        )


def get_entry():
    '''fetches the entries from the data base'''
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM entries;")
    cursor = connection.execute("SELECT * FROM entries ; ")
    # cursor.fetchone()
    return cursor