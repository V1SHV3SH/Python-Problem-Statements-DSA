# Find all unique words in a file
# Shakespeare used over 20,000 words in his works. But how would you determine
# that? How would you produce the list of all the words that Shakespeare used?
# Would you download all his work, read it and track all unique words by hand?
# Let’s use Python to achieve that instead. List all unique words, sorted in alphabet-
# ical order, that are stored in a file romeo.txt containing a subset of Shakespeare’s
# work.
# To get started, download a copy of the file www.py4e.com/code3/romeo.txt. Cre-
# ate a list of unique words, which will contain the final result. Write a program to
# open the file romeo.txt and read it line by line. For each line, split the line into a
# list of words using the split function. For each word, check to see if the word is
# 106 CHAPTER 8. LISTS
# already in the list of unique words. If the word is not in the list of unique words,
# add it to the list. When the program completes, sort and print the list of unique
# words in alphabetical order.
# Enter file: romeo.txt
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
# 'and', 'breaks', 'east', 'envious', 'fair', 'grief',
# 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
# 'sun', 'the', 'through', 'what', 'window',
# 'with', 'yonder']

fhand = open('romeo.txt')
WrdCnt = list()
for line in fhand:
    words = line.split()
    for wrd in words:
        if wrd in WrdCnt :
            continue
        WrdCnt.append(wrd)
WrdCnt.sort()
print(WrdCnt)
