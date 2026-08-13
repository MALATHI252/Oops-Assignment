#Electricity Bill Calculation System
class ElectricityBill:
    def calculate_bill(self,units):
        self.units=units
        BillAmount=units*5
        print("The Bill Amount is:",BillAmount)
class DomesticBill(ElectricityBill):
    def calculate_bill(self, units):
       self.units=units
       if units<=100:
           BillAmount=self.units*5
           print("DomesticBill amount is:",BillAmount)
       else:
           BillAmount=(100*5+(self.units-100)*3)
           print("DomesticBill amount is:",BillAmount)
class CommercialBill(ElectricityBill):
    def calculate_bill(self, units):
        self.units=units
        BillAmount=self.units*8
        Tax=BillAmount*0.10
        print("commercial Bill Amount is:",BillAmount+Tax)


ObjDomesticBill=DomesticBill()
ObjCommercialBill=CommercialBill()
ObjElectricityBill=ElectricityBill()
ObjDomesticBill.calculate_bill(120)
ObjCommercialBill.calculate_bill(20)
ObjElectricityBill.calculate_bill(26)