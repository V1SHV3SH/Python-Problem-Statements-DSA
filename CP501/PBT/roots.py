a=int(input("Enter the number a:"))
b=int(input("Enter the number b:"))
c=int(input("Enter the number c:"))
if (b**2) > (4*a*c):
    print("both roots printed")
elif (b**2) < (4*a*c):
    print("no roots")
else:
    root=(-1*b)/(2*a)
    print("only 1 root,x:",root)
