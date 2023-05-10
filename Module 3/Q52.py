# Write A Python function To Check whether A Number Is Perfect Or Not ?
def Number_Cheker():
  N=int(input("Enter Any Number To Check:-->"))
  sum=0
  for i in range(1,N):
      sum +=i
  if sum==sum:
      print(N,"Is Perfect Number:--<")    
  else:
      print(N,"Is Not Perfect Number:--<")
print(Number_Cheker())      