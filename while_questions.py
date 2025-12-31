# num=int(input("Enter your number:"))
# i=0
# while num>0:
#     i=i+num
#     num=int(input("Enter your number:"))
# print(i)

# num=int(input("Enter your number:"))
# while num>1:
#     print(num)
#     num=num-1
# print('lower threshold reached')

# import random
# num = random.randint(1, 100)
# user_input=int(input('ENTER your guess'))
# while num!=user_input:
#     if user_input>num:
#         print("TOO high")
#     elif user_input<num:
#         print('TOO low')
#     user_input=int(input('ENTER your guess'))
# print("CONGRATSSSSS")
  

# num=int(input('Enter a num'))
# i=1
# while True:
#     print(f'{num}*{i}={num*i}')
#     i=i+1
#     if i==11:
#         break


# total=0
# counter=1
# while counter<51:
#     print(counter)
#     counter=counter+1
#     total=total+counter
# print(total)


player1_score=0
player2_score=0
while True:
    player1=input("choose rock,paper,scissor:")
    player2=input("choose rock,paper,scissor:")
    if player1==player2:
        print('Its a tie')
    elif player1=='rock':
        if player2=='scissor':
            print("PLAYER 1 WINS")
            player1_score+=1
        else:
            print('PLAYER 2 WINS')
            player2_score+=1
    elif player1=='paper':
        if player2=='rock':
            print("PLAYER 1 WINS")
            player1_score+=1
        else:
            print('PLAYER 2 WINS')
            player2_score+=1
    elif player1=='scissor':
        if player2=='paper':
            print("PLAYER 1 WINS")
            player1_score+=1
        else:
            print('PLAYER 2 WINS')
            player2_score+=1
    if player1_score==5:
        print('Player 1 won all')
    elif player2_score==5:
        print('Player 2 won all')