# Write APython Program To  Find The Second  smallest number in list ?

x=[]
y=int(input("Enter The Number Of Element In List:--> "))
for i in range(1,y+1):
    element=int(input("Enter The Elenment :"))
    x.append(element)
x.sort()
print("ThE Sorted List Is:-->",x)
print("The Second Smallest Value Of This List Is:-->",x[1]) 

# x = [] 
# y = int(input("Enter the number of elements: "))
# for i in range(1, y+1): 
#     element = int(input("Enter the elements: ")) 
#     x.append(element) 
# x.sort() 

# print("The sorted list: ", x) 
# print("The second smallest value of this list: ",x[1])   