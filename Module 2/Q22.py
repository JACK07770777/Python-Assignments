# Write a Python program to get a string made of the first 2
# and the last 2 chars from a given string.
# If the string length is less than 2, return 'empty string'.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
# """

my_string = input("enter a string ")


if len(my_string) > 1:
    print(my_string[:2]+my_string[-2:])
else:
    print('empty string')
