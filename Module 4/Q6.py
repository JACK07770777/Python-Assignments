# Write A  python Program To  Raed A file  line by Line  And Store It in Variable ?
with open('filename.txt', 'r') as file:
    lines = file.readlines()

# print the lines variable to see the contents of the file
print(lines)