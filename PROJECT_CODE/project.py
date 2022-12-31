import PROJECT_CODE.func1 as func1

USER_CHOICE = """
ENTERED VALUE : MEANING
a : add a book
l : list all the books
r : to assign a book as read
d : to delete a book
q : quit

ENTER YOUR CHOICE""
"""


def menu():
    func1.create_book_table()
    command = input(USER_CHOICE)

    while command != 'q':

        if command == 'a':

            name = input("Enter name of the book you want to read")
            author = input("Name of teh author")
            func1.enter_books(name, author)

        elif command == 'r':
            book_name = input("ENTER THE BOOK YOU WANT TO SEARCH IN THE DIRECTORY")
            func1.read(book_name)

        elif command == 'l':
            books = func1.get_all_books()
            print(books)
            # for i in books:
            #     read = 'YES' if i['read'] != 0 else 'NO'
            #     print(f"{i['name']} by {i['author']},read:{read}")

        elif command == 'd':
            book_name = input("ENTER THE BOOK YOU WANT TO DELETE FROM THE DIRECTORY")
            func1.delete(book_name)

        else:
            raise func1.NameNotFound('INPUT IS OUT OF THE USER CHOICE')
        command = input("enter command[a,l,r,d,q]")


menu()
