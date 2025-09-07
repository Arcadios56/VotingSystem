item_book = [
	{"title": "The Great wall of Jericho"},
	{"title": "The Great fall of the First man"},
	{"title": "A stitch in time"},

def display_menu():
    print("1. View all books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")
    return input("Enter your choice (1-4): ")


def borrow_book():
    view_books()
    choice = int(input("\nEnter the number of the book to borrow: ")) - 1
    if 0 <= choice < len(books):
        if books[choice]["status"] == "Available":
            books[choice]["status"] = "Borrowed"
            print(f"You have borrowed '{books[choice]['title']}'")
        else:
	    print(" Book is already borrowed!")
    else:
	    print("Invalid book number input!")



def main():
    while True:
        choice = display_menu()
        if choice == "1":
            view_books()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            print("Closing")
            break
        else:
            print(" Select 1-4!")


main()


 

