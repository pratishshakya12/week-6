loop=int(input('Enter the num of times to loop:'))
dictionary={'apple':'fruit',}
for i in range(loop):
    choice=int(input("Press: 1 to add, 2 to display, 3 to remove , 4 to exit"))
    if choice==4:
        break
    elif choice==2:
        print(dictionary)
    elif choice ==3:
        rem=(input("Which word would you like to remove"))
        if rem in dictionary:
            dictionary.popitem(rem)
            print(dictionary)
        else:
            print('Not in dictionary')
    elif choice==1:
        word=(input('Enter the word to add:'))
        if word in dictionary:
            print(f'{word} already exists')
        else:
            meaning=(input(f'Enter the meaning of {word}:'))
            dictionary[word]=meaning




 
