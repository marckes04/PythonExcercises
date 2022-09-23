

#from random import randint

##randint(a,b) -> a<=N<=b

#randVal = randint(0,100)

#while(True):#while(True=True)
 #   guess = int(input("Please enter your guess: "))
  #  if guess == randVal:
   #     break
    #elif guess < randVal:
     #   print("Your guess was too low")
    #else:
     #   print("Too High")

#print("You guessed correctly with: ",guess)

from random import random
from time import perf_counter

randVal = random() # 0.0<=N<1.0
#print(randVal)
#time.perf_counter() - > timeValue
#time.perf_counter() - > timeValue2

upper = 1.0
lower = 0.0
#guess = 0.5 - >Too Low-> lower = 0.5
#guess = 0.9 -> Too High ->uper = 0.9
#guess = 0.5

startTime = perf_counter()
while(True):#while(True=True)
     guess = (upper + lower)/2#0.5+0.75- >1.4/2 -> 0.7
     if guess == randVal:
        break
     elif guess<randVal:
        lower = guess # lower = 0.5; upper = 1.0
     else:
        upper = guess # upper = 0.75
   
endTime = perf_counter()
print(guess)
print("It took us:",endTime-startTime,"seconds")






