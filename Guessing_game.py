import random 
cp = random.randint(1,11)
cp = int(cp)
for num in range(50):
    user = input("Guess a number berween 1 and 10: ")
    user = int(user)
    if user != cp :
        if user < 5:
            print("Too low, try again!")
        else:
            print("Too high, try again!")
    elif user == cp :
        print("You guessed it! You won!")
        user=input("Do you want to keep playing (y/n): ")
        if user == 'y':
            user=str(user)
            break

