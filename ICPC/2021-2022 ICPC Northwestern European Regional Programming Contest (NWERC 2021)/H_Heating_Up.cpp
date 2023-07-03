#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1000005;

long long a[MAXN], n;
pair<long long, int> v[MAXN];

bool check(long long mid)
{
    vector<bool> vis(MAXN, 0);
    for (int j = 1; j <= n; j++)
    {
        if (mid < v[j].first)
            return false;
        else if (!vis[v[j].second])
        {
            int i = v[j].second;
            vis[v[j].second] = true;
            int l = i - 1, r = i + 1;
            if (l <= 0)
                l += n;
            if (r > n)
                r %= n;
            long long count = mid + a[i];
            bool ch = true;
            while (l != r)
            {
                bool kt_temp = false;
                if (count >= a[l])
                {
                    vis[l] = true;
                    count += a[l];
                    kt_temp = true;
                    l--;
                    if (l <= 0)
                        l = n;
                }
                else if (count >= a[r])
                {
                    count += a[r];
                    vis[r] = true;
                    kt_temp = true;
                    r++;
                    if (r > n)
                        r %= n;
                }
                if (!kt_temp)
                {
                    ch = false;
                    break;
                }
            }
            if (ch && count >= a[l])
                return true;
        }
    }
    return false;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
        v[i] = {a[i], i};
    }
    sort(v + 1, v + n + 1);

    long long l = 0, r = 1e13;
    while (l < r)
    {
        long long mid = (l + r) / 2;
        if (check(mid))
            r = mid;
        else
            l = mid + 1;
    }
    long long mid = (l + r) / 2;
    if (mid < 0)
        mid = 0;
    while (!check(mid))
        mid++;
    while (mid - 1 >= 0 && check(mid - 1))
        mid--;
    cout << mid;

    return 0;
}