import random

secret=random.randint(1, 10)

while True: 
    guess=int(input("Enter guess: "))
    
    if guess > secret:
        print("You guessed high")
    elif guess < secret:
        print("You guessed low")
    else:
        print("You guessed correct")
        break
