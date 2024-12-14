class book():
    def __init__(self,title,author,year,isbn,pages):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.pages = pages

books = []

def add_books():
        print("Add new books: ")
        title = input("Enter Book's Title: ")
        author = input("Enter the Book's Author: ")
        year = int(input("Enter The Year of Publication: "))
        isbn = input("Enter Book's ISBN: ")
        pages = int(input("Enter Number of Pages: "))    
        books.append(Library(title,author,year,isbn,pages))
        print("Book Successfully Added to Inventory! \n")

def display_books():
    if not books:
        print("No such books in the Libary.\n")
        return
    for book in books:
         print(f'Title: {book.title}, Author: {book.author}, Year of Publication: {book.year}, ISBN: {book.isbn}, Pages: {book.pages}')
    print()
         
def search_book():
    print("Search for a Book\n")
    search = input("Enter Book Title: ").lower()
    found_books = [book for book in books if search in book.title.lower()]
    
    if found_books:
        for book in found_books:
            print(f'Title: {book.title}, Author: {book.author}, Year of Publication: {book.year}, ISBN: {book.isbn}, Pages: {book.pages}')
    else:
        print("The Book you are searching cannot be found..\n")

     

def main():
     while True:
        print("Library Book Management System")
        print("1. Add Book")
        print("2. Display All Book")
        print("3. Search for Books")
        print("4. Quit Program")


        choice = input("Enter Your Choice: (1-4): ")

        if choice == "1":
             add_books()

        elif choice == "2":
            display_books()

        elif choice == "3":
             search_book()

        elif choice == "4":
            print("Program has been shut down! Thank you!")
            break     

        else:
             print("Invalid Choice. Please Try Again! \n")

if __name__ == "__main__":
    main()
