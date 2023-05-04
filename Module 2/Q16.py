# Write a python program to count the occurences of each world in a given sentence




x=input("Enter Any String:----->")
y=x.split()
for i in y:
    if i.isalpha():
        print("******")
        b=y.count(i)
        print("******")
        print(i,":",b)
        print("******")