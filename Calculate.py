import math
# I - calculate
# Write an algorithm which calculates:

# the sum of two chosen number

def summing(a,b):
   return(a+b)

print (summing(2,3))

# the division of two chosen number
def dividing(a,b):
   return(a/b)

print (dividing(6,3))
# the modulo of two inputed numbers
def modulo(a,b):
   return(a%b)
a= int(input("enter the first number "))
b= int(input("enter the second number "))
print (modulo(a,b))

#II - concatenate sentence
# Write an algorithm which concatenates two phrases together.
x = "lorem ipsum"
y = "tu quoque me fili"
print(x+" "+y)

# III - VAT
# Write an algorithm which receives a price without VAT
# and returns the price with VAT with a rate of 21%.
x = int(input("what is the price without vat? "))
print("this is the full price : " + str(x*1.21))
# IV - surface of a circle
# Write an algorithm which receives the radius of a circle and calculate its surface.
r= input("what's the radius? ")
pi=math.pi
surface = (pi)*(int(r)**2)
print(surface)
