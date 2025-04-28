# Rewrite the program that prompts the user for a list of numbers and prints out the
# maximum and minimum of the numbers at the end when the user enters “done”.
# Write the program to store the numbers the user enters in a list and use the max()
# and min() functions to compute the maximum and minimum numbers after the
# loop completes.
# 8.16. EXERCISES 107
# Enter a number: 6
# Enter a number: 2
# Enter a number: 9
# Enter a number: 3
# Enter a number: 5
# Enter a number: done
# Maximum: 9.0
# Minimum: 2.0

numbers = []
num = 0
while num!= 'done' :
    num = input('Enter a number: ')
    if num == 'done' : continue
    num = int(num)
    numbers.append(num)
max = max(numbers)
min = min(numbers)
print(f'Maximum: {max} \nMinimum: {min}')
