import random

from requests import check_compatibility

options=['rock','paper','scissor']

user_score=0
computer_score=0

print("Let's Play Rock,Paper and Seccior !")
print("\n")

while True:
   choice=input("Pick Your choice from Rock, Paper ,Scissor and for Q for Quit\n")
   if choice.lower()=='q':
     break
   elif choice.lower() not in options:
    continue
   else:
    #rock-->0
    #paper-->1
    #seccsior-->2
    num=random.randint(0, 2)
    if choice=='rock' and options[num]=='scissor':
      print("You won!")
      
      user_score=user_score+1
      
      
    elif choice=='paper' and options[num]=='rock':
      print("You won!")
      user_score=user_score+1
      
      
    elif choice=='scissor' and options[num]=='paper':
       print("You won!")
       user_score=user_score+1
       
      
    elif(choice.lower()==options[num]):
       print("You won!")
      
    else:
      print("You lose!")
      
      computer_score+=1
      
print("You won "+str(user_score)+" times")
print("computer won "+str(computer_score)+" times")
print("Good Bye! Have a nice Day")


