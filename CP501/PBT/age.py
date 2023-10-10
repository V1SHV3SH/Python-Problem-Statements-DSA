age=int(input("enter the age:"))
under5 = age<5
oap = age>=65
under18 = age<18
if under5:
    print ("free")
elif under18:
    print ("half-price")
elif oap:
    print ("half-price")
else:
    print ("full price")
