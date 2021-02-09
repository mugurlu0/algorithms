from random import randint
# I - cinema tariffs
# In a cinema the full tariff is 10€, the reduced one is 8€.Write an algorithm which given a boolean indicating
# if the person can have a reduced tariff prints the price to pay.
tarif=10
dumpedTarif=8
age= int(input("what's your age? "))

if age < 18:
    print("You've got a dumping and will pay: " + str(dumpedTarif)+"€")
else:
    print("your tarif is " + str(tarif)+"€")

# II - maximum
# Write an algorithm which given 3 numbers finds the maximum.

x = int(input("first number : "))
y = int(input("second number : "))
z = int(input("third number : "))

if x > y and x > z:
    print("the bigger one is " + str(x))
elif y > x and y > z:
    print("the bigger one is " + str(y))
elif z > x and z > y:
    print("the bigger one is " + str(z))

