import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("x1 =", x1)
    print("x2 =", x2)
elif D == 0:
    x = -b / (2*a)
    print("x =", x)
else:
    print("no solution")
