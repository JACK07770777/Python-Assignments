# Write A Python Script To  Concatenate Following Dictionaries To Create A new One ?

d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}

d4={}

for i in(d1,d2,d3):
    d4.update(i)
print(d4)    
