# write a python progra to find longest word ?


sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("The longest word is:", longest_word)