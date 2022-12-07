#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<pair<int, int>> v;
    for (int i = 1; i <= n; i++)
        if (i % 2 == 1)
        {
            int x;
            cin >> x;
            if (v.empty())
                v.push_back({1, x});
            else if (v.back().second != x)
                v.push_back({1, x});
            else
            {
                int temp = v.back().first;
                v.pop_back();
                v.push_back({temp + 1, x});
            }
        }
        else
        {
            int x;
            cin >> x;
            if (v.empty())
                v.push_back({1, x});
            else
            {
                int temp = v.back().first;
                v.pop_back();
                if (!v.empty())
                    if (v.back().second == x)
                    {
                        temp += v.back().first;
                        v.pop_back();
                    }
                v.push_back({temp + 1, x});
            }
        }
    long long res = 0;
    for (auto x : v)
        if (x.second == 0)
            res += x.first;
    cout << res;
    // cout << "\n";
    // for (auto x : v)
    //     cout << x.first << " " << x.second << "\n";
    return 0;
}