# Write a python program to replace  last Value of tuple in list ?

# x=("p","y","t","h","o","n")
# print("The Tuple Is :->",x)
# for i in x:
#     print(i)
# index=x.index("n")
# print(index)
# # Change 
# t1=[1,2,3,4,5]
# print([t[:-1]+(6,)for t in t1])


t1 = [(10,20,30,40,50)]
print([t[:-1] + (100,) for t in t1])