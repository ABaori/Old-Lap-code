import sqlite3
from .ContexM import  DatabaseConnection

"""
CONCERNED WITH STROING AND RETRIEVING FILES
name,author,read\n
name,author,read\n
name,authots,read\n

"""


def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key,author text,read integer)')




def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        return [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]


def enter_books(name, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        # cursor.execute(f'insert INTO books VALUES("{name}","{author}",0)')
        cursor.execute(f'INSERT INTO books VALUES(?,?,0)', (name, author))
        books = [{'name':row[0],'author':row[1],'read':row[2]} for row in cursor.fetchall()]



# def _save_all_books(books):    NO NEED FOR IT IN SQL SINCE ITS SVING IT
#     with open(books_file, 'w') as file:
#         json.dump(books, file, indent=2)


def read(book_name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read = 1 WHERE name = ?', book_name)


def not_read(book_name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE*FROM books SET read = 0 WHERE name = ?', book_name)





def delete(book_name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE*FROM books WHERE name = ?', book_name)




class NameNotFound(Exception):
    def __init__(self, message):
        self.message = message
