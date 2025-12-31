# while True:
#     age_input=input("Enter your age (or type 'stop' to exit): ")
#     if age_input.lower() == "stop":
#         break
#     age=int(age_input)
#     if age < 18:
#         print("You are a minor.")
#     elif age <= 60:
#         print("You are an adult.")
#     else:
#         print("You are a senior citizen.")

# while True:
#     vehicle=input("Enter the vehicle name: ")
#     if vehicle.lower()++"bus":
#         print("finally the wait is over")
#         break
#     else:
#         print("waiting")

# while True:
#     fruit=input("Enter a fruit name: ")
#     if fruit=="apple":
#         print("You got it")
#         break
#     else:
#         print("Try again")

# import random
# secret=random.randint(1, 10)
# attempts=0
# while True:
#     guess=int(input("Guess a number between 1 and 10: "))
#     attempts+=1
#     if guess==secret:
#         print(f"attempts={attempts}")
#         break
#     elif guess < secret:
#         print("Guess higher!")
#     else:
#         print("Guess lower!")

# ratings=['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '17+']
# content_ratings={}
# i=0
# while i<len(ratings):
#     rating=ratings[i]
#     if rating in content_ratings:
#         content_ratings[rating]+=1
#     else:
#         content_ratings[rating]=1
#     i=i+1
# print(content_ratings)

# attempts=0
# while attempts<3:
#     username=input("Enter username: ")
#     password=input("Enter password: ")
#     if username=="admin" and password=="1234":
#         print("Logged in")
#         break
#     else:
#         print("try again.")
#         attempts+=1
# print("Too many failed attempts.")

# import random

# while True:
#     num1=random.randint(1, 30)
#     num2=random.randint(1, 30)
#     answer=input(f"What is {num1}*{num2}: ")
#     if answer=="exit":
#         break
#     if int(answer)==num1*num2:
#         print("correct!")
#     else:
#         print("incorrect, try again.")

# while True:
#     num=input("Enter a number: ")
#     if num.lower()=="exit":
#         break
#     num=int(num)
    
#     if num < 2:
#         print("The number is not prime.")
#     else:
#         prime=True
#         i=2
#         while i*i<=num:
#             if num%i==0:
#                 prime=False
#                 break
#             i+=1
        
#         if prime:
#             print("The number is prime.")
#         else:
#             print("The number is not prime.")

# word='python'
# user_input=input('Enter your guess: ')
# while True:
#     if user_input=='quit':
#         break
#     if word!=user_input:
#         print('Incorrect! Try Again')
#         user_input=input('Enter your guess: ')
#     elif word==user_input:
#         print('CORRECT! YOU WIN')
#         break

# floor=1
# while True:
#     desired_floor_troubleshoot=input('Enter your destination floor:')
#     if desired_floor_troubleshoot.isdigit():
#         desired_floor=int(desired_floor_troubleshoot)
#         if desired_floor>floor:
#             print('Going up')
#         elif desired_floor<floor:
#             print('Going DOWN')
#         elif desired_floor==floor:
#             print(f'You are already on floor {floor}')
#         floor=desired_floor
#     else:
#         print('Invalid Floor no')

count=0
while True:
    name=input('Enter a name:')
    if name=='good luck':
        count=count+1
    if count==3:
        print('you have entered good luck 3 times')
        break