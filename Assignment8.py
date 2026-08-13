#Employee Payroll Management System
from abc import ABC,abstractmethod
class Employee(ABC):
     def __init__(self,basic_salary):
          self._basic_salary=basic_salary
     @abstractmethod
     def calculate_salary(self):
          pass
     def display_basic_salary(self):
          
          print("The basic salary is:",self._basic_salary)

class FullTimeEmployee(Employee):
     def calculate_salary(self):
          HRA=0.20*self._basic_salary
          DA=0.10*self._basic_salary
          Total_Salary=self._basic_salary+HRA+DA
          print("total salary:",Total_Salary)
ObjFullTimeEmployee=FullTimeEmployee(20000)

ObjFullTimeEmployee.display_basic_salary()
ObjFullTimeEmployee.calculate_salary()