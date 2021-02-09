# V - print shop
# A print shop charges 0.12€ the ten first copy, 0.11€ the next 20 and 0.10€ from there.Write an algorithm which given a
# number of copies and calculates the price.

copies = int(input("How many copies do you want? "))

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
