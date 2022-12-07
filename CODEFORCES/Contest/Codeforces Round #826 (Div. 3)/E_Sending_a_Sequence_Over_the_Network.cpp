#include <bits/stdc++.h>

using namespace std;

int a[200001], n, dp[200011];

vector<int> Q[200011];

void solve()
{

    cin >> n;

    for (int i = 1; i <= n; ++i)
        cin >> a[i];

    for (int i = 0; i <= n + 10; ++i)
    {
        Q[i].clear();
        dp[i] = false;
    }

    for (int i = 1; i <= n; ++i)
    {

        int l = i, r = a[i] + i;

        if (r <= n)
            Q[l].push_back(r);

        l = i - a[i], r = i;

        if (l >= 1)
            Q[l].push_back(r);
    }

    dp[1] = true;

    for (int i = 1; i <= n; ++i)
    {

        if (!dp[i])
            continue;

        for (int j : Q[i])
            dp[j + 1] = true;
    }

    cout << (dp[n + 1] ? "YES" : "NO") << endl;
}

int main()
{

    int T;

    cin >> T;

    while (T--)
        solve();
}
