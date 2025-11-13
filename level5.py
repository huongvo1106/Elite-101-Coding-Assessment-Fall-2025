# Create a Book class and refactor your logic so books are objects, not dictionaries
# Create a simple command-line menu that allows the user to:
# View available books
# Search
# Checkout
# Return
# View overdue books
# View top 3 most checked-out books


class Book:
    def __init__(self, id, title, author, genre, available: bool, due_date, checkouts: int):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts

def view_available_books(book_list) -> []:
    return [book.title for book in book_list if book.available == True]

def search_book_by_title(book_list, title) -> [bool]:
    return [book.available for book in book_list if book.title.lower() == title.lower()]

def top_three_checked_books(book_list):
    
    sort_book_list_checkout = sorted(book_list, key=lambda book:book.checkouts, reverse=True)
    return [book.title for book in sort_book_list_checkout[0:3]]



book_1 = Book("B1", "The Lightning Thief", "Rick Riordan", "Fantasy", True, None, 2)
book_2 = Book("B2", "To Kill a Mockingbird", "Harper Lee", "Historical", False, "2025-11-01", 5)
book_3 = Book("B3", "The Great Gatsby", "F. Scott Fitzgerald", "Classic", True, None, 3)
book_4 = Book("B4", "1984", "George Orwell", "Dystopian", True, None, 4)
book_5 = Book("B5", "Pride and Prejudice", "Jane Austen", "Romance", True, None, 6)
book_6 = Book("B6", "The Hobbit", "J.R.R. Tolkien", "Fantasy", False, "2025-11-10", 8)
book_7 = Book("B7", "Fahrenheit 451", "Ray Bradbury", "Science Fiction", True, None, 1)
book_8 = Book("B8", "The Catcher in the Rye", "J.D. Salinger", "Coming-of-Age", False, "2025-11-12", 3)

book_list: Book = [book_1, book_2, book_3, book_4, book_5, book_6, book_7, book_8]
print("1. View available books\n2. Search\n3. Checkout\n4. Return\n5. View overdue books\n6. View top 3 most checked-out books")
user_choice = input("Enter your option: ")
if (user_choice == "1"):
    print(view_available_books(book_list))
elif (user_choice == "2"):
    title = input("Enter book title: ")
    if search_book_by_title(book_list, title) == [True]:
        print(title, "is available.")
    else:
        print(title, "is not available.")
elif (user_choice == "6"):
    print(top_three_checked_books(book_list))

    
