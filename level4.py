import library_books
from datetime import datetime, date

#Write a function to return a book by ID. Reset its availability and due date.
#Write another function to list all overdue books (i.e., books with due_date in the past and still checked out).

def update_book_info(book_id):
    for book in library_books.LIBRARY_BOOKS:
        if book['id'] == book_id:
            book['available'] = True
            book['due_date'] = None
    

def get_overdue_books():
    over_due_books = []
    today_date = date.today()
    for book in library_books.LIBRARY_BOOKS:
        if book['due_date'] != None and book['available'] == False:
            get_book_due_date = datetime.strptime(book['due_date'],"%Y-%m-%d").date()
            if get_book_due_date < today_date:
                over_due_books.append(book['id'])
    return over_due_books


print(get_overdue_books())

