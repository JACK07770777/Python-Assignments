# Write A Python Program To Sum Of Three Given Integers.However,If  Two  Values Are Equal sum Will Be Zero?

# def threeone(x,y,z):
#     if x==y or y==z or z==x:
#         sum=0
#     else:
#         sum=x=y=z
#     return sum    
    
# x=int(input("Enter First Number"))
# y=int(input("Enter First Number"))
# z=int(input("Enter First Number"))





#Function to get sum of all value, if 2 values are equal, return 0.
def sum(x, y, z):
        if x == y or y == z or z == x:
                sum = 0
        else:
                sum = x + y + z
        return sum

#Calculate average number for all 3 sum value.
def avg(total, totalnum):
  avg = float(total)/float(totalnum)
  return avg

#Getting user input. Create 3 different variable.
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))


totalnum = 3
total = sum(x,y,z)
average = avg(total,totalnum)
print ("Your total sum value is :", total)
print ("Your average number of 3 sum value is :", average)

# any two values are same so sum === 0