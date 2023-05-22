# What Is File Function In Python ? What Is Keyword To Create And Write File

# The file function in Python is used to create, open, read, write, and close files. It is a built-in function that provides a way to interact with files on the file system. 

# The keyword to create and write a file in Python is "open". Here's an example of how to create and write to a file:

# ```
# Open a file in write mode
file = open("text", "w")

# Write to the file
file.write("Hello, world!")

# Close the file
file.close()