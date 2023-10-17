from abc import ABC, abstractmethod
from  Shop import Shop
class User:
    customers = []
    sellers = []
    def __init__(self,name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password
        


class Seller(User):
    
    def __init__(self,name, email, password) -> None:
        self.s_wallet = 0
        self.sellers.append(self)
        super().__init__(name, email, password)
    
    

class Customer(User):
    
    def __init__(self,name, email, password) -> None:
        self.c_wallet = 0
        self.bill_due = 0
        self.customers.append(self)
        super().__init__(name, email, password)

    def buy_Product(self, customer, pName):
            for item in Shop.products:
                 if item.name == pName:
                      self.bill_due += item.price 
                      print(f'{customer.name} placed an order')
                      break
           
            

    


    

