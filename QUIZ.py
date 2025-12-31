import random

quiz_questions ={
    '1': {
        'question': 'Which of the following charcter comments is Python',
        'options': {'a':'#','b':'//','c':'/*','d':'!'},
        'answer': 'a'
    },
    '2': {
        'question': 'Which of the following is used to create a empty set in Python?',
        'options': {'a':'()','b':'[]','c':'{ }','d':'set( )'},
        'answer': 'd'
    },
    '3': {
       'question': 'Which method is used to add an element to a list',
       'options': {'a':'add()','b':'addList()','c':'update()','d':'append()'},
       'answer': 'd'
    }
}
a=list(dictionary.key())
random.shuffle(a)
print(a)
score=0
for i,j in quiz_questions.items():
    print(i," ",j['question'])
    for k,l in j['options'].items():
        print(k,":",l)
    user_answer=input('Enter your answer:')
    if user_answer in j['answer']:
        score=score+1
    
print(f'Your score is:{score}')