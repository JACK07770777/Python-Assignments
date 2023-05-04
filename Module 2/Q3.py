# Write A python program To Get Fibonacci Series Of Given Range.

# A program which takes any Range as input and Prints Fibonacci Series Upto that range.

r = int(input("Enter any Range = "))
x, y = 0, 1

print("------------------------------------------------------------------")
print("Fibonacci Series upto Range {0} : {1},{2}".format(r, x, y), end = ',')

for i in range (3, r+1):
    Sum = x + y
    if (i == r):
        print(Sum, end = ' ')
    else:
        print(Sum, end = ',')
    x = y
    y = Sum
print()
print("------------------------------------------------------------------")