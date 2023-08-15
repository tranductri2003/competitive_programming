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
    string s;
    cin >> s;
    int n = s.size();
    for (int i = 2; i <= n; i *= 2)
    {
        for (int j = 0; i + j - 1 < n; j += i)
        {
            reverse(s.begin() + j, s.begin() + i + j);
        }
    }
    cout << s << '\n';
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