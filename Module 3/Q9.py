# Wrirte a python program to check the list is empty or not ?

# creating an empty list
# lst = []

# # number of elements as input
# n = int(input("Enter number of elements : "))

# # iterating till the range
# for i in range(0, n):
# 	ele = int(input())
# 	# adding the element
# 	lst.append(ele)

# print(lst)


a=[]
x=int(input("Enter number Of Element"))
for i in range(0,x):
     y=int(input())
     a.append(y)
print(a)
z=len(a)
print("The List Length Is ",z)
if z==0:
    print("The Length Of List Is Empty")
else:
    print("The List Of Length Is:-->",z)

