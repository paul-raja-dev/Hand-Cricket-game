import random

choice=int(input('enter your choice \n 1. 0 -> head \n 2. 1 -> tail'))
com_choice= 1 if choice==0 else 0
toss_result=random.randint(1,2)
if choice==toss_result:
     print('you won bro !')
     bat_or_bowl=int(input('enter your choice \n 1. 0 -> batting \n 2. 1-> bowling'))
else:
     print('ha ! ha ! ha ! i won bro')
     bot_choice=random.randint(1,2)

if choice==toss_result:
     print('so bro you won the toss and decided to ', 'bat' if bat_or_bowl==0 else 'bowl' )

else :
     print('so bro basically i won the toss and decided to','bat' if bot_choice==0 else 'bowl')