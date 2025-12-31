# items=[1,2,3,4,5]
# for i in items:
#     if i%2==0:
#         print(f'Number {i} is EVEN')
#     else:
#         print(f'Number {i} is odd')\


# list = [10,20,30,40]
# a=0
# for i in list:
#     a+=i
#     print(f'Added {i}. The running total is {a}')
# print(f'The total is {a}')


# student_names = ["Ram", "Hari", "Sita"]
# print(' --- Email Greetings Generated ---')
# for i in student_names:
#     print(f'Hi {i}, your course approval is ready!')


# pages=[45, 30, 50, 40]
# count=0
# print('--- Book Chapter Summary ---')
# for i in pages:
#     count=count+1
#     print(f'Chapter {count} has {i} pages.')


# list=[4,5,3,2]
# product=1
# for i in list:
#     product=product*i
# print(product)


# num=11
# for i in range(1,11):
#     print(f'11 * {i} = {11*i}')


# students = [

#     {"name": "ram", "math_grade": 43},

#     {"name": "hari", "math_grade": 65},

#     {"name": "sita", "math_grade": 90}

# ] 
# for i in students:
#     if i["math_grade"]>=70:
#         print('Approved')
#     else:
#         print('Rejected')


# a=[1,2,3,4,5]
# b=[3,4,5,6,7] 
# common=[]
# for i in a:
#     if i in b:
#         common.append(i)
# print('Status:',common)


# lst=[1,2,3,4]
# print(lst[0],lst[3])

# lst=[1,2,3,4]
# print(lst[0],lst[3],lst[1])


# lst=[1,2,3,4]
# lst.remove(3)
# lst.insert(1,"a")
# print(lst)


# items=[1,2,3,4,5]
# odd=[]
# even=[]
# for i in items:
#     if i>0:
#         if i%2==0:
#            even.append(i)
#         else:
#             odd.append(i)
# print(odd)
# print(even)


# num = int(input("Enter a number: "))
# count = 0
# for i in range(1, num+1):
#     if num%i == 0:
#         count += 1
# if count > 2:
#     print (f"Number {num} is not a prime number")
# else:
#     print (f"Number {num} is a prime number")


# items=[1,2,3,5,'a','b',-4,-22,20]
# letters=[]
# odd=[]
# even=[]
# nega=[]
# for i in items:
#     if type(i)==str:
#         letters.append(i)
#     else:
#         if i>0:
#             if i%2==0:
#                even.append(i)
#             else:
#              odd.append(i)
#         else:
#            nega.append(i)
# print(letters)
# print(odd)
# print(even)
# print(nega)


# text = input("Enter a string: ")
# digits = 0
# letters = 0
# for i in text:
#     if i.isdigit():
#         digits += 1
#     elif i.isalpha():
#         letters += 1
# print(digits)
# print(letters)


# password="password"
# entered_password=input("Enter your password")
# for i in range(3):
#     if entered_password==password:
#         print("Logged in successfully")
#         break
#     else:
#         entered_password=input(f"Try again({i+1}):")


# num=input('Enter a num:')
# if num%2==0:
#     print('Even')
# else:
#     print('odd')


# num=int(input('Enter a number:'))
# factorial=1
# for i in range(1,num+1):
#     factorial*=i
# print(f'The factorial of {num} is {factorial}')



# for i in range(1,9):
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")


# lst=[1,2,3,4] 
# print(lst[0],lst[1])


# upper=int(input("Enter the upper value"))
# lower=int(input("Enter the lower value"))
# sum=0
# for i in range(lower,upper+1):
#     if not i%2==0:
#         sum+=i
# print('Sum = ',sum)


# upper=int(input("Enter the upper value"))
# lower=int(input("Enter the lower value"))
# sum=0
# for i in range(lower,upper+1):
#     if not i%2==0:
#         sum+=i
# print('Sum = ',sum)


# string=input('enter a string:')
# num=string.count(' ')
# print(num)


# list=[1,2,3,4]
# for i in list:
#     a=i**3
#     list.pop(i-1)
#     list.insert(i-1,a)
# print(list)
# list=[1,2,3,4]
# for i in list:
#     list[i-1]=i**3
# print(list)


# name='programming'
# rev=''
# for i in name[::-1]:
#     rev=rev+i
# print(rev)


# for i in range(50):
#     if i==8:
#         break
#     else:
#         print(i)


# word='programming'
# for i in word:
#     print(i)
    

# a=["ram","shyam",1,2]
# for i in a:
#     if type(i)==str:
#         print(f'Hello! {i}')


# a=["ram","shyam"]
# for i in a:
#     a.append('Dr '+a[0])
#     a.pop(0)
# print(a)


# list=[1,2,3,4,5]
# square=[]
# for i in list:
#     square.append(i**2)
# print(square)


# lst1=[111,32,-9,-45,-17,9,85,-10]
# positive=[]
# for i in lst1:
#     if i>0:
#         positive.append(i)
# print(positive)


# list=[0,1,2,3,4,5,6]
# for i in list:
#     if i==3 or i==6:
#         list.remove(i)
# print(list)


# list1=[1,'a',2,'b','c','d',5]
# list2=[]
# for i in list1:
#     list2.append(type(i))
# print(list2)


# for i in range(5):
#     print(i)
# else:
#     print('done')


# num=105
# for i in range(100):
#     print(num)
#     num-=7
#     if num==0:
#         break


# bad_chars = [';', ':', '!', '*',' ']
# string = "py;th* o:n ! ;py * t*h:o !n"
# for i in bad_chars:
#     string=string.replace(i,'')
# print(string)


# num=[2,3,6,3,7,1937,74910]
# even=[]
# odd=[]
# for i in num:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(odd)
# print(even)


# sum=0
# for i in range(3,100):
#     if i%3==0 or i%5==0:
#         sum=sum+i
# print(sum)


# sum_even=0
# sum_odd=0
# for i in range(101):
#     if i%2==0:
#          sum_even+=i
#     else:
#          sum_odd+=i
# print(sum_even)
# print(sum_odd)


