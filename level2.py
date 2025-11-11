import library_books

# Allow the user to enter a search term. 
# Return all books that match either the author or genre. 
# Search should be case-insensitive.

def search(search_type,string_search):
    lower_case_str_search = string_search.lower().strip()
    output = []
    if (search_type == "1"):
        output = [book['title'] for book in library_books.LIBRARY_BOOKS if book['author'].lower().strip() == lower_case_str_search]
    elif (search_type == "2"):
        output = [book['title'] for book in library_books.LIBRARY_BOOKS if book['genre'].lower().strip() == lower_case_str_search]
    return output


search_type = input("If search by author, type 1. If seach by genre, type 2.\nEnter option: ")
string_search = ""

if (search_type == "1"):
    string_search = input("Enter author: ")
elif (search_type == "2"):
    string_search = input("Enter genre: ")

print("-----Search result----------")
print(*search(search_type,string_search),sep="\n")
    
        





