# write A python Function To insert A string In  The Middle Of A string ?

x=input("Enter Any String:-->")
y=input("Enter A Sub string:-->")

center=len(x)//2
a=x[:center]
b=x[center:]
Final=f'{a}{y}{b}'
print(Final)
