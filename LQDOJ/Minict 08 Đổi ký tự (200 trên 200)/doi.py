chuoi=str(input())
n=int(input())


sokytuphanbiet=len(set(chuoi))
sokytutrungnhau=len(chuoi)-sokytuphanbiet
sokytucandoi=n-sokytuphanbiet
if sokytucandoi<=0:
    print("0")
elif sokytucandoi>sokytutrungnhau:
    print("impossible")
else:
    print(sokytucandoi)