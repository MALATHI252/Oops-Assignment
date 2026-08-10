#Person and Student
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_inf(self):
        print("Name        :",self.name)
        print("Age         :",self.age)
class Student(Person):
    def __init__(self, name, age,roll_number,marks):
        super().__init__(name, age)
        self.roll_number=roll_number
        self.marks=marks
    def details(self):
        self.display_inf()
        print("Roll Number :",self.roll_number)
        print("Marks       :",self.marks)
objStudent=Student("Anu",12,11,100)

objStudent.details()
print("=================================")
#Employee and Manager
class Employee:
    def __init__(self,employee_id,employee_name):
        self.employee_id=employee_id
        self.employee_name=employee_name
    def disp_Employee(self):
        print("Employee_id    :",self.employee_id)
        print("Employee Name  :",self.employee_id)

class Manager(Employee):
    def __init__(self,employee_id,employee_name,department):
        super().__init__(employee_id,employee_name)
        self.department=department
    def details(self):
        self.disp_Employee()
        print("Department  :",self.department)
ObjManager=Manager(101,"Meera","IT")
ObjManager.details()
print("=================================")
#Vehicle and Car
class Vehicle:
    def start(self):
        print("Car is being started")
class Car(Vehicle):
    def drive(self):
        print("Car is to be driven")
objVehicle=Car()
objVehicle.start()
objVehicle.drive()
print("=================================")
#Bank Account
class Account:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.account_balance=balance
    def display(self):
        print("Account Number  :",self.account_number)
        print("Balance         :",self.account_balance)
class SavingsAccount(Account):
    def __init__(self,account_number,account_balance,interest_amount=0):
        super().__init__(account_number,account_balance)
        self.interest=interest_amount
    def calculate_interest(self):
        self.display()
        interest_amount=self.account_balance*self.interest/100
        print("Interest         :",interest_amount)
account_number=input("Enter the account Number   :")
account_balance=float(input("Enter the account Balance :"))
interest_amount=float(input("Enter the interest amount :"))
objAccount=SavingsAccount(account_number,account_balance,interest_amount)
objAccount.calculate_interest()
print("=================================")
#Library Member System
class Member:
    def __init__(self,member_id,member_name):
        self.member_id=member_id
        self.member_name=member_name
    def details(self):
        print("Member Id   :",self.member_id)
        print("Member Name :",self.member_name)
class LibraryMember(Member):
    def __init__(self, member_id, member_name,books_issued):
        super().__init__(member_id, member_name)
        self.books_issued=books_issued
    def complete_details(self):
        self.details()
        print("Books issued   :",self.books_issued)
member_id=input("Enter the member id       :")
member_name=input("Enter the member name   :")
books_issued=input("Enter the books_issued :")
objMember=LibraryMember(member_id,member_name,books_issued)
print("=================================")      

        
   



        