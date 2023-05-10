# Write a python program to create  a dictionar from a string.sample string
# w3resource
# expected output {"3":1,"s":1,"r":2,"e":2,"o":1,"u":1,"c":1}

string=str(input("Enter Any String :-->"))
F_D={}
for char in string:
    F_D[char]=1
print(F_D)    
