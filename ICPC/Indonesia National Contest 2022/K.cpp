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

template <typename T>
class graph
{
public:
    struct edge
    {
        int from;
        int to;
        T cost;
    };

    vector<edge> edges;
    vector<vector<int>> g;
    int n;

    graph(int _n) : n(_n)
    {
        g.resize(n);
    }

    virtual int add(int from, int to, T cost) = 0;
};

template <typename T>
class forest : public graph<T>
{
public:
    using graph<T>::edges;
    using graph<T>::g;
    using graph<T>::n;

    forest(int _n) : graph<T>(_n)
    {
    }

    int add(int from, int to, T cost = 1)
    {
        assert(0 <= from && from < n && 0 <= to && to < n);
        int id = (int)edges.size();
        assert(id < n - 1);
        g[from].push_back(id);
        g[to].push_back(id);
        edges.push_back({from, to, cost});
        return id;
    }
};

template <typename T>
class dfs_forest : public forest<T>
{
public:
    using forest<T>::edges;
    using forest<T>::g;
    using forest<T>::n;

    vector<int> pv;
    vector<int> pe;
    vector<int> order;
    vector<int> pos;
    vector<int> end;
    vector<int> sz;
    vector<int> root;
    vector<int> depth;
    vector<T> dist;

    dfs_forest(int _n) : forest<T>(_n)
    {
    }

    void init()
    {
        pv = vector<int>(n, -1);
        pe = vector<int>(n, -1);
        order.clear();
        pos = vector<int>(n, -1);
        end = vector<int>(n, -1);
        sz = vector<int>(n, 0);
        root = vector<int>(n, -1);
        depth = vector<int>(n, -1);
        dist = vector<T>(n);
    }

    void clear()
    {
        pv.clear();
        pe.clear();
        order.clear();
        pos.clear();
        end.clear();
        sz.clear();
        root.clear();
        depth.clear();
        dist.clear();
    }

private:
    void do_dfs(int v)
    {
        pos[v] = (int)order.size();
        order.push_back(v);
        sz[v] = 1;
        for (int id : g[v])
        {
            if (id == pe[v])
            {
                continue;
            }
            auto &e = edges[id];
            int to = e.from ^ e.to ^ v;
            depth[to] = depth[v] + 1;
            dist[to] = dist[v] + e.cost;
            pv[to] = v;
            pe[to] = id;
            root[to] = (root[v] != -1 ? root[v] : to);
            do_dfs(to);
            sz[v] += sz[to];
        }
        end[v] = (int)order.size() - 1;
    }

    void do_dfs_from(int v)
    {
        depth[v] = 0;
        dist[v] = T{};
        root[v] = v;
        pv[v] = pe[v] = -1;
        do_dfs(v);
    }

public:
    void dfs(int v, bool clear_order = true)
    {
        if (pv.empty())
        {
            init();
        }
        else
        {
            if (clear_order)
            {
                order.clear();
            }
        }
        do_dfs_from(v);
    }

    void dfs_all()
    {
        init();
        for (int v = 0; v < n; v++)
        {
            if (depth[v] == -1)
            {
                do_dfs_from(v);
            }
        }
        assert((int)order.size() == n);
    }
};

void Duck()
{
    int n;
    cin >> n;
    vti a(n + 1);
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
    }
    vt<vti> g(n + 1);
    // cout << a;
    vti deg(n + 1);
    for (int i = 1; i <= n; i++)
    {
        if (a[i] != -1)
        {
            g[a[i]].pb(i);
            deg[i]++;
        }
    }
    int curchild = n;
    for (int i = n - 1; i >= 1; i--)
    {
        if (a[i] == -1 || a[i] > curchild)
        {
            g[i].pb(curchild);
            deg[curchild]++;
            curchild = i;
        }
    }
    // cout << g << endl;
    int tot = 0;
    for (int i = 1; i <= n; i++)
    {
        tot += g[i].size();
    }
    if (tot >= n)
    {
        cout << -1;
        return;
    }
    dfs_forest<int> G(n);
    for (int u = 1; u <= n; u++)
    {
        for (int v : g[u])
            G.add(u - 1, v - 1);
    }
    for (int i = 1; i <= n; i++)
    {
        if (deg[i] == 0)
        {
            G.dfs(i - 1);
            break;
        }
    }

    // cout << G.depth;
    int cur = n;
    map<int, vti> mp;
    for (int i = 0; i < n; i++)
    {
        mp[G.depth[i]].pb(i);
        if (G.depth[i] == -1)
        {
            cout << -1;
            return;
        }
    }
    vti ans(n);
    for (auto it = mp.begin(); it != mp.end(); ++it)
    {
        for (auto i : it->second)
        {
            ans[i] = cur--;
        }
    }
    cout << ans;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    /*Duck3*/
    int t = 1;
    // #ifndef ONLINE_JUDGE
    //     freopen("input.txt", "r", stdin);
    // #endif
    // cin >> t;
    while (t--)
        Duck();
    return 0;
}
/*
Test:

*/
