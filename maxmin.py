largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        I=int(num)
    except:
        print("Invalid input")
    print(num)
    if largest is None:
        largest=I
        smallest=I
    if I>largest:
        largest=I
    if smallest>I:
        smallest=I
print("Maximum", largest)
print("Minimum is", smallest)
