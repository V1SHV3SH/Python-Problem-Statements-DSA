hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Pay_Rate:")
r = float(rate)
hike=1.5
if h>40:
    extra=h-40
    h=h-extra
Gross = h*r+extra*r*hike
print(Gross)
