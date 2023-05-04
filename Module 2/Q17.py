# write A python program to get a single string from two given string, seprated by a space and swap the first two characters of each string?
a=input("Enter Any String")
b=input("Enter Any String")

x=a[0:2]
y=b[0:2]

# print(x)
x1=a.replace(x,y)
y1=b.replace(y,x)


print(x1)
print(y1)