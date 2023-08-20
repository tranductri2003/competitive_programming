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

struct nodeq
{
    int type, k;
    int a, b;
};
int n, q, a[N];
nodeq ques[N];
vector<int> V;

void compress()
{
    for (int i = 1; i <= n; i++)
        V.pb(a[i]);
    for (int i = 1; i <= q; i++)
    {
        if (ques[i].type == 1)
            V.pb(ques[i].k);
        else
            V.pb(ques[i].a), V.pb(ques[i].b);
    }
    sort(all(V));
    V.resize(unique(all(V)) - V.begin());
    for (int i = 1; i <= n; i++)
    {
        a[i] = lower_bound(all(V), a[i]) - V.begin() + 1;
    }
    for (int i = 1; i <= q; i++)
    {
        if (ques[i].type == 1)
        {
            ques[i].k = lower_bound(all(V), ques[i].k) - V.begin() + 1;
        }
        else
        {
            ques[i].a = lower_bound(all(V), ques[i].a) - V.begin() + 1;
            ques[i].b = lower_bound(all(V), ques[i].b) - V.begin() + 1;
        }
    }
    return;
}

int bit[4 * N], sz;

void update(int x, int val)
{
    for (; x <= sz; x += x & (-x))
        bit[x] += val;
}

int query(int x)
{
    int res = 0;
    for (; x > 0; x -= x & (-x))
    {
        res = res + bit[x];
    }
    return res;
}
int main()
{
    FASTIO;
    cin >> n >> q;
    for (int i = 1; i <= n; i++)
        cin >> a[i];
    for (int i = 1; i <= q; i++)
    {
        cin >> ques[i].type;
        if (ques[i].type == 1)
        {
            cin >> ques[i].k;
        }
        else
        {
            cin >> ques[i].a >> ques[i].b;
        }
    }
    compress();
    sz = V.size();
    multiset<int> ss;
    for (int i = 1; i <= n; i++)
    {
        ss.insert(a[i]);
        update(a[i], 1);
    }
    for (int i = 1; i <= q; i++)
    {
        if (ques[i].type == 1)
        {
            int x = ques[i].k;
            auto f = ss.find(x);
            if (f != ss.end())
                continue;
            if (x > *ss.rbegin())
            {
                ss.insert(x);
                update(x, 1);
            }
            else
            {
                auto fx = ss.lower_bound(x);
                update(*fx, -1);
                ss.erase(fx);
                update(x, 1);
                ss.insert(x);
            }
        }
        else
        {
            cout << query(ques[i].b) - query(ques[i].a - 1) << "\n";
        }
    }
    return 0;
}
