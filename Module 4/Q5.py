# Write A Python Program to  reada file line by line and store into a list ?
file = open('filename.txt', 'r')


lines = []

# Loop through each line in the file
for line in file:
    # Add the line to the list
    lines.append(line.strip())

# Close the file
file.close()

# Print the list of lines
print(lines)