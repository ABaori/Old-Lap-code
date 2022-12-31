import csv
import json

"""
CONCERNED WITH STROING AND RETRIEVING FILES
name,author,read\n
name,author,read\n
name,authots,read\n

"""
books_file = 'books.json'

def create_book_table():

    with open(books_file,'w') as file:
        json.dump([], file)


def get_all_books():

    with open(books_file,'r') as file:
        return json.load(file)


def enter_books(name, author):

    books = get_all_books()
    with open(books_file) as file:
        books.append({'name':name,'author':author,'read': False})
        _save_all_books(books)

def _save_all_books(books):
    with open(books_file,'w') as file:
        json.dump(books, file, indent=2)



def read(book_name):
    books = get_all_books()
    try:
        for i in range(len(books)):
            if books[i]['name'] == book_name:
                books[i]['read'] = True
            break
    except:
        raise NameNotFound('No book by the name you gave')
    print(books)
    _save_all_books(books)


def not_read(book_name):
    books = get_all_books()
    try:
        for i in range(len(book)):
            if books[i]['name'] == book_name:
                books[i]['read'] == False
            break
    except:
        raise NameNotFound('No book by the name you gave')
    print(book)


def delete(book_name):
    # try:
    #     for i in range(len(books)):
    #         if books[i]['name'] == book_name:
    #             books.remove(books[i])
    #         break
    # except:
    #     raise NameNotFound('No book by the name you gave')
    books = get_all_books()
    books = [book for book in books if book['name'] != book_name]
    print(books)

    _save_all_books(books)

class NameNotFound(Exception):
    def __init__(self, message):
        self.message = message








