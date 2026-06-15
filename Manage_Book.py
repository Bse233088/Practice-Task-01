books = []

def add_book():
    title = input("Enter book title: ").strip()

    if title == "":
        print("Book title cannot be empty.")
        return

    books.append(title)
    print("Book added successfully.")


def view_books():
    if not books:
        print("No books available.")
        return

    print("\nBooks List:")
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book}")


def delete_book():
    view_books()

    if not books:
        return

    try:
        index = int(input("Enter book number to delete: "))
        books.pop(index - 1)
        print("Book deleted successfully.")
    except (ValueError, IndexError):
        print("Invalid selection.")