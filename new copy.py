items=[1,2,3,5,'a','b',-4,-22,20]
letters=[]
odd=[]
even=0
for i in items:
    if type(i)==str:
        letters.append(i)
    else:
        if i>0:
            if i%2==0:
               even+=i
            else:
             odd.append(i)
print(letters)
print(odd)
print(even)