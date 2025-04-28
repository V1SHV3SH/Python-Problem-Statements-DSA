# Exercise 1: Download a copy of the file
# www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as keys in
# a dictionary. It doesn’t matter what the values are. Then you can use the in
# operator as a fast way to check whether a string is in the dictionary.


fname=open("words.txt")

word_dict = {}

for lines in fname :
    lines = lines.rstrip()
    words = lines.split()
    # print(words)

    for word in words :
        print(word)
        word_dict[word] = 0

print(word_dict)
if 'Writing' in word_dict :
    print("hurray")
