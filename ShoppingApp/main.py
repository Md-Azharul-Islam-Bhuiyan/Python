from Shop import Shop, Product
from Users import User, Customer, Seller
def main():
  
  shop = Shop('Saklain Super Shop')
   
  # seller_1 = Seller('karim','karim@gmail.com', '12s')
  # shop.add_sellers(seller_1)


  # prod1 = Product("Iphone", 120000, True)
  # shop.add_Product(prod1)

  # prod2 = Product("macBook", 120000, False)
  # shop.add_Product(prod2)

  # shop.show_product()
  
  # cus_1 = Customer('Hakim','hak@gmail.com','023')
  
  # ord_1 = Order(cus_1,[prod1])
  # cus_1.placed_order(ord_1)
  
  print(f'---------Welcome to  {shop.name}-------------')
  cur_user = None
  cur_seller = None
  while True:
    print('------------SELECT USERS TYPE-----------')
    print('1. SELLER')
    print('2. CUSTOMER')
    print('3. Exit')
    op = int(input('ENTER OPTIONS:'))
    
    if op == 1:
      while True:
        if cur_seller == None:
          print('NO SELLER LOGIN!!')
          ch = input('LOGIN OR RESGISTER (L/R)?:')

          if ch == 'R':
            nm = input('ENTER NAME:')
            em = input('ENTER EMAIL:')
            passw = input('ENTER PASSWORD:')

            cur_seller = Seller(nm, em, passw)
            User.sellers.append(cur_seller)
            print(f'Welcome {cur_seller.name}')
          elif ch == 'L':
            em = input('ENTER EMAIL:')
            passw = input('ENTER PASSWORD:')
            f = False
            for s_user in User.sellers:
              if(s_user.email == em and s_user.password == passw):
                cur_seller = s_user
                print(f'Welcome {cur_seller.name}')
                f = True
                break
            
            if f == False:
              print('Seller Not Found!')
          
          else:
            print('Invalid Option')
        
        else:
           
           print('---------------OPTIONS--------------')
           print('1. ADD PRODUCT')
           print('2. UPDATE PRODUCT STATUS')
           print('3. SHOW PRODUCT')
           print('4. LOGOUT')

           op = int(input('ENTER OPTION:'))

           if op == 1:
               pnm = input('ENTER PRODUCT NAME:')
               price = int(input('ENTER PRODUCT PRICE:'))
               status = input('ENTER PRODUCT STATUS:')
               prod = Product(pnm, price, status)
               shop.add_Product(prod)

           elif op == 2:
                new_status = input('ENTER PRODUCT STATUS:')
                nm = input('ENTER PRODUCT NAME:')
                shop.update_stock(nm, new_status)
           elif op == 3:
                for product in shop.products:
                   print(f'Product name: {product.name}\tPrice: {product.price}\tStock Status: {product.stock}')
           elif op == 4:
              cur_seller = None
              break
           else:
              print('Invalid Option!!')
           
    elif op == 2:
          while True:
            if cur_user == None:
              print('NO CUSTOMER LOGIN!!')
              ch = input('LOGIN OR RESGISTER (L/R)?:')

              if ch == 'R':
                nm = input('ENTER NAME:')
                em = input('ENTER EMAIL:')
                passw = input('ENTER PASSWORD:')

                cur_user = Customer(nm, em, passw)
                User.customers.append(cur_user)
                print(f'Welcome {cur_user.name}')
              elif ch == 'L':
                em = input('ENTER EMAIL:')
                passw = input('ENTER PASSWORD:')
                f = False
                for user in User.customers:
                  if(user.email == em and user.password == passw):
                    cur_user = user
                    print(f'Welcome {cur_user.name}')
                    f = True
                    break
                
                if f == False:
                  print('Customer Not Found!')
              
              else:
                print('Invalid Option')
            
            else:
                print('---------------OPTIONS--------------')
                print('1. BUY PRODUCT')
                print('2. SHOW PORDUCT')
                print('3. LOGOUT')

                op = int(input('ENTER OPTION:'))

                if op == 1:
                    nm = input('ENTER PRODUCT NAME')
                    cur_user.buy_Product(cur_user, nm)
                elif op == 2:
                   shop.show_product()
                elif op == 3:
                   cur_user = None
                   break
    elif op == 3:
       break
    else:
       print('Invalid option')


if __name__ == '__main__' :
  main()