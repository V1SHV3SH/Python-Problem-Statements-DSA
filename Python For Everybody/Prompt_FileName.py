# Exercise 2: Write a program to prompt for a file name,
# and then read through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
# the line to extract the floating-point number on the line. Count these lines and
# then compute the total of the spam confidence values from these lines. When you
# reach the end of the file, print out the average spam confidence.
# You can download the file from www.py4e.com/code3/mbox-short.txt

file = input("Enter File Name: ")

if file == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")

try:
    fhand = open(file)
except:
    print("no such file found")
    print(f'no such file name {file} found')
    quit()

count, sum = 0,0

for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:') :
        # print(line)
        index = line.find(':')
        num = line[index+1:]
        num = num.strip()
        num = float(num)
        count = count+1
        sum = sum+num

avg=sum/count
print(" Total Spam Confidence value is ",avg)


# Exercise 3:
# Sometimes when programmers get bored or want to have a bit of fun, they add a
# harmless Easter Egg to their program. Modify the program that prompts the user
# for the file name so that it prints a funny message when the user types in the exact
# file name “na na boo boo”. The program should behave normally for all other files
# which exist and don’t exist. Here is a sample execution of the program:
# python egg.py
# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt
# python egg.py
# Enter the file name: missing.tyxt
# File cannot be opened: missing.tyxt
# python egg.py
# Enter the file name: na na boo boo
# NA NA BOO BOO TO YOU - You have been punk'd!
# We are not encouraging you to put Easter Eggs in your programs; this is just an
# exercise.
