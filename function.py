x=input("Input hours first: ")
hrs=int(x)
y=input("Now input the Pay_Rate: ")
rate=float(y)
def computepay(h,r):
    if h>40:
        excs=h-40
        h=h-excs
        excs=excs*1.5
    pay=(h*r)+(excs*r)
    return pay
p = computepay(hrs, rate)
print(p)
