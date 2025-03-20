# Write a function called chop that takes a list and modifies it, removing
# the first and last elements, and returns None. Then write a function called middle
# that takes a list and returns a new list that contains all but the first and last
# elements.

letters = ['a', 'b', 'c']
letters1 = ['a', 'b', 'c']
def chop():
    del letters[0]
    del letters[-1]
    print(letters)

def middle(let):
    new = let[1:-1]
    return new

chop()
a = middle(letters1)
print(letters, letters1)
print(a)
