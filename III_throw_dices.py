# III - throw dices
# Write an algorithm which throws a dice a given number of time and count the number of time a certain number is received.
from random import randint

attempts = int(input("number of counts? "))
theNumber = 0
while attempts != 0:
    attempts -= 1
    dice = randint(1, 6)

    if dice == 3:
        theNumber += 1
    print("you have " + str(attempts) + " left")
    print("the dice shows " + str(dice))

print("number three appears " + str(theNumber)+" time(s)")
