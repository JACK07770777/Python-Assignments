# Write A Python  Program To Generate And  Print Lsit Of First And Last 5  Elements Where  The Values Are Square Of Numbers Between 1 And 30 ?
#17
l=[]
for i in range(1,31):
    l.append(i**2)
print(l[5:])
