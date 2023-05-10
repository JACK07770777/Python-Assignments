# Write A Python Program to  check  Multiple keys exists in a dictionary ?
d1={'Name':'Kido','age':999999999,'ID':0777}

def CM(d1,keys):
    end=True
    for key in keys:
        if key not in d1.key():
            end=False
            break
    return end 
keys = ['Name', 'Age', 'ID'] 
print(CM(d1, keys))