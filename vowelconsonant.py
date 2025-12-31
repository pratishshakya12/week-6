str=input('Enter a string:')
vowels=set()
for i in str:
    if i in 'aeiou':
        vowels.add(i)
print(vowels)
