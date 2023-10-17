from abc import ABC, abstractmethod
class Shop:
    products = []
    def __init__(self, name) -> None:
        self.name = name
        self.customers = []
        self.sellers = []
        # self.products = []
    

    
    # def add_customer(self, customer) :
    #     self.customers.append(customer)
    
    # def add_sellers(self, seller) :
    #     self.sellers.append(seller)

    def add_Product(self, product) :
        self.products.append(product)
    
    def update_stock(self,pName, pStock):
        for prod in self.products:
            if prod.name == pName:
                prod.stock = pStock
                print(f'{prod.name} stock status updated successfully!')
                break


    def show_product(self):
        for product in self.products:
            if product.stock is True:
                print(f'Product Name: {product.name} Price: {product.price} Stock: {product.stock}')
            else:
                print('Not Found')
        print('Looper baire')
    
    

    def __repr__(self) -> str:
        print(f'Welcome to {self.name}')

class Product:
      def __init__(self, name, price, stock) -> None:
          self.name = name
          self.price = price
          self.stock = stock


# class Order:
#     def __init__(self, customer, items) -> None:
#         self.customer = customer
#         self.items = items
#         total = 0
#         for item in items:
#             if item in 
        
#         self.bill = total

          





    