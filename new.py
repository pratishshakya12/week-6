# items=[1,2,3,5,'a','b',-4,-22,20]
# letters=[]
# odd=[]
# even=0
# for i in items:
#     if type(i)==str:
#         letters.append(i)
#     else:
#         if i>0:
#             if i%2==0:
#                even+=i
#             else:
#              odd.append(i)
# print(letters)
# print(odd)
# print(even)


# for i in range(1,11):
#     if i==4 or i==5:
#         continue
#     for j in range(1,11):

#         print(f'{i}*{j}={i*j}')
  

lst=[1,2,3,4]
result=[]
# #1,8,27,64
# lst.remove(2)
# lst.remove(3)
# lst.remove(4)
# lst.insert(1,8)
# lst.insert(2,27)
# lst.insert(3,64)
# print(lst)
for i in lst:
    lst.append(lst[0]**3)
    lst.pop(0)
print(lst)
# for i in range(0,4):
#     lst.pop(i)
#     lst.append((i+1)**3)
# print(lst)