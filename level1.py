import library_books

# Create a function that prints all available books in the system. 
# Include book ID, title, and author.

def print_avail_books(books):
    avail_books = [{book['id'], book['title'], book['author']} for book in books if book['available']]
    print(*avail_books, sep="\n")


print_avail_books(library_books.LIBRARY_BOOKS)

    



