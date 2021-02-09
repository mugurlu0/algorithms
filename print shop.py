# V - print shop
# A print shop charges 0.12€ the ten first copy, 0.11€ the next 20 and 0.10€ from there.Write an algorithm which given a number of copies and calculates the price.

copies=int(input("how many copies do you want to do? "))
if copies == range(1,10):
    print("That makes "+ str(copies*0.12)+ "€")

if copies >10 and copies <20:
        print("That makes "+ str(copies*0.11)+ "€")

if copies >20:
    print("That makes "+ str(copies*0.10)+ "€") 



            copies == 30
            =copies-10
            xx=x*0.12
            y=copies-20
            yy=y*0.11
            rest=copies-x-y
            restr=rest*0.1
            z=xx+yy+restr