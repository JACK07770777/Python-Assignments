# Write A python program to read an entire text file
filename = input("Enter the name of the file: ")

with open(filename, "r") as file:
    contents = file.read()
    print(contents)