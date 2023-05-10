# Write a python function that takes a list and  returns a new list with unique elements of the first?
 
 
 
# a=[]
# x=int(input("Enter number Of Element"))
# for i in range(0,x):
#      y=int(input())
#      a.append(y)
# print(a)
# New Least Creation 
# a=[1,2,3,4,5,6]
# a.choices()
# print(a)

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([8,3,4,7,7,6,9,5,8,3])) 

