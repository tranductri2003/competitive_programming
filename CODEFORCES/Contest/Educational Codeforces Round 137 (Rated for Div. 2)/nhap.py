n = int(input())
a = list(map(int, input().split()))
a.sort()
# res1=tich max cua 2 phan tu
# res2=tich max cua 3 phan tu
# res=max(res1,res2)


# TH1: Tích lớn nhất từ việc lấy 2 số
res1 = max(a[0]*a[1], a[-1]*a[-2])

# TH2: Tích lớn nhất từ việc lấy 3 số
res2 = max(a[-1]*a[-2]*a[-3], a[0]*a[1]*a[-1])
res = max(res1, res2)
print(res)
