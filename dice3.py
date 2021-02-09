from random import randint
# III - identical dice
# Write an algorithm which throws 3 dices and finds out the number of identical value, three, two or none.
dice1= randint(1,6)
dice2= randint(1,6)
dice3= randint(1,6)
print(dice1)
print(dice2)
print(dice3)
if dice1==dice2 and dice2==dice3:
    print("3 times the same number")
elif dice1==dice2 or dice1==dice3:
    print("twice the same number")
elif dice2==dice1 or dice2==dice3:
    print("twice the same number")
elif dice3==dice1 or dice2==dice3:
    print("twice the same number")
elif dice1!=dice2 and dice1!=dice3:
    print("none of the dices are the same number")
