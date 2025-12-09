# #Public Member

# class Car:
#    def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#     def display(self):
#         print("f Car:{self.brand}{self.model}")

# car = Car("Toyoto","Corolla")

# print(car.brand)
# print(car.model)

# car.display()


#protected member


class Car:  
    def __init__(self, brand, model, engine):  
        self.brand = brand   
        self._model = model   
        self._engine = engine    
  
    def _show_details(self):   
        print(f"Brand: {self.brand}, Model: {self._model}, Engine: {self._engine}")  
  
class ElectricCar(Car):  
    def __init__(self, brand, model, battery_capacity):  
        super().__init__(brand, model, "Electric")  
        self.battery_capacity = battery_capacity  
  
    def show_info(self):  
        self._show_details()   
        print(f"Battery: {self.battery_capacity} kWh")  
    
tesla = ElectricCar("Tesla", "Model S", 100)  
    
tesla.show_info()  
  
print(tesla._model)  


#Private Member

class BankAccount:  
    def __init__(self, account_number, balance):  
        self.account_number = account_number    
        self.__balance = balance   
  
    def get_balance(self):  
        return self.__balance  
  
    def set_balance(self, amount):  
        if amount >= 0:  
            self.__balance = amount  
        else:  
            print("Invalid amount! Balance cannot be negative.")  
   
account = BankAccount("123456789", 1000)  
  
  
print(account.account_number) 

   
print(account.get_balance())   
   
account.set_balance(2000)  
print(account.get_balance())
  
 
print(account._BankAccount__balance)  






 









