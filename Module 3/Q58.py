# How Will You Pickup Random Item From A Range ?

import random

x=int(input("Enter The Start Of The Range:-->"))
y=int(input("Enter The End Of Range:-->"))

M_range=range(x,y+1)
print("Your Range Is:-->",M_range)
R1=random.choice(M_range)

print("The Random Item From Given Range Is",R1)
