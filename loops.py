# I - print numbers
# Write an algorithm which receives an integer n and prints:

# 1 the numbers from 1 to n

n = int(input("Type a number "))
for x in range(1, n+1):
    print(x)


# 2 the numbers from 1 to n in descending order
n = int(input("Type a number "))
for x in range(n, 0, -1):
    print(x)
# 3 the numbers from -n to n
n = int(input("Type a number "))
for x in range(-n, n+1, 1):
    print(x)

# 4 the odd numbers from 1 to n
n = int(input("Type a number "))
for x in range(1, n+1, 2):
    print(x)

# 4bis with modulo:
n = int(input("Type a number "))
for x in range(1, n+1):
    if x % 2 == 1:
        print(x)
