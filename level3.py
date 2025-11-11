import library_books
from datetime import datetime, timedelta

# Using a book ID, perform a checkout. 
# If the book is available: - Mark it unavailable - Set a due date 2 weeks from today (use datetime) - Increment the book’s checkout count
# If the book is already checked out, show a message instead.

def book_check_avail(book_id):
    for book in library_books.LIBRARY_BOOKS:
        if (book['id'] == book_id and book['available'] == True):
            return True
    return False

def update_book_status(book_id):
    for book in library_books.LIBRARY_BOOKS:
        if (book['id'] == book_id):
            book['available'] = False
            book['checkouts'] += 1
            book['due_date'] = (datetime.today() + timedelta(weeks=2)).strftime("%Y-%m-%d")
            print("Update Info",book)
            break
    
    

book_id = input("Enter book id: ")
if (book_check_avail(book_id) == False):
    print('Your book cannot be found or unavailable.')
else:
    update_book_status(book_id)
