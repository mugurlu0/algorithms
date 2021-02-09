# V - perfect number
# Write an algorithm which verify if a given positive integer is a perfect number,
# meaning equal to the sum of his divisors (except himself).

Number = int(input(" Please Enter any Number: "))
Sum = 0  # starts here to gather dividers
# the first value being 1, up to Number(e.g. "6"), each "i" will be tested ->
for i in range(1, Number):
    # 6%1==0, 6%2==0, 6%3==0, 6%4==2, 6%5==1
    if(Number % i == 0):
        # sum(0)+1+2+3 (bcs the condition is met only in these cases)
        Sum = Sum + i
        # =>sum== 6
if (Sum == Number):
    print(str(Number) + " is a Perfect number")
    # => 6 is a perfect number
else:
    print(str(Number) + " not a Perfect number")
