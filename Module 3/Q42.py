# Write A Python Program To  Map Two List Into A Dictionary 

key=['name','age','gender']
value=["Jack",9999999999,'male']

MD={key[i]:value[i] for i in range(len(key))}
print(MD)