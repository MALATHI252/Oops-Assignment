import mysql.connector
class Database:
    def __init__(self, host, user, password, database=None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
    def connect(self):
        if self.database:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        else:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
        self.cursor = self.connection.cursor()
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
        self.cursor = None
        self.connection = None
    def commit(self):
        if self.connection and self.connection.is_connected():
            self.connection.commit()
    def rollback(self):
        if self.connection and self.connection.is_connected():
            self.connection.rollback()
db_server = Database(
    "localhost",
    "root",
    "Maalu@2529"
)
try:
    db_server.connect()
    db_server.cursor.execute(
        "CREATE DATABASE IF NOT EXISTS LibraryDB"
    )
    db_server.commit()
    print("Database created successfully")
except mysql.connector.Error as e:
    print("Unable to create database")
    print("Error:", e)
finally:
    db_server.close()
class Books:
    def __init__(self, database):
        self.database = database
    def create_table(self):
        try:
            self.database.connect()
            query = """
                CREATE TABLE IF NOT EXISTS Books(
                    Book_id INT AUTO_INCREMENT PRIMARY KEY,
                    ISBN VARCHAR(20) UNIQUE,
                    Book_Title VARCHAR(100),
                    Author VARCHAR(50),
                    Category VARCHAR(20),
                    price DECIMAL(10,2),
                    Available_copies INT
                ) AUTO_INCREMENT=101
            """
            self.database.cursor.execute(query)
            self.database.commit()
            print("Books table created successfully")
        except mysql.connector.Error as e:
            self.database.rollback()
            print("Unable to create Books table")
            print("Error:", e)
        finally:
            self.database.close()
    def add_book(self):
        try:
            self.database.connect()
            ISBN = input("Enter the ISBN number: ")
            Book_Title = input("Enter the Book Title: ")
            Author = input("Enter the author: ")
            Category = input("Enter the Category: ")
            price = float(input("Enter the price: "))
            Available_copies = int(input("Enter the available copies of the book: "))
            if (not ISBN or not Book_Title or not Author or not Category):
                print("Each field must be filled")
                return
            if price <= 0:
                print("Price cannot be zero or negative")
                return
            if Available_copies <= 0:
                print("Available copies cannot be zero or negative")
                return
            query = """
                INSERT INTO Books
                (ISBN,Book_Title,Author,Category,price,Available_copies)
                VALUES(%s,%s,%s,%s,%s,%s)
            """
            values = (ISBN,Book_Title,Author,Category,price,Available_copies)
            self.database.cursor.execute(
                query,
                values)
            self.database.commit()
            print(self.database.cursor.rowcount,"Record inserted")
        except ValueError:
            print("Please enter valid numeric values ""for price and available copies")
        except mysql.connector.Error as e:
            self.database.rollback()
            print("Unable to insert record")
            print("Error:", e)
        finally:
            self.database.close()
    def update_Book(self):
        try:
            self.database.connect()
            Book_id = input("Enter the book id for update: ")
            New_Category = input("Enter the new Category: ")
            New_price = float( input("Enter the new price: "))
            if not Book_id or not New_Category:
                print("Each field must be filled")
                return
            if New_price <= 0:
                print("Price cannot be zero or negative")
                return
            query = """
                UPDATE Books
                SET price=%s,
                    Category=%s
                WHERE Book_id=%s
            """
            values = (New_price,New_Category,Book_id)
            self.database.cursor.execute(
                query,values)
            self.database.commit()
            if self.database.cursor.rowcount > 0:
                print(self.database.cursor.rowcount,"Record updated")
            else:
                print("No matching record found")
        except ValueError:
            print("Please enter a valid price" )
        except mysql.connector.Error as e:
            self.database.rollback()
            print("Unable to update record")
            print("Error:", e)
        finally:
            self.database.close()
    def delete_Book(self):
        try:
            self.database.connect()
            Book_id = input("Enter the book id: ")
            if not Book_id:
                print("Book id cannot be empty")
                return
            check_query = """
                SELECT *
                FROM Borrow
                WHERE Book_id=%s
                AND Status='BORROWED'
            """
            self.database.cursor.execute(
                check_query,
                (Book_id,))
            if self.database.cursor.fetchone():
                print(
                    "Cannot delete the book because "
                    "it is currently borrowed")
                return
            query = """
                DELETE FROM Books
                WHERE Book_id=%s
            """
            self.database.cursor.execute(
                query,
                (Book_id,) )
            self.database.commit()
            if self.database.cursor.rowcount > 0:
                print( self.database.cursor.rowcount,"Record deleted")
            else:
                print("No matching record found")
        except mysql.connector.Error as e:
            self.database.rollback()
            print("Unable to delete record")
            print("Error:", e)
        finally:
            self.database.close()
    def display_all(self):
        try:
            self.database.connect()
            query = """
                SELECT *
                FROM Books
            """
            self.database.cursor.execute(query)
            records = (self.database.cursor.fetchall())
            print("\n======== ALL BOOKS ========")
            if records:
                for record in records:
                    print(record)
            else:
                print("No records found")
        except mysql.connector.Error as e:
            print("Unable to retrieve records")
            print("Error:", e)
        finally:
            self.database.close()
    def search(self):
        try:
            self.database.connect()
            Book_Title = input("Enter the book title: ")
            if not Book_Title:
                print("Book title cannot be empty")
                return
            query = """
                SELECT *
                FROM Books
                WHERE Book_Title=%s
            """
            self.database.cursor.execute(
                query,(Book_Title,))
            record = (self.database.cursor.fetchone())
            if record:
                print("Record found:", record)
            else:
                print("No record found")
        except mysql.connector.Error as e:
            print("Unable to retrieve record")
            print("Error:", e)
        finally:
            self.database.close()
class Members:
    def __init__(self, database):
        self.database = database
    def create_table(self):
        try:
            self.database.connect()
            query = """
                CREATE TABLE IF NOT EXISTS Members(
                    Member_id INT AUTO_INCREMENT PRIMARY KEY,
                    Member_Name VARCHAR(50),
                    Phone VARCHAR(15),
                    Email VARCHAR(100) UNIQUE,
                    Membership_Type
                    ENUM('Regular','Premium')
                ) AUTO_INCREMENT=101
            """
            self.database.cursor.execute(query)
            self.database.commit()
            print("Members table created successfully")
        except mysql.connector.Error as e:
            self.database.rollback()
            print("Unable to create Members table")
            print("Error:", e)
        finally:
            self.database.close()
    def add_member(self):
        try:
            self.database.connect()
            Member_Name = input("Enter the member name: ")
            Phone = input("Enter the phone number: ")
            Email = input("Enter the email: ")
            Membership_Type = input("Enter the membership type (Regular/Premium): ")
            if (not Member_Name or not Phone or not Email or not Membership_Type):
                print("Fields must be filled")
                return
            if len(Phone) != 10:
                print("Phone number should be 10 digits")
                return
            if Membership_Type not in ("Regular","Premium"):
                print("Select Regular or Premium")
                return
            if "@" not in Email:
                print("Enter a valid email")
                return
            query = """
                INSERT INTO Members
                (Member_Name,Phone,Email,Membership_Type)
                VALUES(%s,%s,%s,%s)
            """
            values = (Member_Name,Phone,Email,Membership_Type)
            self.database.cursor.execute(query,values)
            self.database.commit()
            print(self.database.cursor.rowcount,
                "Member added")
        except mysql.connector.Error as e:
            self.database.rollback()
            print("Unable to add member")
            print("Error:", e)
        finally:
            self.database.close()
    def update_member(self):
        try:
            self.database.connect()
            Member_id = input("Enter the member id to update: ")
            New_Phone = input("Enter the new phone number: ")
            New_Email = input("Enter the new email: ")
            if (not Member_id or not New_Phone or not New_Email):
                print("Fields must be filled")
                return
            if len(New_Phone) != 10:
                print("Phone number should be 10 digits")
                return
            if "@" not in New_Email:
                print("Enter a valid email")
                return
            query = """
                UPDATE Members
                SET Phone=%s,
                    Email=%s
                WHERE Member_id=%s
            """
            values = (New_Phone,New_Email,Member_id)
            self.database.cursor.execute(
                query,values)
            self.database.commit()
            if self.database.cursor.rowcount > 0:
                print(self.database.cursor.rowcount,"Record updated")
            else:
                print("No matching record found")
        except mysql.connector.Error as e:
            self.database.rollback()
            print("Unable to update record")
            print("Error:", e)
        finally:
            self.database.close()
    def delete_member(self):
        try:
            self.database.connect()
            Member_id = input("Enter the member id: ")
            if not Member_id:
                print("Member id cannot be empty")
                return
            check_query = """
                SELECT *
                FROM Borrow
                WHERE Member_id=%s
                AND Status='BORROWED'
            """
            self.database.cursor.execute(check_query,(Member_id,))
            if self.database.cursor.fetchone():
                print(
                    "Cannot delete member because "
                    "the member has a borrowed book")
                return
            query = """
                DELETE FROM Members
                WHERE Member_id=%s
            """
            self.database.cursor.execute(
                query,
                (Member_id,))
            self.database.commit()
            if self.database.cursor.rowcount > 0:
                print(self.database.cursor.rowcount,"Record deleted")
            else:
                print("No matching member found")
        except mysql.connector.Error as e:
            self.database.rollback()
            print("Unable to delete member")
            print("Error:", e)
        finally:
            self.database.close()
    def display_all(self):
        try:
            self.database.connect()
            query = """
                SELECT *
                FROM Members
            """
            self.database.cursor.execute(query)
            records = (self.database.cursor.fetchall())
            print("\n======== ALL MEMBERS ========")
            if records:
                for record in records:
                    print(record)
            else:
                print("No records found")
        except mysql.connector.Error as e:
            print("Unable to retrieve records")
            print("Error:", e)
        finally:
            self.database.close()
    def search_member(self):
        try:
            self.database.connect()
            Member_id = input("Enter the member id to search: ")
            if not Member_id:
                print("Member id cannot be empty")
                return
            query = """
                SELECT *
                FROM Members
                WHERE Member_id=%s
            """
            self.database.cursor.execute(
                query,
                (Member_id,)
            )
            record = (
                self.database.cursor.fetchone())
            if record:
                print("Record found:",record)
            else:
                print("No record found")
        except mysql.connector.Error as e:
            print("Unable to retrieve record")
            print("Error:", e)
        finally:
            self.database.close()
class Borrows:
    def __init__(self, database):
        self.database = database
    def create_table(self):
        try:
            self.database.connect()
            query = """
                CREATE TABLE IF NOT EXISTS Borrow(
                    Borrow_id INT AUTO_INCREMENT PRIMARY KEY,
                    Book_id INT,
                    Member_id INT,
                    Borrow_date DATE DEFAULT (CURRENT_DATE),
                    Return_date DATE NULL,
                    Status
                    ENUM('BORROWED','RETURNED')
                    DEFAULT 'BORROWED',
                    FOREIGN KEY(Book_id)
                    REFERENCES Books(Book_id),
                    FOREIGN KEY(Member_id)
                    REFERENCES Members(Member_id)
                ) AUTO_INCREMENT=1001
            """
            self.database.cursor.execute(query)
            self.database.commit()
            print("Borrow table created successfully")
        except mysql.connector.Error as e:
            self.database.rollback()
            print("Unable to create Borrow table")
            print("Error:", e)
        finally:
            self.database.close()
    def borrow_book(self):
        try:
            self.database.connect()
            Member_id = input("Enter the Member ID: ")
            Book_id = input("Enter the Book ID: ")
            check_member = """
                SELECT *
                FROM Members
                WHERE Member_id=%s
            """
            self.database.cursor.execute(
                check_member,
                (Member_id,))
            if not self.database.cursor.fetchone():
                print("Member does not exist")
                return
            check_book = """
                SELECT *
                FROM Books
                WHERE Book_id=%s
            """
            self.database.cursor.execute(
                check_book,
                (Book_id,))
            if not self.database.cursor.fetchone():
                print("Book does not exist")
                return
            check_copy = """
                SELECT Available_copies
                FROM Books
                WHERE Book_id=%s
            """
            self.database.cursor.execute(
                check_copy,
                (Book_id,))
            copy_record = (self.database.cursor.fetchone())
            available_copies = copy_record[0]
            if available_copies <= 0:
                print("No book copies available")
                return
            check_borrow = """
                SELECT Borrow_id
                FROM Borrow
                WHERE Book_id=%s
                AND Member_id=%s
                AND Status='BORROWED'
            """
            self.database.cursor.execute(
                check_borrow,
                (Book_id, Member_id))
            if self.database.cursor.fetchone():
                print("Member has already borrowed ""this book")
                return
            borrow_record = """
                INSERT INTO Borrow
                (Book_id, Member_id)
                VALUES(%s,%s)
            """
            self.database.cursor.execute(borrow_record,(Book_id, Member_id))
            available_copy = """
                UPDATE Books
                SET Available_copies =
                    Available_copies - 1
                WHERE Book_id=%s
            """
            self.database.cursor.execute(available_copy,(Book_id,))
            self.database.commit()
            print("Book borrowed successfully")
        except mysql.connector.Error as e:
            self.database.rollback()
            print("Unable to borrow book")
            print("Error:", e)
        finally:
            self.database.close()
    def returnbook(self):
        try:
            self.database.connect()
            Borrow_id = input("Enter your Borrow ID: ")
            check_borrow = """
                SELECT *
                FROM Borrow
                WHERE Borrow_id=%s
                AND Status='BORROWED'
            """
            self.database.cursor.execute(check_borrow,(Borrow_id,))
            record = (self.database.cursor.fetchone())
            if record is None:
                print("No such borrow record found")
                return
            set_return = """
                UPDATE Borrow
                SET Status='RETURNED',
                    Return_date=CURRENT_DATE
                WHERE Borrow_id=%s
            """
            self.database.cursor.execute(set_return,(Borrow_id,))
            available_copy = """
                UPDATE Books
                SET Available_copies =
                    Available_copies + 1
                WHERE Book_id =
                    (
                        SELECT Book_id
                        FROM Borrow
                        WHERE Borrow_id=%s
                    )
            """
            self.database.cursor.execute(available_copy,(Borrow_id,))
            self.database.commit()
            print("Book returned successfully")
        except mysql.connector.Error as e:
            self.database.rollback()
            print("Unable to return book")
            print("Error:", e)
        finally:
            self.database.close()
    def displayborrowbooks(self):
        try:
            self.database.connect()
            query = """
                SELECT
                    r.Borrow_id,
                    b.Book_Title,
                    m.Member_Name,
                    r.Borrow_date,
                    r.Status
                FROM Borrow r
                JOIN Books b
                    ON r.Book_id = b.Book_id
                JOIN Members m
                    ON r.Member_id = m.Member_id
                WHERE r.Status='BORROWED'
            """
            self.database.cursor.execute(query)
            borrow = (self.database.cursor.fetchall())
            print("\n----- CURRENTLY BORROWED BOOKS -----")
            if borrow:
                for row in borrow:
                    (Borrow_id,Book_Title,Member_Name,Borrow_date,Status) = row
                    print(f"BorrowID: {Borrow_id} | "f"Title: {Book_Title} | "f"Member: {Member_Name} | "f"Borrowed: {Borrow_date} | "f"Status: {Status}")
            else:
                print("No books currently borrowed")
        except mysql.connector.Error as e:
            print("Unable to retrieve borrowed books")
            print("Error:", e)
        finally:
            self.database.close()
    def memberhistory(self):
        try:
            self.database.connect()
            Member_id = input("Enter Member ID: ")
            check_member = """
                SELECT *
                FROM Members
                WHERE Member_id=%s
            """
            self.database.cursor.execute(check_member,(Member_id,))
            if not self.database.cursor.fetchone():
                print("Member does not exist")
                return
            displayhistory = """
                SELECT
                    m.Member_Name,
                    b.Book_id,
                    b.Book_Title,
                    b.price,
                    r.Borrow_date,
                    r.Return_date,
                    r.Status
                FROM Borrow r
                JOIN Books b
                    ON r.Book_id = b.Book_id
                JOIN Members m
                    ON r.Member_id = m.Member_id
                WHERE m.Member_id=%s
            """
            self.database.cursor.execute(displayhistory,(Member_id,))
            history = (self.database.cursor.fetchall())
            print("\n----- MEMBER HISTORY -----")
            if history:
                for row in history:
                    (Member_Name,Book_id,Book_Title,price,Borrow_date,Return_date,Status) = row
                    print(f"MEMBER: {Member_Name} | "f"BOOK ID: {Book_id} | "f"BOOK TITLE: {Book_Title} | "f"PRICE: {price} | "f"BORROWED DATE: {Borrow_date} | "f"RETURNED DATE: {Return_date} | "f"STATUS: {Status}")
            else:
                print("No member history")
        except mysql.connector.Error as e:
            print("Unable to fetch member history")
            print("Error:", e)
        finally:
            self.database.close()
    def availablebook(self):
        try:
            self.database.connect()
            query = """
                SELECT *
                FROM Books
                WHERE Available_copies > 0
            """
            self.database.cursor.execute(query)
            books = (self.database.cursor.fetchall())
            print("\n----- AVAILABLE BOOKS -----")
            if books:
                for row in books:
                    (Book_id,ISBN,Book_Title,Author,Category,price,Available_copies) = row
                    print(f"BOOK ID: {Book_id} | "f"ISBN: {ISBN} | "f"TITLE: {Book_Title} | "f"AUTHOR: {Author} | "f"CATEGORY: {Category} | "f"PRICE: {price} | "f"AVAILABLE COPIES: "f"{Available_copies}" )
            else:
                print("No available books")
        except mysql.connector.Error as e:
            print("Unable to fetch available books")
            print("Error:", e)
        finally:
            self.database.close()
    def overduebook(self):
        try:
            self.database.connect()
            query = """
                SELECT
                    b.Book_id,
                    b.Book_Title,
                    m.Member_Name,
                    r.Borrow_date,
                    r.Borrow_date +
                    INTERVAL 14 DAY AS Due_date
                FROM Borrow r
                JOIN Books b
                    ON r.Book_id = b.Book_id
                JOIN Members m
                    ON r.Member_id = m.Member_id
                WHERE r.Status='BORROWED'
                AND r.Borrow_date +
                    INTERVAL 14 DAY < CURDATE()
            """
            self.database.cursor.execute(query)
            overdue = (self.database.cursor.fetchall())
            print("\n----- OVERDUE BOOKS -----")
            if overdue:
                for row in overdue:
                    (Book_id,Book_Title,Member_Name,Borrow_date,Due_date) = row
                    print(f"BOOK ID: {Book_id} | "f"TITLE: {Book_Title} | "f"MEMBER: {Member_Name} | "f"BORROWED: {Borrow_date} | "f"DUE: {Due_date}")
            else:
                print("No overdue books")
        except mysql.connector.Error as e:
            print("Unable to fetch overdue books")
            print("Error:", e)
        finally:
            self.database.close()
db = Database(
    "localhost",
    "root",
    "Maalu@2529",
    "LibraryDB"
)
Book = Books(db)
member = Members(db)
borrow = Borrows(db)
Book.create_table()
member.create_table()
borrow.create_table()
while True:
    print("\n======================= MENU =======================")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. Display All Books")
    print("5. Search Book")
    print("6. Add Member")
    print("7. Update Member")
    print("8. Delete Member")
    print("9. Display All Members")
    print("10. Search Member")
    print("11. Borrow Book")
    print("12. Return Book")
    print("13. Display Borrowed Books")
    print("14. Member Borrowing History")
    print("15. Display Available Books")
    print("16. Overdue Books")
    print("17. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        Book.add_book()
    elif choice == '2':
        Book.update_Book()
    elif choice == '3':
        Book.delete_Book()
    elif choice == '4':
        Book.display_all()
    elif choice == '5':
        Book.search()
    elif choice == '6':
        member.add_member()
    elif choice == '7':
        member.update_member()
    elif choice == '8':
        member.delete_member()
    elif choice == '9':
        member.display_all()
    elif choice == '10':
        member.search_member()
    elif choice == '11':
        borrow.borrow_book()
    elif choice == '12':
        borrow.returnbook()
    elif choice == '13':
        borrow.displayborrowbooks()
    elif choice == '14':
        borrow.memberhistory()
    elif choice == '15':
        borrow.availablebook()
    elif choice == '16':
        borrow.overduebook()
    elif choice == '17':
        print("Exiting Library Management System...")
        print("Thank you!")
        break
    else:
        print("Invalid choice")
