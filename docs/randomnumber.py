
from random import *
#Generates a random integer.
aRandomNumber = randint(1,20)
i=0
while i<3:
    guess=input("Guess a number between 1 and 20 (inclusive): ")
    if not guess. isnumeric(): # checks if a string is only digit 0 to 9
        print ("That's not a postive whole number, try again1")
    else:
        guess=int(guess) # converts a string to an integer
    i+=1
print(i)
