#include <bits/stdc++.h>
#define pb push_back
#define ff first
#define ss second
#define vt vector
#define ins insert
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define make_unique(x) \
    sort(all((x)));    \
    (x).resize(unique(all((x))) - (x).begin())
#define debug(...) " [" << #__VA_ARGS__ ": " << (_VA_ARGS_) << "] "
using namespace std;

typedef unsigned long ull;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
typedef pair<ll, ll> pll;
typedef map<int, int> mii;
typedef vt<int> vti;
const double Pi = acos(-1.0);
template <typename T>
ostream &operator<<(std::ostream &os, const std::vector<T> &vec)
{
    for (T x : vec)
        cout << x << ' ';
    cout << endl;
    return os;
}
const int inf = INT_MAX;

void Duck()
{
    int n;
    cin >> n;
    vt<ll> a(n);
    ll sum = 0;
    for (ll &i : a)
    {
        cin >> i;
        sum += i;
    }

    vt<ll> extended_a = a;
    extended_a.insert(extended_a.end(), a.begin(), a.end());
    vt<ll> prf(2 * n + 1, 0);
    for (int i = 0; i < 2 * n; ++i)
    {
        prf[i + 1] = prf[i] + extended_a[i];
    }

    ll mi = sum, L = 0, R = 0;
    for (int i = 1; i <= n; ++i)
    {
        for (int j = i; j <= 2 * n; j += i)
        {
            ll seg_sum = prf[j + 1] - prf[j - 1];
            if (mi > abs(sum - 2 * seg_sum))
            {
                L = seg_sum;
                R = sum - L;
            }
            mi = min(mi, abs(sum - 2 * seg_sum));
        }
    }
    if (L > R)
        swap(L, R);
    ll ans = min(R / 2, L);
    R -= ans * 2, L -= ans;
    ans += min(L / 2, R);
    cout << ans << endl;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    /*Duck3*/
    int t = 1;
    // #ifndef ONLINE_JUDGE
    //     freopen("input.txt", "r", stdin);
    //     cin >> t;
    // #endif

    while (t--)
        Duck();
    return 0;
}
/*
Test:

*/
