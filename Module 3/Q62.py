# Write a python program to raed a random line from File ?
# import random
# with open("text") as f:
#     R_L
    
    
import random

with open("text.file") as f:
    lines = f.readlines()
    random_line = random.choice(lines)
    print(random_line.strip())