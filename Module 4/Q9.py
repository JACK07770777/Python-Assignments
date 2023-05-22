# Write a python program to  count the frequency of words in file ?


from collections import Counter


with open('sample.txt', 'r') as file:

   
    contents = file.read()

   
    words = contents.split()


    word_count = Counter(words)

    
    for word, count in word_count.items():
        print(f"{word}: {count}")