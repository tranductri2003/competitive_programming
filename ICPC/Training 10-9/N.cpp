#include <bits/stdc++.h>
#define fo(i, n) for (int i = 0; i < (n); i++)
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
#define debug(...) " [" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "] "
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
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    map<ll, pii> mp;
    for (int i = 0; i < n; i++)
    {
        int l = i;
        int r = i;
        while (a[l] == a[r + 1] && r + 1 < n)
        {
            r++;
            i++;
        }
        // cout << debug(i);
        mp[a[i]] = make_pair(l, r);
    }
    ll s = 0;
    int q;
    cin >> q;
    while (q--)
    {
        char t;
        cin >> t;
        if (t == 's')
        {
            int k;
            cin >> k;
            s += k;
            if (s < 0)
                s += n;
            else
                s %= n;
        }
        else
        {
            ll x;
            cin >> x;
            if (mp.find(x) != mp.end())
            {
                int l = mp[x].ff, r = mp[x].ss;
                if (l == r)
                {
                    cout << (l + s + n) % n + 1 << '\n';
                }
                else
                {
                    int d = r - l + 1;
                    l = (l + s + n) % n + 1;
                    r = (r + s + n) % n + 1;
                    if (n - l >= d)
                    {
                        cout << l << '\n';
                    }
                    else
                    {
                        cout << 1 << '\n';
                    }
                }
            }
            else
            {
                cout << -1 << '\n';
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    /*Duck3*/
    int t = 1;
    //	cin >> t;

    while (t--)
        Duck();
    return 0;
}
/*
Test:

*/
