#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> v(n + 1);
        vector<pair<int, int>> vec;
        int mn = 1000;
        int mx = -1000;
        for (int i = 1; i <= n; i++)
        {
            cin >> v[i];
            mx = max(mx, v[i]);
            mn = min(mn, v[i]);
        }
        if (abs(mx) >= abs(mn) && mx > 0)
        {
            int id = -1;
            for (int i = 1; i <= n; i++)
            {
                if (mx == v[i])
                {
                    id = i;
                    break;
                }
            }
            for (int i = 1; i <= n; i++)
            {
                if (v[i] < 0)
                {
                    v[i] += mx;
                    vec.push_back({i, id});
                }
            }
            for (int i = 2; i <= n; i++)
            {
                if (v[i] < v[i - 1])
                {
                    v[i] += v[i - 1];
                    vec.push_back({i, i - 1});
                }
            }
        }
        else
        {
            int id = -1;
            for (int i = 1; i <= n; i++)
            {
                if (mn == v[i])
                {
                    id = i;
                    break;
                }
            }
            for (int i = 1; i <= n; i++)
            {
                if (v[i] > 0)
                {
                    v[i] += mn;
                    vec.push_back({i, id});
                }
            }
            for (int i = n - 1; i >= 1; i--)
            {
                if (v[i] > v[i + 1])
                {
                    v[i] += v[i + 1];
                    vec.push_back({i, i + 1});
                }
            }
        }
        cout << (int)vec.size() << "\n";
        for (auto it : vec)
        {
            cout << it.first << " " << it.second << "\n";
        }
    }
}