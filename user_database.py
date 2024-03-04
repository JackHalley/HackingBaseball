import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('lpDatabase.db')

cursor = connection.cursor()

# create a table
# connection.execute('''
#     CREATE TABLE IF NOT EXISTS users(
#     first_name text,
#     last_name text,
#     email text
#     )
#     ''')

# many_users = [
#     ('Jackson', 'Halley', 'hackingbaseball@gmail.com'),
#     ('Alex','Adams','alexadams@gmail.com' ),
#     ('Jack','Sage', 'jacktheman@email.com')
#     ]

# cursor.executemany("INSERT INTO users VALUES (?,?,?)", many_users)

cursor.execute("SELECT * FROM users")

print(cursor.fetchall())






print("Command executed successfully... ")
# commit command
connection.commit()

# close our connection
connection.close()

