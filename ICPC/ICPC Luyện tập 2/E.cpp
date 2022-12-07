#include <bits/stdc++.h>
using namespace std;

long long n, a[120], x;
int dp[120];

int recur(int x)
{
    if (dp[x] != -1)
        return dp[x];
    int check = 1;
    for (int i = 1; i <= n; i++)
        if (x >= a[i])
            check &= recur(x - a[i]);

    if (check == 1)
        return dp[x] = 0;
    else
        return dp[x] = 1;
}

int main()
{
    cin >> x >> n;
    for (int i = 1; i <= n; i++)
        cin >> a[i];
    memset(dp, -1, sizeof(dp));
    dp[0] = 0;
    recur(x);
    if (dp[x] == 1)
        cout << "Tuan";
    else
        cout << "Hao";
}