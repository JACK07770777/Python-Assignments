# Write A Python Function To calculate  the factorial of a number(a non negative integer)

def F_number(n):
    if n==0:
        return 1
    else:
        return n*F_number(n-1)
# n=int(input("Enter Any Number"))  
print(F_number(5))  
    
    