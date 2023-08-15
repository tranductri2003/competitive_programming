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
    ll k;
    cin >> k;
    int n;
    cin >> n;

    vector<ll> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    sort(a.begin(), a.end());
    int ans1 = 0;
    ll ans2 = 0;
    do
    {
        ll T = 0;
        ll s = 0;
        int cnt = 0;
        for (int i = 0; i < n; i++)
        {
            if (T + a[i] > k)
                break;
            cnt++;
            T += a[i];
            s += T;
        }
        if (cnt > ans1)
        {
            ans1 = cnt;
            ans2 = (s - (s / 1440) * 1440);
        }
        else if (cnt == ans1)
        {
            ans2 = min(ans2, s - (s / 1440) * 1440);
        }

    } while (next_permutation(a.begin(), a.end()));
    cout << ans1 << ' ' << ans2;
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