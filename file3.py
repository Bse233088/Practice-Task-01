from users import users
from books import books
from transactions import transactions


def generate_report():
    print("\n===== LIBRARY REPORT =====")

    print(f"Total Users: {len(users)}")
    print(f"Total Books: {len(books)}")
    print(f"Total Transactions: {len(transactions)}")

    borrowed = 0
    returned = 0

    for t in transactions:
        if t["status"] == "Borrowed":
            borrowed += 1
        elif t["status"] == "Returned":
            returned += 1

    print(f"Borrowed Books: {borrowed}")
    print(f"Returned Books: {returned}")

    print("==========================")