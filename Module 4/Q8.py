# Write a python program to count the number of lines in a text file ?


filename = "myfile.txt"
with open(filename, "r") as file:
    # Initialize a counter variable
    count = 0
    # Loop through each line in the file
    for line in file:
        # Increment the counter
        count += 1
# Print the total number of lines
print("The file has", count, "lines.")
