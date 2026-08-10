#Person,Student,Result
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Student:
    def __init__(self,roll_number,marks):
        self.roll_number=roll_number
        self.marks=marks
    def detail(self):
        print("Roll number:",self.roll_number)
        print("Marks:",self.marks)
class Result(Person,Student):
    def __init__(self,name,age,roll_number,marks):
        Person.__init__(self,name,age)
        Student.__init__(self,roll_number,marks)
    def results(self):
        self.details()
        self.detail()
Obj=Result("Anu",12,11,90)
Obj.results()
print("=====================================")
#Animal Hierarchy
class Animal:
    def eat(self):
        print("Dog is eating")
class Dog(Animal):
    def bark(self):
        print("Dog will bark")
class Puppy(Dog):
    def play(self):
        print("Puppy plays well")
Obj=Puppy()
Obj.eat()
Obj.bark()
Obj.play()
print("=====================================")
#Company,Employee,Salary
class Company:
    def __init__(self,company_name):
        self.company_name=company_name
class Employee(Company):
    def __init__(self,company_name,employee_id,name):
        Company.__init__(self,company_name)
        self.employee_id=employee_id
        self.name=name
class Salary(Employee):
    def __init__(self,company_name,employee_id,name,salary):
        
        Employee.__init__(self,company_name,employee_id,name)
        self.salary=salary
    def details(self):
        print("Company Name  :",self.company_name)
        print("Employee Id   :",self.employee_id)
        print("Employee Name  :",self.name)
        print("Salary        :",self.salary)
Obj=Salary("TCS",11,"Meera",20000)
Obj.details()
print("=====================================")
        

        