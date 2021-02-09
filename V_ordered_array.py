# Write an algorithm which receives an array of integers and checks if it's ordered ascendantly.
# Print true if the array is ordered, false if it’s not.
x = [1, 2, 3, 4, 5]
# y = sorted(x, reverse=True)
z = [5, 4, 3, 2, 1]

if x == sorted(x, reverse=False):
    print(True)
else:
    print(False)
