import math
print(math.pi)
radius=float(input("radius?:"))
if radius<0:
    print("radius is not a positive number")
while radius>=0:
    pi=3.14
    circum=2*math.pi*radius
    print("circumference:",circum)
    if circum<100:
        print("it is too small")
    break
