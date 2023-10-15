import math
x=float(input("Initial x :"))
rows=float(input("Number of rows:"))
inc=float(input("Increment by :"))
limit=rows*inc
print ("       x   exp(x)")
while x<limit:
    print("%8.2f %8.2f"%(x,math.exp(x)))
    x=x+inc
