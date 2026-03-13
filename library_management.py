import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    category TEXT,
    status TEXT DEFAULT 'Available'
)''')
conn.commit()


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    category = input("Enter category: ")
    cursor.execute("INSERT INTO books (title,author,category) VALUES (?,?,?)",(title,author,category))
    conn.commit()
    print("book added succesfully")


def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    print("all books list")
    for b in books:
        print(b[0],b[1],b[2],b[3],b[4])


def search_book():
    name = input("enter book name to search: ")
    cursor.execute("SELECT * FROM books WHERE title LIKE ?"  ,('%'+name+'%',))
    results = cursor.fetchall()
    for b in results:
        print(b[0],b[1],b[2],b[3],b[4])


def delete_book():
    view_books()
    bid = int(input("enter book id to delete: "))
    cursor.execute("DELETE FROM books WHERE id=?",(bid,))
    conn.commit()
    print("book deleted")


def total_books():
    cursor.execute("SELECT COUNT(*) FROM books")
    count = cursor.fetchone()
    print("total books in library :",count[0])


def main():
    print("welcome to library management system")
    while True:
        print("\n1 add book")
        print("2 view all books")
        print("3 search book")
        print("4 delete book")
        print("5 total books")
        print("6 exit")

        choice = input("enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            total_books()
        elif choice == '6':
            print("thankyou bye")
            conn.close()
            break
        else:
            print("wrong choice enter again")


main()





