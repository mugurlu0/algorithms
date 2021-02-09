# IV_minimum_position
# Write an algorithm which receives an array of integers and prints the position of its minimum.
x = []
while len(x) != 3:
    y = input("number ")
    x.append(int(y))
print(x.index(min(x)))
