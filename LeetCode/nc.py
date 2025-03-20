def f(n: int) -> int:
    c = 0
    i=0
    while n >= 0:
        n -= 2
        c += n - 2
        i+=1# This part is ambiguous, but keeping it as in the pseudocode
    return c,i

o = int(input("Enter a number: "))
d,i = f(o)
print("iterations",i)
print(d)
