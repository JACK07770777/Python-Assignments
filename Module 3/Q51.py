# Write a python program to check whether a number is in a given range 
def I_N_R():
    # number,S_range,E_range
    number=int(input("Enter Any Number:-->"))
    S_range=int(input("Enter The Starting Range Of Number:-->"))
    E_range=int(input("Enter The Ending Range Of Number:-->"))
    if number>=S_range and number<=E_range:
        return True
    else:
        return False
print(I_N_R())