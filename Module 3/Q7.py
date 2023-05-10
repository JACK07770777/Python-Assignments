# Write a pyhton program to count the number of string where the string length is 2 or morw and the first and last character are same from given list of string ?




x=input("Enter Any String:-->")
y=x.split()
a1=[]
for i in y:
    if len(i)>1 and i[0]==i[-1]:
        a1+=[i]
print("All Characters:",len(a1))
print(a1)        
        
    