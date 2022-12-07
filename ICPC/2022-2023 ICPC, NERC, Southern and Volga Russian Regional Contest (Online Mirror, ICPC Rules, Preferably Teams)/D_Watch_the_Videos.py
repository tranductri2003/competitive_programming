from collections import defaultdict
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))


a = sorted(a)
print(a)
res = 0
curMem = 0
i = 0  # Video đang xét hiện tại
check = defaultdict(lambda: 0)
while i != n:
    print("Xem video thu", i+1)
    res += a[i]  # Ngồi đợi tải xong video hiện tại
    print(res)
    if check[i] == 0:
        curMem += a[i]

    # Nếu như tải luôn cái video sau được thì trong lúc mình xem sẽ tải video sau
    if i+1 < n and curMem+a[i+1] <= m:
        print("Du bo nho")
        if check[i+1] == 0:
            curMem += a[i+1]  # Thêm bộ nhớ của video sau
            check[i+1] = 1
        a[i+1] -= 1  # Trong lúc xem thì tải được thêm 1 phút video sau

        # Thời gian để xem video hiện tại (Kết hợp ngồi tải video sau)
        res += 1

        print(res)

        curMem -= a[i]  # Xóa bộ nhớ của video hiện tại
        i += 1  # Chuyển đến video sau
    else:  # Nếu như không đủ bộ nhớ để tải thì phải đợi để xem hết rồi xóa rồi tải cái mới
        print("Khong du bo nho")
        res += 1  # Thời gian ngồi xem cho hết video hiện tại
        print(res)
        curMem -= a[i]  # Xóa bộ nhớ của video hiện tại
        i += 1  # Chuyển đến video sau
