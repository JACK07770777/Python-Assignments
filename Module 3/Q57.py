# How Can You Pickup A Random Item  From Tuple or List ?

import random

# FOR LIST:--->
l1=["Jack",777,"Queen","Phantom","Cow","Hen","Dog"]
t1=("A",5,"p",8,"abcd")

# for list=====

L=random.choice(l1)
print("The Random List Is:-->",L)

# for tuple=====
T=random.choice(t1)
print("The Random Tuple Is:-->",T)

