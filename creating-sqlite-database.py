import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
create_table = "CREATE TABLE users (id int, username text, password text)"
user = (1, 'jose','asdf')
insert_query = " INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query,user)
