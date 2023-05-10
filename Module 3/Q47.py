# Write A Python Program To Find  Highest 3 Values In Dictionary 
d1={
 'a':500,
  'b':1000,
  'c':100000,
  'd':1000000,
  'e':10000000
 }
S_D=sorted(d1.items(),key=lambda x:x[1],reverse=True)
print("Three Higest Value's Are:-->",S_D)
