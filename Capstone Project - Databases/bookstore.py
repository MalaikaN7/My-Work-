import sqlite3

# Connect to the ebookstore database (it will be created if it doesn't exist).
db = sqlite3.connect('ebookstore.db')
cursor = db.cursor()

# Create the book table (if it doesn't already exist).
cursor.execute('''
CREATE TABLE IF NOT EXISTS book(
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    qty INTEGER)
''')
db.commit()

# Insert default data if the table is empty.
cursor.execute("SELECT COUNT(*) FROM book")
if cursor.fetchone()[0] == 0:
    books = [
        (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
        (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40),
        (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
        (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
        (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
    ]
    cursor.executemany('INSERT INTO book(id, title, author, qty) VALUES(?, ?, ?, ?)', books)
    db.commit()


def add_book():
    '''Function to add a new book to the database.'''
    try:
        id = int(input("Enter book ID: "))
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        qty = int(input("Enter quantity: "))
        cursor.execute('''INSERT INTO book(id, title, author, qty) VALUES(?, ?, ?, ?)''', (id, title, author, qty))
        db.commit()
        print("Book added successfully!")
    except ValueError:
        print("Invalid input! Please make sure you enter numbers for ID and quantity.")
    except sqlite3.IntegrityError:
        print(f"Error: A book with ID {id} already exists. Please use a unique ID.")
    except Exception as e:
        # Rolling back to make sure the database remains\
        # unchanged if an error occurs.
        db.rollback()
        print(f"Unexpected error: {e}")


def update_book():
    '''Function to update book information.'''
    try:
        id = int(input("Enter the ID of the book you want to update: "))
        new_title = input("Enter new title: ")
        new_author = input("Enter new author: ")
        new_qty = int(input("Enter new quantity: "))
        cursor.execute('''UPDATE book SET title = ?, author = ?, qty = ? WHERE id = ?''', (new_title, new_author, new_qty, id))
        db.commit()
        if cursor.rowcount == 0:
            print("Error: Book not found!")
        else:
            print("Book updated successfully!")
    except ValueError:
        print("Invalid input! Please make sure you enter numbers for ID and quantity.")
    except Exception as e:
        # Rolling back to make sure the database remains\
        # unchanged if an error occurs.
        db.rollback()
        print(f"Unexpected error: {e}")


def delete_book():
    '''Function to delete a book from the database.'''
    try:
        id = int(input("Enter the ID of the book you want to delete: "))
        cursor.execute('''DELETE FROM book WHERE id = ?''', (id,))
        db.commit()
        if cursor.rowcount == 0:
            print("Error: Book not found!")
        else:
            print("Book deleted successfully!")
    except ValueError:
        print("Invalid input! Please enter a valid book ID.")
    except Exception as e:
        # Rolling back to make sure the database remains\
        # unchanged if an error occurs.
        db.rollback()
        print(f"Unexpected error: {e}")


def search_books():
    '''Function to search for a book in the database.'''
    try:
        search_id = int(input("Enter the ID of the book you're searching for: "))
        cursor.execute('''SELECT * FROM book WHERE id = ?''', (search_id,))
        book = cursor.fetchone()
        if book:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")
        else:
            print("Error: Book not found!")
    except ValueError:
        print("Invalid input! Please enter a valid book ID.")
    except Exception as e:
        print(f"Unexpected error: {e}")


def menu():
    '''Function for the menu for the bookstore.'''
    while True:
        print("\nBookstore Menu:")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search books")
        print("0. Exit")
        choice = input("Select an option from (0-4): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            search_books()
        elif choice == '0':
            print("You chose Exit")
            print("Goodbye!")
            db.close()
            break
        else:
            print("Invalid option, please try again.")


# Run the menu
menu()
