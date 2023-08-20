#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <iomanip>
#include <stdio.h>

#include <set>
#include <unordered_set>
#include <bitset>
#include <map>
#include <unordered_map>
#include <queue>
#include <deque>
#include <vector>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define ll long long
#define ld long double
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define ii pair<int, int>
#define pli pair<ll, int>
#define pll pair<ll, ll>
#define pil pair<int, ll>
#define plii pair<ll, pair<int, int>>
#define heapmax(type) priority_queue<type>
#define heapmin(type) priority_queue<type, vector<type>, greater<type>>
#define ordered_multiset tree<int, null_type, less_equal<int>, rb_tree_tag, tree_order_statistics_node_update>
#define ordered_set tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update>
#define FASTIO                  \
    ios::sync_with_stdio(NULL); \
    cin.tie(NULL);              \
    cout.tie(NULL);
#define sz(x) (int)x.size()
#define all(x) (x).begin(), (x).end()
#define getbit(mask, i) ((mask >> i) & 1)

template <typename T>
bool maximize(const T &res, const T &val)
{
    if (res < val)
    {
        res = val;
        return true;
    }
    return false;
}
template <typename T>
bool minimize(const T &res, const T &val)
{
    if (res > val)
    {
        res = val;
        return true;
    }
    return false;
}
template <typename T>
ll rv_num(T x)
{
    ll res = 0;
    while (x > 0)
        res = res * 10 + x % 10, x /= 10;
    return res;
}
const ll mod = 1e9 + 7;
const ld PI = acos(-1);
const int N = 1e6 + 100;
const int N_Trie = 1e5;
const int N_ST = 2e5 + 10;
const int N_BIT = 2e5 + 10;
const int ooint = (1LL << 31) - 1;
const int ooll = (1LL << 63) - 1;
const int LIM = 1e7;   // N_Prime
const int N_MST = 1e5; // N of Merge Sort Tree
const int N_Hash = 2e6 + 10;

// sort(all(V));
// V.resize(unique(all(V)) - V.begin());*/

struct Trie_Number
{
    struct DT
    {
        ii c[2];
    };
    DT trie[32 * N_Trie];
    bool save[33];
    int pw[32], am = 0;
    void Built_PW()
    {
        pw[0] = 1;
        for (int i = 1; i < 32; i++)
            pw[i] = pw[i - 1] * 2;
    }
    void _reset()
    {
        memset(save, 0, sizeof(save));
        memset(trie, 0, sizeof(trie));
    }
    void _change(int x)
    {
        int p = 0;
        while (x > 0)
        {
            save[++p] = x % 2;
            x /= 2;
        }
        while (p < 32)
            save[++p] = 0;
    }
    void _add(int x)
    {
        _change(x);
        int node = 0;
        for (int i = 32; i >= 1; i--)
        {
            int w = save[i];
            if (!trie[node].c[w].fi)
                trie[node].c[w].fi = ++am;
            trie[node].c[w].se++;
            if (i > 1)
                node = trie[node].c[w].fi;
        }
    }
    void _delete(int x)
    {
        _change(x);
        int node = 0;
        for (int i = 32; i >= 1; i--)
        {
            int w = save[i];
            if (!trie[node].c[w].fi)
            {
                return;
            }
            if (trie[node].c[w].se == 0)
            {
                return;
            }
            if (i > 1)
                node = trie[node].c[w].fi;
        }
        node = 0;
        for (int i = 32; i >= 1; i--)
        {
            int w = save[i];
            // if (trie[node].c[w].se > 0)
            trie[node].c[w].se--;
            if (i > 1)
                node = trie[node].c[w].fi;
        }
    }
    int _get(int k)
    {
        int node = 0, res = 0;
        for (int i = 32; i >= 1; i--)
        {
            if (k <= trie[node].c[0].se)
            {
                if (!trie[node].c[0].se)
                    return -1;
                node = trie[node].c[0].fi;
            }
            else
            {
                if (!trie[node].c[1].se)
                    return -1;
                k = k - trie[node].c[0].second;
                node = trie[node].c[1].fi;
                res = res + pw[i - 1];
            }
        }
        return res;
    }
};
int lp[LIM + 2], pr[LIM], cnt = 0;
void Sieve(int N_SIEVE)
{
    lp[0] = -1;
    lp[1] = 0;
    for (int i = 2; i <= N_SIEVE; i++)
    {
        if (!lp[i])
            lp[i] = pr[++cnt] = i;
        for (int j = 1; j <= cnt && pr[j] <= lp[i] && pr[j] * i <= N_SIEVE; j++)
            lp[pr[j] * i] = pr[j];
    }
}
ll mul(ll a, ll b, ll c)
{ // O(log(min(a,b)))
    if (a < b)
        swap(a, b);
    ll res = 0;
    a = a % c;
    for (; b > 0; b >>= 1, a = (a + a) % c)
        if (b & 1)
            res = (res + a) % c;
    return res;
}
ll power(ll a, ll b, ll c)
{ // O(log(b))
    ll res = 1;
    a = a % c;
    for (; b > 0; b >>= 1, a = a * a % c)
        if (b & 1)
            res = res * a % c;
    return res;
}
ll power_mul(ll a, ll b, ll c)
{ // O(log(b)^2)
    ll res = 1;
    a = a % c;
    for (; b > 0; b >>= 1, a = mul(a, a, c))
        if (b & 1)
            res = mul(res, a, c);
    return res;
}
void file(const string FILE)
{
    if (fopen((FILE + ".INP").c_str(), "r"))
    {
        freopen((FILE + ".INP").c_str(), "r", stdin);
        freopen((FILE + ".OUT").c_str(), "w", stdout);
    }
}

int n, q;
ll a[N], pre[N], sq[N];
int main()
{
    FASTIO;
    cin >> n >> q;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
        pre[i] = (pre[i - 1] + a[i]) % mod;
        sq[i] = (sq[i - 1] + a[i] * a[i]) % mod;
    }
    for (int i = 1; i <= q; i++)
    {
        int l, r;
        cin >> l >> r;
        ll u = (pre[r] - pre[l - 1] + mod + mod) % mod;
        ll v = (sq[r] - sq[l - 1] + mod + mod) % mod;
        ll res = (u * u - v + mod * mod) % mod;
        res = (res * power(2, mod - 2, mod)) % mod;
        cout << res << "\n";
    }
    return 0;
}
