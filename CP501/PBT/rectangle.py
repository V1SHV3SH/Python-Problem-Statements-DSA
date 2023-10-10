len=int(input("Enter length:"))
wid=int(input("Enter width:"))
if len>0 and wid>0:
    area=len*wid
    print("Area of rectangle is",area)
else:
    print("Error: Both the length and width must be positive numbers")
