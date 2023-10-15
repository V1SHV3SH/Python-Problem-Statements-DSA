sum = 0
i = 0
x = int(input ("Enter a number :") )
if x<0:
    print("no number has been entered")
else:
    while x>=0:
        sum = sum + x
        i = i + 1
        x = int(input ("Enter a number :") )
mean = sum / i
print ("Sum is",sum,"& Mean is %.2f"%mean)
