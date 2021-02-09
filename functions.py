
# Exercises
# Instructions
# translate five previous exercises into modular functions

# detail each and every step

def perfectNumber(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    if sum == n:
        print(str(n)+" is a perfect number")
    else:
        print(str(n) + " is not a perfect one")


perfectNumber(7)


def printShop(copies):
    if copies < 10:
        price = copies*0.12
        print(price)
    elif copies > 10 and 20 > copies:
        moreten = copies-10
        moretenprice = ((10*0.12) + (moreten*0.11))
        print(moretenprice)
    elif copies > 20:
        more30 = copies-30
        moret30price = ((more30*0.10) + (10*0.12) + (20*0.11))
        print(moret30price)


printShop(5)


def dice(attempts):
    from random import randint

    theNumber = 0
    while attempts != 0:
        attempts -= 1
        dice = randint(1, 6)

        if dice == 3:
            theNumber += 1
        print("you have " + str(attempts) + " left")
        print("the dice shows " + str(dice))

    print("number three appears " + str(theNumber)+" time(s)")


dice(2)


def vat(price):
    finalPrice = price*1.21
    print(str(finalPrice)+" €")


vat(5)


def modConvert(n, x):
    print(n % x)


modConvert(11, 5)
