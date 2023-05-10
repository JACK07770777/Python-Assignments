# Write a python program to convert a list of tuple into dictionary ?

def tupdi(Tuple, Dictionary):
    for Name, RollNo in Tuple:
        Dictionary.setdefault(Name, []).append(RollNo)
    return Dictionary


lit = [("Akash", 101), ("Gaurav", 102), ("Anand", 103), ("Neelam", 107)]

Dictionary = {}
print('Dictionary is :', tupdi(lit, Dictionary))

