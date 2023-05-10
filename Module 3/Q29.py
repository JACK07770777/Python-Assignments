# Write a python program to remove an empty tuples froma list ?

x=[(1,2,3),(1,2,9),()]
for i in x:
    if i==():
        x.remove(i)   
print(x)        
