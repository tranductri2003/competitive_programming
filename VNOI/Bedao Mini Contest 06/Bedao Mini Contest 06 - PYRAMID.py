import math
X, Y = list(map(float, input().split()))

# Truong hop Huyen-Nho=X
delta = 4*(X**2+2*X*Y+Y**2)-4*(Y**2-X**2)
a1 = (2*(X+Y)+math.sqrt(delta))/2
a2 = (2*(X+Y)-math.sqrt(delta))/2


b1 = Y-a1
c1 = a1+X

b2 = Y-a2
c2 = a2+X

if 0 < a1 < b1 < c1 and a1+b1 > c1 and a1+c1 > b1 and b1+c1 > a1:
    a1 = format((2*(X+Y)+math.sqrt(delta))/2, ".9f")
    b1 = format(Y-float(a1), ".9f")
    c1 = format(float(a1)+X, ".9f")
    print(a1, b1, c1)
elif 0 < a2 < b2 < c2 and a2+b2 > c2 and a2+c2 > b2 and b2+c2 > a2:
    a2 = format((2*(X+Y)-math.sqrt(delta))/2, ".9f")
    b2 = format(Y-float(a2), ".9f")
    c2 = format(float(a2)+X, ".9f")
    print(a2, b2, c2)
else:
    # Truong hop huyen - Lon = X
    delta = 8*X**2+8*X*Y
    a1 = ((-2*X)+math.sqrt(delta))/(2)
    a2 = ((-2*X)-math.sqrt(delta))/(2)

    b1 = Y-a1
    c1 = b1+X

    b2 = Y-a2
    c2 = b2+X

    if 0 < a1 < b1 < c1 and a1+b1 > c1 and a1+c1 > b1 and b1+c1 > a1:
        a1 = format((-2*X+math.sqrt(delta))/2, ".9f")
        b1 = format(Y-float(a1), ".9f")
        c1 = format(float(b1)+X, ".9f")
        print(a1, b1, c1)
    elif 0 < a2 < b2 < c2 and a2+b2 > c2 and a2+c2 > b2 and b2+c2 > a2:
        a2 = format((-2*X-math.sqrt(delta))/2, ".9f")
        b2 = format(Y-float(a2), ".9f")
        c2 = format(float(b2)+X, ".9f")
        print(a2, b2, c2)
