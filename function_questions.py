
# items=['sql', '123', 'python']
# f=list(filter(lambda x:x.isalpha(),items))
# print(f)

# products = [
#  {'id': 1, 'name': 'laptop', 'category': 'electronics', 'price': 1200, 'instock': True},
#  {'id': 2, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock':False}
# ]
# f=list(filter(lambda x:x['instock'],products))
# print(f)

# num1=int(input('a num'))
# num2=int(input('a num'))
# def calculate_sum(start,end):
#     total=0
#     for i in range(start,end+1):
#         total=total+i
#     print(total)

# calculate_sum(num1,num2)


# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def div(a,b):
#     if b==0:
#         print('Zero error')
#     print(a/b)

# def main_calculator():
#     while True:
#         num1=int(input('Enter first num : '))
#         num2=int(input('Enter first num : '))
#         action=input('Enter action (Add, Subtract, Multiply, Divide, Exit) :').capitalize()
#         if action=='Add':
#             add(num1,num2)
#         elif action=='Sub':
#             sub(num1,num2)
#         elif action=='Mul':
#             mul(num1,num2)
#         elif action=='Div':
#             div(num1,num2)
#         elif action=='Exit':
#             break

# main_calculator()


# course = [ {'title': 'Ancient Civilizations', 'genre': 'history'},
#            {'title': 'Corporate Finance', 'genre': 'commerce'},
#            {'title': 'Modern World History', 'genre': 'history'} ]

# f=list(filter(lambda x:x['genre']=='history',course))
# print(f)

# emails = ['ram.sharma@gmail.com', 'spam@hooya.com', 'virus@malware.net', 'shyam.kumar@workcorp.com']
# blacklist = ('@hooya.com', '@malware.net')

# f=list(filter(lambda x:x.endswith(blacklist),emails))
# print(f)


# price = [100, 50, 200, 75]
# f=list(map(lambda x:x*0.8,price))
# print(f)


# def skip_two(items):
#     result=[]
#     for i in range(1,len(items)+1):
#         result.append(items[i])
#         return result
# list=['a','b','c','d','e','f','g','h','i','j','k','l']
# skip_two(list)


# items=['a','b','c','d','e','f','g','h','i','j','k','l']
# def remove_at_idx(lst,a):
#     new=[]
#     lst.pop(a)
#     new=lst
#     return new
# print(remove_at_idx(items,3))


# def clean(user_input):
#     step1=user_input.maketrans('@%#!','####')
#     step2=user_input.translate(step1)
#     print(step2)
# clean('abcd@#!%')


# users_db={}
# def register_user(username,password,email):
#     if username in users_db:
#         return 'username alr exists'
#     else:
#         users_db[username]=[password,email]
#         return "Registration successful for ",username

# def login_user(username,password):
#     if username in users_db.keys():
#         if password==users_db[username][0]:
#             print(f'Welcome back {username}')
#         else:
#             print('Incorrect password')

#     else:
#         print('User not found')
# while True:       
#     action=input('Enter your action (Register, login): ').lower()
#     if action=='register':
#         user_username=input('Enter a username:')
#         user_password=input('Enter a password')
#         user_email=input('Enter your email')
#         register_user(user_username,user_password,user_email)
#     elif action=='login':
#         user_username=input('Enter your username:')
#         user_password=input('Enter your password')
#         login_user(user_username,user_password)
#     else:
#         break



# inventory=[{'name':'Laptop','price':50000,'quantity':5}]
# def add_product():
#     name=input("Enter a product")
#     for i in inventory:
#         if i['name'].lower()==name.lower():
#             print("Product already exists.")
#             return
#     price=int(input("Enter price: "))
#     quantity=int(input("Enter quantity: "))

#     if price <= 0 or quantity <= 0:
#         print("Price and quantity must be positive.")
#         return
#     inventory.append({'name': name, 'price': price, 'quantity': quantity})
#     print("Product added successfully.")


# def view_products():
#     print("\nName    Price  Quantity")
#     print("-" * 30)
#     for i in inventory:
#         print(f"{i['name']}  {i['price']}  {i['quantity']}")


# def update_product():
#     name=input("Enter product name to update: ")

#     for i in inventory:
#         if i['name'].lower()==name.lower():
#             price=float(input("Enter new price: "))
#             quantity=int(input("Enter new quantity: "))

#             if price <= 0 or quantity <= 0:
#                 print("Price and quantity must be positive.")
#                 return

#             i['price']=price
#             i['quantity']=quantity
#             print("Product updated successfully.")
#             return

#     print("Product not found.")


# def delete_product():
#     name=input("Enter product name to delete: ")

#     for i in inventory:
#         if i['name'].lower()==name.lower():
#             inventory.remove(i)
#             print("Product deleted successfully.")
#             return

#     print("Product not found.")


# def total_inventory_value():
#     total=0
#     for i in inventory:
#         total += i['price'] * i['quantity']

#     print("Total inventory value:", total)

# while True:
#     choice=int(input('1. Add new product \n 2. View all products in a formatted table \n 3. Update product details \n 4. Delete a product\n 5. Calculate total inventory value \n 6. Exit \n Enter action : '))
#     if choice=='1':
#         add_product()
#     elif choice=='2':
#         view_products()
#     elif choice=='3':
#         update_product()
#     elif choice=='4':
#         delete_product()
#     elif choice=='5':
#         total_inventory_value()
#     elif choice=='6':
#         break
    

