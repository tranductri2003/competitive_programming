t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Một số chẵn thì chia thành tổng 2 số lẻ hoặc tổng 2 số chẵn
    # Một số lẻ thì chia thành tổng 2 số lẻ
    # => Tức là mình chỉ có thể chia một số chẵn thành 2 số lẻ hoặc 2 số chẵn
    # => Tức là mình chỉ có thể chia một số chẵn thành 2 số lẻ
    # Tức là nếu cần thay đổi, thì mình chỉ có thể chia một số chẵn thành 2 số lẻ
    # Tức là dãy full lẻ hoặc full chẵn thì in ra 0
    # Else: chỉ có thể biến thành full lẻ
    res = 0
    for i in range(n-1):
        if a[i] % 2 == a[i+1] % 2:
            pass
        else:
            for num in a:
                if num % 2 == 0:
                    res += 1
            print(res)
            break
    else:
        print(0)
