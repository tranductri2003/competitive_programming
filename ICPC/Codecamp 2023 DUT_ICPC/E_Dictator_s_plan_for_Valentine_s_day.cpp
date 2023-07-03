#include <bits/stdc++.h>

using namespace std;

struct Guards
{
    int l, r, x;
};
bool cmp(Guards a, Guards b)
{
    if (a.x == b.x)
        return a.l < b.l;
    return a.x < b.x;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int m, n;
    cin >> m >> n;
    vector<Guards> guards(m);
    for (int i = 0; i < m; ++i)
        cin >> guards[i].l >> guards[i].r >> guards[i].x;
    set<pair<int, int>> times;
    for (int i = 0; i < n; ++i)
    {
        int t;
        cin >> t;
        times.insert(make_pair(t, i));
    }
    sort(guards.begin(), guards.end(), cmp);
    vector<int> ans(n, -1);
    for (int i = 0; i < m && !times.empty(); ++i)
    {
        auto itl = times.upper_bound(make_pair(guards[i].l - guards[i].x - 1, -1));
        auto itr = times.lower_bound(make_pair(guards[i].r - guards[i].x - 1, n));
        if (itl != times.end() && (*itl).first <= (*itr).first)
        {
            ans[(*itl).second] = guards[i].x;
            times.erase(itl);
        }
    }
    for (int e : ans)
        cout << e << '\n';
    return 0;
}
