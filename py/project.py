import random

terget= random.randint(1,100)

while True:
    userChoice= int(input("Guess The Number : "))
    if(userChoice == terget):
        print("Success : Currect Guess")
        break
    elif(userChoice<terget):
        print("Incurrect : your number is too short")
    else:
        print("your number is too big. Take a smaller number")

print("-----------Game Over------------");




