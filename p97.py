import random

print("Number Guessing Game")

number= random.randint(1,9)

chances=0
print("Guess a number between (0 and 9)")
#ask the user for the input


while chances<5:
    guessNumber= int(input("enter your guess: "))
    if guessNumber==number:
        print("CONGRATS you have WON!!")
        break
    elif guessNumber<number:
        print("choose a higher number than",guessNumber)
    else :
        print("choose a lower number than ",guessNumber)


    chances +=1





if not chances<5:
    print("you have lost!! the correct number was ",number)    
     

        
