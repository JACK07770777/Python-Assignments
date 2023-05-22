# Write a python program to  write a list to a file 
my_list = ['apple', 'banana', 'cherry', 'date']

with open('my_file.txt', 'w') as file:
    file.writelines("%s\n" % element for element in my_list)