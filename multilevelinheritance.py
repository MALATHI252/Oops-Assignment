#Office Machine System

class Printer:
    def printer(Self):
        print("Printing the doc")
class scanner:
    def scanner(self):
        print("Scanning the doc")
class office(Printer,scanner):
    def display(self):
        pass
Obj=office()
Obj.printer()
Obj.scanner()

print("==================================")     
#Online Payment Application
class Onpayment:
    def onlinePayment(self):
        print("THis is online payment")
class cashPayment:
    def cashPayment(self):
        print("This is cash payment")
class System(Onpayment,cashPayment):
    def display(self):
        pass
Obj=System()
Obj.onlinePayment()
Obj.cashPayment()

print("==================================")   

#Smart phone features
class callfn:
    def callingfunctionality(self):
        print("This is calling functionality")
class camfn:
    def camfunctionality(self):
        print("This is camera functionality")
class systemfn(callfn,camfn):
    def details(self):
        pass
Obj=systemfn()
Obj.callingfunctionality()
Obj.camfunctionality()

print("==================================")   
#Employee information system
class pers_info():
    def personal_info(self):
        print("This is personal information")
class prof_info():
    def professional_info(self):
        print("This is professional information")
class system_info(pers_info,prof_info):
    def system_information(self):
        pass
Obj=system_info()
Obj.personal_info()
Obj.professional_info()
print("==================================")   
#Logging and db mgmt
class logging_connection:
    def logging_connect(self):
        print("This is the logging functionality")
class database_connection:
    def database_connect(self):
        print("This is the database connectivity")
class main_application(logging_connection,database_connection):
    def details(self):
        pass
Obj=main_application()
Obj.logging_connect()
Obj.database_connect()
print("==================================")  
#Educational Portal
class academic_portal:
    def academic_details(self):
        print("This is the academic details")
class personal_detail:
    def personal_details(self):
        print("This is the personal details report")
class system_profile(academic_portal,personal_detail):
    def system_profiledetails(self):
        pass
Obj=system_profile()
Obj.academic_details()
Obj.personal_details()
print("==================================")  
#Vehicle mgmt systme
class engine:
    def engine_details(self):
        print("This is the vehicle engine details")
class safety:
    def safety_feature(self):
        print("This is the safety feature handled by different modules")
class System(engine,safety):
    def System(self):
        pass
Obj=System()
Obj.engine_details()
Obj.safety_feature()
print("==================================")  