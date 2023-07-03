# https://bkdnoj.dut.udn.vn/public/practice_problem.php?id=DUT21A
a = [1]
for i in range(10**7):
    a.append(i)

xa, ya = list(map(int, input().split()))
xb, yb = list(map(int, input().split()))
xc, yc = list(map(int, input().split()))

ccw = (xb-xa)*(yc-ya)-(yb-ya)*(xc-xa)

if ccw > 0:
    print("LEFT")
else:
    if ccw < 0:
        print("RIGHT")
    else:
        print("TOWARDS")
