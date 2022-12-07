#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
#define fi first
#define se second
#define mp make_pair
//#define int long long
#define sz(x) (int)(x).size()
#define all(x) (x).begin(), (x).end()
#define rep(i, l, r) for (int i = (int)(l); i <= (int)(r); i++)
#define per(i, r, l) for (int i = (int)(r); i >= (int)(l); i--)
const int mod = 1e9 + 7;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    //    freopen((file + ".inp").c_str(), "r", stdin);
    //    freopen((file + ".out").c_str(), "w", stdout);

    int n;
    cin >> n;

    map<pii, int> cnt;
    rep(i, 1, n)
    {
        int a, b, c;
        cin >> a >> b >> c;

        int g = __gcd(a, b);
        a /= g;
        b /= g;

        if (a < 0)
        {
            a *= -1;
            b *= -1;
        }

        cnt[mp(a, b)]++;
    }

    ll ans = n * (ll)(n - 1) * (n - 2) / 6;
    for (auto x : cnt)
    {
        ans -= x.se * (ll)(x.se - 1) * (x.se - 2) / 6 + x.se * (ll)(x.se - 1) / 2 * (n - x.se);
    }

    cout << ans % mod << "\n";

    //    cerr << "Time: " << 1000 * clock() / CLOCKS_PER_SEC << " ms\n";

    return 0;
}
