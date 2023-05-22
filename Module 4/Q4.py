# Write A Python program to read first n line of a file ?
n = int(input("\n\t\tEnter Lines To Read : "))
f = open("file.txt","r")
for i in range(n):
	print(f.readline())