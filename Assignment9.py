# #School Management System
from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self,ID):
        self._ID=ID
    @abstractmethod
    def get_role_details(self):
        pass
    def display_id(self):
        print("The id is:",self._ID)
class Teacher(Person):
    def __init__(self,ID,sub,dept):
        super().__init__(ID)
        self.sub=sub
        self.dept=dept
    def get_role_details(self):
        
        print(f"The subject is {self.sub} and the department is {self.dept}")
ObjTeacher=Teacher(101,"Semiconductor","ECE")
ObjTeacher.display_id()
ObjTeacher.get_role_details()