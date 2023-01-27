
# create a guessing game
# generate random integer

import random

jackpot = random.randint(1 , 100)

guess = int(input("guess a number"))
counter = 1 

while guess != jackpot :

 if guess < jackpot : 
     print("Wrong ! Guess Higher")
 else:
     print("Galat ! Guess lower")

 guess = int(input("Guess the Number"))
 counter = counter + 1

else : 
    print("correct guess")
    print("attempts" , counter)
