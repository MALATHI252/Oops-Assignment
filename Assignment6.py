#Shape Area Calculator
from abc import ABC,abstractmethod
class Shape(ABC):
    def detailsArea(self):
        print("Details of the Area")

    @abstractmethod #because it doesnt contain body
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area(self):
        return self.length*self.breadth
       
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14*self.radius*self.radius
rectangle=Rectangle(2,6)
circle=Circle(3)
print("Rectangle Area:",rectangle.area())
print("Circle Area:",circle.area())
print("=====================================")
# Vehicle Engine System
from abc import ABC,abstractmethod
class Vehicle(ABC):
    def details(self):
        print("Vehicle Engine System")
    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        print("car engine is started")
    def car_details(self):
        print("This is car")
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine is started")
    def bike_details(self):
        print("This is bike")
car=Car()
car.details()
car.car_details()
bike=Bike()
bike.bike_details()
car.start_engine()
bike.start_engine()
print("=====================================")
#Bank Account Operations
from abc import ABC,abstractmethod
class BankAccount:

    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
class SavingsAccount(BankAccount):
    def __init__(self,amount):
        self.amount=amount
    def deposit(self,amount):
        self.amount=self.amount+amount
    def deposit(self,amount):
        self.amount=self.amount-amount
        #Bank Account Operations
from abc import ABC,abstractmethod
class BankAccount:

    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
class SavingsAccount(BankAccount):
    def __init__(self,amount):
        self.amount=amount
    def deposit(self, amount):
        self.amount=self.amount+amount
        print(f"Deposited ${self.amount}")
    def withdraw(self, amount):
        self.amount=self.amount-amount
        print(f"Withdrwan ${self.amount}")
    def account_info(self):
        print(f"Savings Account Balance: ${self.amount}")

class CurrentAccount(BankAccount):
    def __init__(self,amount):
        self.amount=amount
    def deposit(self, amount):
        self.amount=self.amount+amount
        print(f"Deposited ${self.amount}")
    def withdraw(self, amount):
        self.amount=self.amount-amount
        print(f"Withdrwan ${self.amount}")
        
    def account_info(self):
       
        print(f"Current Account Balance: ${self.amount}")
amount=500
account=SavingsAccount(amount)
account.deposit(200)
account.withdraw(3000)
account.account_info()
account1=CurrentAccount(amount)
account1.deposit(200)
account1.withdraw(3000)
account1.account_info()
print("=====================================")

#Payment Gateway System
from abc import  ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def make_payment(amount):
        pass
class CreditCardPayement(Payment):
    def make_payment(self,amount):
        print(f"Paid ${amount}using Credit Card")


class UPIPayment(Payment):
    def make_payment(self,amount):
        print(f"Paid ${amount}using UPI")

class NetBankingPayment(Payment):
    def make_payment(self,amount):
        print(f"Paid ${amount}using Net Banking")
Payment1=CreditCardPayement()
Payment1.make_payment(2000)
Payment2=UPIPayment()
Payment2.make_payment(1000)
Payment3=NetBankingPayment()
Payment3.make_payment(8000)
print("=====================================")
#Notification System
from abc import ABC,abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass
class EmailNotification(Notification):
    def send(self,message):
        print(f"{message} is notified through Email")
class SMSNotification(Notification):
    def send(self,message):
        print(f"{message} is notified through SMS")
class PushNotification(Notification):
    def send(self,message):
        print(f"{message} is sent through push notification")
message="Hiii"
notify=EmailNotification()
notify.send(message)
notify1=SMSNotification()
notify1.send(message)
notify2=PushNotification()
notify2.send(message)
print("=====================================")
#Online Food delivery app
from abc import ABC,abstractmethod
class FoodOrder(ABC):
    @abstractmethod
    def place_order(self):
        pass
    @abstractmethod
    def calculate_bill(self):
        pass
class VegOrder(FoodOrder):
    def place_order(self):
        print(f"Veg Order placed successfully")
    def calculate_bill(self):
        return 250
       
class NonVegOrder(FoodOrder):
    def place_order(self):
        print(f"Non Veg Order placed successfully")
    def calculate_bill(self):
        return 500
order=VegOrder()
order.place_order()
order.calculate_bill()
order1=NonVegOrder()
order1.place_order()
order1.calculate_bill()
print("=====================================")
#Abstract Login System
from abc import ABC,abstractmethod
class LoginSystem(ABC):
    @abstractmethod
    def login(self):
        pass
class AdminLogin(LoginSystem):
    def login(self):
        print("Admin login successfull")


class UserLogin(LoginSystem):
    def login(self):
        print("User login successful")
admin=AdminLogin()
admin.login()
user=UserLogin()
user.login()
print("=====================================")