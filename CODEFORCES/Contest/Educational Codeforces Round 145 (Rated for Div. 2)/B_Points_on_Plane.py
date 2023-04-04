import math


t = int(input())
for _ in range(t):
    n = int(input())
    # l = 0
    # r = 10**9+7
    # res = 0
    # # tìm k min sao cho (k+1)^2>=n
    # while l <= r:
    #     m = (l+r)//2
    #     if (m+1)*(m+1) >= n:
    #         res = m
    #         r = m-1
    #     else:
    #         l = m+1
    # print(res)
    temp = int(math.sqrt(n))
    if temp*temp >= n:
        print(temp-1)
    else:
        print(temp)
    # include <bits/stdc++.h>
    # C++17
    # using namespace std

    # int main()
    # {
    #     int test = 0
    #     cin >> test
    #     while (test--)
    #     {
    #         long long n
    #         cin >> n
    #         cout << (long long)sqrt(n - 1) << endl
    #     }
    # }
