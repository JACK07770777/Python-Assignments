# Write a python program to  copy the contents of a file  to another file

source_file = 'source.txt'
dest_file = 'dest.txt'

# 
with open(source_file, 'r') as src, open(dest_file, 'w') as dest:
    # 
    for line in src:
        dest.write(line)
        