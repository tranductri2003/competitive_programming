from collections import defaultdict
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    s = input()

    sample = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    thuong = defaultdict(lambda: 0)
    hoa = defaultdict(lambda: 0)
    # print(sample[0], sample[26])
    for i in range(n):
        if s[i].lower() == s[i]:
            thuong[s[i]] += 1
        else:
            hoa[s[i]] += 1
    for i in range(26):
        tt = thuong[sample[i]]
        h = hoa[sample[i+26]]
        if tt > h:
            thuong[sample[i]] = h
            hoa[sample[i+26]] = tt

        new = (thuong[sample[i]]+hoa[sample[i+26]])//2

        use = new-thuong[sample[i]]
        temp = min(k, use)
        k -= temp
        thuong[sample[i]] += temp
        hoa[sample[i+26]] -= temp
    res = 0
    for i in range(26):
        res += min(thuong[sample[i]], hoa[sample[i+26]])
    print(res)
