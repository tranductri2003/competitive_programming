#include <bits/stdc++.h>
using namespace std;
#define fi first
#define se second
// std::vector<bitset<5005>> m;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // m.assign(5005, bitset<5005>(0));
    long long n;
    cin >> n;
    map<pair<int, int>, bool> m;
    int a[3001][3];
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i][1] >> a[i][2];
        m[{a[i][1], a[i][2]}] = true;
    }
    long long res = 0;
    int dem = 0;
    for (int i = 1; i < n; i++)
        for (int j = i + 1; j <= n; j++)
        {
            double x = (a[i][1] + a[j][1]) / 2.0;
            double y = (a[i][2] + a[j][2]) / 2.0;
            double v1 = (a[i][1] - a[j][1]) / 2.0;
            double v2 = (a[i][2] - a[j][2]) / 2.0;
            swap(v1, v2);
            v1 *= -1;
            double t1_x = x + v1;
            double t1_y = y + v2;
            double t2_x = x - v1;
            double t2_y = y - v2;
            if (t1_x == int(t1_x) && t1_y == int(t1_y) && t2_x == int(t2_x) && t2_y == int(t2_y))
            {
                if (m[{int(t1_x), int(t1_y)}] && m[{int(t2_x), int(t2_y)}])
                {
                    long long t1 = a[i][1] - a[j][1];
                    long long t2 = a[i][2] - a[j][2];
                    res = max(res, (t1 * t1 + t2 * t2) / 2);
                    // cout<<i<<" "<<j<<" "<<t1<<" "<<t2<<"\n";
                }
            }
            // dem++;
        }
    // cout<<dem<<"\n";
    cout << res;
}