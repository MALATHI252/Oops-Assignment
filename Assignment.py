# Product Inventory

class Product:
    Product_name = ""
    price = 0
    stock_quantity = 0

    def add_stock(self, quantity):
        if quantity > 0:
            self.stock_quantity = self.stock_quantity+quantity  

    def sell(self, quantity):
        if quantity <= self.stock_quantity:
            self.stock_quantity = self.stock_quantity -quantity  

    def display(self):
        print("Product Name:", self.Product_name)
        print("Price:", self.price)
        print("Stock Quantity:", self.stock_quantity)


ObjProduct = Product()

ObjProduct.Product_name = "Computer"
ObjProduct.price = 75000
ObjProduct.stock_quantity= 20

ObjProduct.add_stock(10)
ObjProduct.sell(2)
ObjProduct.display()
print("==================================================")

# Employee Salary

class Employee:
    name = ""
    base_salary = 0
    years_of_service = 0

    def calculate_bonus(self):
        self.bonus = self.base_salary * 5 / 100 * self.years_of_service

    def calculate_salary(self):
        self.total_salary = self.base_salary +self.bonus

    def display(self):
        print("Name:", self.name)
        print("Base Salary:", self.base_salary)
        print("Years of Service:", self.years_of_service)
        print("Bonus salary:",self.bonus)
        print("Total salary:",self.total_salary)


ObjEmployee = Employee()
ObjEmployee.name="Meera"
ObjEmployee.base_salary=25000
ObjEmployee.years_of_service=5
ObjEmployee.calculate_bonus()
ObjEmployee.calculate_salary()
ObjEmployee.display()
print("==================================================")
#Bank Account
class BankAccount:
    account_holder=""
    account_number=0
    balance=0
    def deposit(self,amount):
        if(amount>0):
            self.balance=self.balance+amount
        else:
            print("Deposit amount must be greater than 0")
    def withdraw(self,amount):
        if (amount)<=self.balance:
            print("Withdraw success")
    def display(self):
        print("Account_holder:",self.account_holder)
        print("Account Number:",self.account_number)
        print("balance",self.balance)
ObjBankAccount=BankAccount()
ObjBankAccount.account_holder="Anu"
ObjBankAccount.account_number=1234455678923213
ObjBankAccount.balance=500
ObjBankAccount.deposit(2000)
ObjBankAccount.withdraw(200)
ObjBankAccount.display()
print("==================================================")
#student Result
class StudentResult:
    student_name=""
    roll_number=0
    marks=0
    def calculate_result(self):
        if self.marks >= 35:
            print("Pass")
        else:
            print("Fail")
        
    def calculate_grade(self):
        if(self.marks>90):
            print("A")
        elif 75 <= self.marks <= 89:
            print("B")
        elif 60 <= self.marks <= 74:
            print("C")
        else:
            print("D")
ObjStudentResult=StudentResult()
ObjStudentResult.student_name="Anushma"
ObjStudentResult.roll_number=6
ObjStudentResult.marks=89
ObjStudentResult.calculate_grade()
ObjStudentResult.calculate_result()
print("==================================================")
#Library Book
class LibraryBook:
    book_title=""
    author=""
    total_copies=0
    issued_copies=0
    def issue_book(self,quantity):
        if quantity>0 and quantity<=(self.total_copies-self.issued_copies):
            self.issued_copies=self.issued_copies+quantity
            print("Issue book")
    def return_book(self,quantity):
        if(quantity<=self.issued_copies):
            self.issued_copies=self.issued_copies-quantity
            print("Return book")
    def display(self):
        print("Book title",self.book_title)
        print("Author",self.author)
        print("Total copies",self.total_copies)
        print("issued copies",self.issued_copies)
ObjLibraryBook=LibraryBook()
ObjLibraryBook.book_title="Atomic Habits"
ObjLibraryBook.author="James"
ObjLibraryBook.total_copies=50
ObjLibraryBook.issued_copies=25
ObjLibraryBook.issue_book(5)
ObjLibraryBook.return_book(2)
ObjLibraryBook.display()
print("==================================================")
#Hotel Room Booking
class HotelRoom:
    room_number = 0
    room_type = ""
    total_rooms = 0
    booked_rooms = 0

    def book_room(self, rooms):
        if rooms > 0 and rooms <= (self.total_rooms - self.booked_rooms):
            self.booked_rooms += rooms
            print("Room booked successfully")
        else:
            print("Rooms not available")

    def cancel_room(self, rooms):
        if rooms > 0 and rooms <= self.booked_rooms:
            self.booked_rooms -= rooms
            print("Booking cancelled")
        else:
            print("Invalid cancellation")

    def display(self):
        print("Room Number:", self.room_number)
        print("Room Type:", self.room_type)
        print("Total Rooms:", self.total_rooms)
        print("Booked Rooms:", self.booked_rooms)


obj = HotelRoom()
obj.room_number = 101
obj.room_type = "Deluxe"
obj.total_rooms = 20
obj.booked_rooms = 5

obj.book_room(4)
obj.cancel_room(2)
obj.display()

print("==================================================")
#Movie ticket booking
class MovieTicket:
    movie_name = ""
    total_seats = 0
    booked_seats = 0

    def book_seats(self, seats):
        if seats > 0 and seats <= (self.total_seats - self.booked_seats):
            self.booked_seats += seats
            print("Seats booked")
        else:
            print("Seats not available")

    def cancel_seats(self, seats):
        if seats > 0 and seats <= self.booked_seats:
            self.booked_seats -= seats
            print("Seats cancelled")
        else:
            print("Invalid cancellation")

    def display(self):
        print("Movie:", self.movie_name)
        print("Total Seats:", self.total_seats)
        print("Booked Seats:", self.booked_seats)


obj = MovieTicket()
obj.movie_name = "Leo"
obj.total_seats = 100
obj.booked_seats = 40

obj.book_seats(10)
obj.cancel_seats(5)
obj.display()
print("==================================================")
#Mobile Recharge
class MobileRecharge:
    mobile_number = ""
    balance = 0

    def recharge(self, amount):
        if amount > 0:
            self.balance += amount
            print("Recharge successful")
        else:
            print("Invalid recharge amount")

    def use_balance(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Balance used")
        else:
            print("Insufficient balance")

    def display(self):
        print("Mobile Number:", self.mobile_number)
        print("Balance:", self.balance)


obj = MobileRecharge()
obj.mobile_number = "9876543210"
obj.balance = 100

obj.recharge(200)
obj.use_balance(150)
obj.display()
print("==================================================")
#Car fuel Management
class Car:
    car_name = ""
    fuel_capacity = 0
    current_fuel = 0

    def refill_fuel(self, litres):
        if litres > 0:
            if self.current_fuel + litres <= self.fuel_capacity:
                self.current_fuel += litres
                print("Fuel added")
            else:
                print("Fuel exceeds capacity")

    def drive(self, litres):
        if litres <= self.current_fuel:
            self.current_fuel -= litres
            print("Car driven")
        else:
            print("Not enough fuel")

    def display(self):
        print("Car:", self.car_name)
        print("Fuel Capacity:", self.fuel_capacity)
        print("Current Fuel:", self.current_fuel)


obj = Car()
obj.car_name = "Hyundai"
obj.fuel_capacity = 50
obj.current_fuel = 20

obj.refill_fuel(15)
obj.drive(10)
obj.display()
print("==================================================")
#shopping Cart
class ShoppingCart:
    item_name = ""
    item_price = 0
    quantity = 0

    def add_item(self, qty):
        if qty > 0:
            self.quantity += qty
            print("Item added")
        else:
            print("Invalid quantity")

    def remove_item(self, qty):
        if qty > 0 and qty <= self.quantity:
            self.quantity -= qty
            print("Item removed")
        else:
            print("Not enough items")

    def display(self):
        print("Item Name:", self.item_name)
        print("Price:", self.item_price)
        print("Quantity:", self.quantity)


obj = ShoppingCart()
obj.item_name = "Pen"
obj.item_price = 20
obj.quantity = 10

obj.add_item(5)
obj.remove_item(3)
obj.display()