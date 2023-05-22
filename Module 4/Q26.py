# What Is Used To check Whether An Object o is an insttance of a class a ?

# In Python, the "isinstance()" function is used to check whether an object is an instance of a class. Here's an example:
# 

class Animal:
    def __init__(self, name):
        self.name = name

cat = Animal("Fluffy")
if isinstance(cat, Animal):
    print("cat is an instance of Animal")
else:
    print("cat is not an instance of Animal")

# Output:
# cat is an instance of Animal


