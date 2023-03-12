#include <bits/stdc++.h>
using namespace std;

#define sz(a) (int)(a.size())
#define all(a) (a).begin(), (a).end()

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    if (fopen("in.txt", "r"))
    {
        freopen("in.txt", "r", stdin);
        freopen("ou.txt", "w", stdout);
    }

    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;

        vector<int> a(n);
        for (int i = 0; i < n; i++)
            cin >> a[i];
        map<int, int> cnt;
        for (int x : a)
            cnt[x]++;

        int _x = -1, _y = 0, ans = 0;
        for (auto [x, y] : cnt)
        {
            if (x == _x + 1)
            {
                if (_y > y)
                {
                    ans += _y - y;
                }
            }
            else
            {
                ans += _y;
            }
            _x = x;
            _y = y;
        }

        ans += _y;
        cout << ans << '\n';
    }
}
