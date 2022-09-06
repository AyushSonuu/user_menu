import sqlite3

connection = sqlite3.connect("dataa.db")

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
    return entries
