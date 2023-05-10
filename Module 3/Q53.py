# Write a python function that checks whether a passed string is palindrome or not 
def Checker():
    x=str(input("Enter Any String To Check:-->"))
    x="".join(e for e in x.lower()if e.isalnum())
    return x==x[::-1]
print(Checker())    
    