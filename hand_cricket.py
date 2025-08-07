import random

def batting ():
   try:
      print('So you are going to bat and i am going to bowl')
      score=0
      balls=[random.randint(1,6) for i in range(6)]
      for i in balls:
          user=int(input('enter your number'))
          if user<1 or user>6 :
                print('enter the number within six bro')
                break
          else:
             print('my no is ',i)   
             if i==user:
                    print('Result - you are done bro')
                    print('your score is ',score)
                    break  
             else:
                    score=score+user
      else:
            print('Result- you completed batting and your sore is',score)
      
      print('Now ready to Bowl bro . I am going to bat')
      score2=0
      batt_balls=[random.randint(1,6) for i in range(6)]
      for i in batt_balls:
           user2=int(input('enter your no '))
           if user2<1 or user2>6 :
                print('Bro use the numbers within six')
                break
           else:
             print('my no is ',i)   
             if i==user2:
                    print('Result - I am done bro')
                    print('My score is ',score2)
                    break  
             else:
                    score2=score2+i
      else:
            print('Result- I completed batting and My sore is',score2)
       
      if score > score2 :
           print('FINAL RESULT \n YOU WON BRO !','\n YOUR SCORE',score,'\n MY SCORE',score2)
      else :
           print('FINAL RESULT  \n I WON BRO !','\n YOUR SCORE',score,'\n MY SCORE',score2)
           

   except ValueError :
        print('only numbers are allowed bro and it also allowed only within six')

def bowling():
     try:
         print('so i am going to bat . You are going to bowl')
         score=0
         batt_balls=[random.randint(1,6) for i in range(6)]
         for i in batt_balls:
            user=int(input('enter your no '))
            if user<1 or user>6 :
                print('Bro use the numbers within six')
                break
            else:
               print('my no is ',i)   
               if i==user:
                    print('Result - I am done bro')
                    print('My score is ',score)
                    break  
               else:
                    score=score+i
         else:
            print('Result- I completed batting and My sore is',score)

         print('Now ready to bat i am going to bowl')
         score2=0
         balls=[random.randint(1,6) for i in range(6)]
         for i in balls:
             user2=int(input('enter your number'))
             if user2<1 or user2>6 :
                   print('enter the number within six bro')
                   break
             else:
                print('my no is ',i)   
                if i==user2:
                       print('Result - you are done bro')
                       print('your score is ',score2)
                       break  
                else:
                       score2=score2+user2
         else:
           print('Result- you completed batting and your sore is',score2)

         if score > score2 :
           print('FINAL RESULT \n I WON BRO !','\n YOUR SCORE',score2,'\n MY SCORE',score)
         else :
           print('FINAL RESULT  \n YOU WON BRO !','\n YOUR SCORE',score2,'\n MY SCORE',score)
     except ValueError :
        print('only numbers are allowed bro and it also allowed only within six')

try :
   choice=int(input('enter your choice \n 1. 0 -> head \n 2. 1 -> tail')) 
   if choice in [0,1] :
        com_choice= 1 if choice==0 else 0
        toss_result=random.randint(0,1)
        if choice==toss_result:
             print('you won the toss bro !')
             bat_or_bowl=int(input('enter your choice \n 1. 0 -> batting \n 2. 1-> bowling')) 
             if bat_or_bowl == 0:
                  print('So bro you decided to bat')
                  batting();
             elif bat_or_bowl== 1:
                  print('So you decided to bowl')
                  bowling();
        else:
             print('ha ! ha ! ha ! i won bro')
             bot_choice=random.randint(0,1)
             if bot_choice==0:
                  print('i choose to bat bro')
                  bowling();
             elif bot_choice==1:
                  print('i choose to bowl')
                  batting();

        
   else:
        print('enter valid choice bro ie) "0" or "1"')

except ValueError:
     print('enter the given options bro ie) "0" or "1"')




     


    