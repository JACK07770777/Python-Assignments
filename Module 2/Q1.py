# Write a python program to check if number is possitive negative or zero.

n=int(input("Enter Any Number:-->"))

if n<=0:
    if n==0:
        print(n,'=Zero')
    else:
        print(n,'=Negative')
else:
    print(n,'=Posotive')