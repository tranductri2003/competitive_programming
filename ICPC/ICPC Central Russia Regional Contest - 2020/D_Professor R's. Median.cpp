#include <bits/stdc++.h>
#define ll long long
#define fi first
#define se second
#define pb push_back
const ll inf = 1e18;
const long double esp = 1e-12;
const ll mod = 1e9 + 7;
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define ordered_set tree<pair<int, int>, null_type, less<pair<int, int>>, rb_tree_tag, tree_order_statistics_node_update>
void solve()
{
    int n;
    cin >> n;
    vector<ll> a(n);
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        a[i] *= 2;
    }
    sort(a.begin(), a.end());
    ll mid = (a[0] + a[n - 1]) / 2;
    int vt = 0;
    for (int i = 1; i < n; i++)
    {
        if (abs(a[vt] - mid) > abs(a[i] - mid))
            vt = i;
    }
    cout << a[vt] / 2 << '\n';
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int test = 1;
    // cin>>test;
    while (test--)
    {
        solve();
    }
    return 0;
}