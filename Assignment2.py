#ATM PIN Verification
print("=========================================")    
class Verify:
    PIN=1234
    def __init__(self,users_Pin):
        self.users_Pin=users_Pin
        if(self.PIN==users_Pin):
            print("Access granted")
        else:
            print("Access Denied")
    def display(self):
        print("Verification of users pin code")
        print("Users pin",self.users_Pin)
ObjVerify=Verify(1245)
ObjVerify.display()
print("=========================================")        
#Box Volume Calculation 
class Box:
    def box_volume(self,width,height,depth):
        self.width=width
        self.height=height
        self.depth=depth
    def get_volume(self):
        self.volume=self.width*self.height*self.depth
        print("Volume:",self.volume)
ObjBox=Box()
ObjBox2=Box()
ObjBox.box_volume(12,23,4)
ObjBox2.box_volume(12,2,1)
ObjBox.get_volume()
ObjBox2.get_volume()
print("=========================================")    
#Box Volume Calculation
class Box:
    def __init__(self,width,height,depth):
        self.width=width
        self.height=height
        self.depth=depth
    def get_volume(self):
        self.get_volume=self.width*self.height*self.depth
        print("Volume:",self.get_volume)
ObjBox3=Box(3,23,4)
ObjBox4=Box(6,7,2)
ObjBox3.get_volume()
ObjBox4.get_volume()
print("=========================================") 
#Billing System for International Customers
class BillingSystem:
    def __init__(self,country_name,language,customer_id,billing_date,amount_outstanding):
        self.country_name=country_name
        self.language=language
        self.customer_id=customer_id
        self.billing_date=billing_date
        self.amount_outstanding=amount_outstanding
    def display_details(self):
        print("Billing info")
        print("Country Name:",self.country_name)
        print("Language:",self.language)
        print("Customer id:",self.customer_id)
        print("Billing date:",self.billing_date)
        if type(self.amount_outstanding)==float:
            print("Amount_outstanding:",self.amount_outstanding)
ObjBillingSystem=BillingSystem("US","English",101,"28-7-2025",2999.00)
ObjBillingSystem1=BillingSystem("Japan","Japanese",123,"28-7-2026",9000.00)
ObjBillingSystem.display_details()
print("=========================================")
ObjBillingSystem1.display_details()
print("=========================================")
#Hospital Management System
class Patient:
    Hospital_name="CityCare Hospital"
    def __init__(self,patient_id,name,age,admitted_days,daily_charge):
        self.patient_id=patient_id
        self.name=name
        self.age=age
        self.admitted_days=admitted_days
        self.daily_charge=daily_charge
    def calculate_bill(self):
        self.total_bill=self.admitted_days*self.daily_charge
        print("Total Bill:",self.total_bill)
    @classmethod
    def change_hospital_name(cls,new_name):
           
           cls.Hospital_name=new_name
           print("Hospital Name changed")
    @staticmethod
    def is_senior(age):
        if age>=60:
            print("True")
        else:
            print("False")
    def __str__(self):
        print("Patient Details")
        print("Patient id   :",self.patient_id)
        print("Name         :",self.name)
        print("Age          :",self.age)
        print("Admitted days:",self.admitted_days)
        print("Daily charge :",self.daily_charge)
print("=========================================")

ObjPatient=Patient(101,"Anu",25,2,1000)
ObjPatient.calculate_bill()
ObjPatient.change_hospital_name("Care Hospital")
ObjPatient.is_senior(25)
ObjPatient.__str__()
print("=========================================")      