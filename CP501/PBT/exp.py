import math
a=[]
for i in range(0,4):
    val=float(input("Enter a number:"))
    a.append(val)
print("     X|  e*X /n ----------")
print(a)
for i in a:
    print("%.2f %.2f"%(i,(math.e)*i))
