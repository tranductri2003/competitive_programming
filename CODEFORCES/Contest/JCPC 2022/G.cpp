#include <bits/stdc++.h>
#define ll long long
#define db double
#define fi first
#define se second
#define ii pair<int, int>
#define mp make_pair
#define pb push_back

using namespace std;

int n, q;
vector<int> a;
map<int, int> ma;

struct BIT
{
    int n;
    vector<int> node;
    BIT(int _n = 0)
    {
        n = _n;
        node.resize(4 * n + 7);
    }
    void upd(int pos, int val, int in, int l, int r)
    {
        if (pos < l || pos > r)
        {
            return;
        }
        if (l == r)
        {
            node[in] = val;
            return;
        }
        int m = (l + r) / 2;
        upd(pos, val, 2 * in, l, m);
        upd(pos, val, 2 * in + 1, m + 1, r);
        node[in] = min(node[2 * in], node[2 * in + 1]);
    }
    void upd(int pos, int val)
    {
        upd(pos, val, 1, 1, n);
    }
    int get_min(int u, int v, int in, int l, int r)
    {
        if (v < l || r < u)
        {
            return INT_MAX;
        }
        if (l >= u && r <= v)
            return node[in];
        int m = (l + r) / 2;
        return min(get_min(u, v, 2 * in, l, m), get_min(u, v, 2 * in + 1, m + 1, r));
    }
    int get_min(int u, int v)
    {
        return get_min(u, v, 1, 1, n);
    }
};

void ip()
{
    ma.clear();
    a.clear();
    priority_queue<ii, vector<ii>, greater<ii>> pq;
    cin >> n >> q;
    BIT T(n);
    for (int i = 1; i <= n; ++i)
    {
        int a1;
        cin >> a1;
        a.pb(a1);
        pq.push({a1, i - 1});
        ma[a1] = INT_MAX;
    }
    int maxVal = *max_element(a.begin(), a.end());
    for (int i = 0; i < a.size(); ++i)
    {
        while (pq.size() && pq.top().se < i)
            pq.pop();
        ma[a[i]] = min(pq.top().fi, ma[a[i]]);
    }
    sort(a.begin(), a.end());
    for (int i = 0; i < a.size(); ++i)
    {
        T.upd(i + 1, ma[a[i]]);
    }
    while (q--)
    {
        int u, v;
        cin >> u >> v;
        if (u <= v)
        {
            cout << (maxVal >= v ? "Yes\n" : "No\n");
        }
        else
        {
            auto it = lower_bound(a.begin(), a.end(), u);
            if (it == a.end())
            {
                cout << "No\n";
                continue;
            }
            int val = it - a.begin() + 1;
            cout << (T.get_min(val, n) <= v ? "Yes\n" : "No\n");
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    if (fopen("T.INP", "r"))
    {
        freopen("T.INP", "r", stdin);
        freopen("T.OUT", "w", stdout);
    }
    if (fopen("milk.in", "r"))
        freopen("milk.in", "r", stdin);
    int t = 1;
    cin >> t;
    while (t--)
        ip();
}