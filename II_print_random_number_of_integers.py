# II - print random number of integers
# Write an algorithm which receives a random integer and prints from 0 to it.
from random import randint

n = randint(0, 100)
print(n)
for x in range(0, n+1):
    print(x)


# IV - even numbers
# Write an algorithm which prints all the even numbers from 0 to a given number.
n = int(input("nbr? "))
for x in range(0, n+1):
    if x % 2 == 0:
        print(x)
