# Write A Python Program To Append Text To File And Disply The Text ?

filename = "example.txt"
text = "This is a sample text."

# append text to file
with open(filename, "a") as file:
    file.write(text)

# read the file and display the text
with open(filename, "r") as file:
    text = file.read()
    print(text)