# guess the number game
import random 
random=random.randint(1,100)
i=True
count = 1
while(i):
    guess=int(input("Guess The Number : "))
    difference=abs(guess-random)
    if(guess == random):
        print(f"Congratulation ! You Guessed the number in {count} attempt !")
        i=False
    elif(difference <= 5 and difference >=1):
        print("So Close !!")
        count+=1
    elif(difference <= 10 and difference >=6):
        print("Too Close..")
        count+=1
    elif(difference <= 15 and difference >=11):
        print("Close ..")
        count+=1
    elif (difference <= 20 and difference>=16) :
        print("Not too far")
        count+=1
    elif(difference >=21):
        print("too long.. ")
        count+=1
    else:
        print("You Enter a number out of range!")